#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import scipy
import controller
import numpy as np
from enum import Enum
from scipy.interpolate import UnivariateSpline
from moveit_msgs.msg import OrientationConstraint, Constraints, CollisionObject
from geometry_msgs.msg import PoseStamped, Vector3, Point, Quaternion, Pose
from shape_msgs.msg import SolidPrimitive
from intera_interface import Limb
import tf2_ros
import math
from geometry_msgs.msg import Wrench
from intera_core_msgs.msg import EndpointState

from intera_interface import gripper as robot_gripper
import traceback
import utils

from copy import deepcopy

from segmentation.msg import wound
# from tf import Vector3

MAX_SPEED = 1.0
POS_THRESHOLD = 0.1 
# STATE_THRESHOLD = 300
ROT_THRESHOLD = 0.25 ## degrees
ROS_PUBLISH_RATE = 1000 ## Hz
MODIFICATION_SCALE = 0.000001
MODIFICATION_SPEED_POWER = 0.7
MODIFICATION_DISTANCE_POWER = 1


class PathPlanner(object):
    """
    Path Planning Functionality for Nurse Sawyer

    Fields:
    _robot: moveit_commander.RobotCommander; for interfacing with the robot
    _scene: moveit_commander.PlanningSceneInterface; the planning scene stores a representation of the environment
    _group: moveit_commander.MoveGroupCommander; the move group is moveit's primary planning class
    _planning_scene_publisher: ros publisher; publishes to the planning scene

    _base: Sawyer's base link height.
    _table: Table height.
    _tx: Table thickness.
    _phantom: Phantom height.
    _spacing: Stitch spacing.
    _radius: Needle radius.
    _string: String length.
    """    

    def __init__(self, group_name):
        """
        Constructor.

        Inputs:
        group_name: the name of the move_group.
            For Sawyer, this would be 'right_arm'
        """

        # If the node is shutdown, call this function    
        rospy.on_shutdown(self.shutdown)

        # Initialize moveit_commander
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the robot
        self._robot = moveit_commander.RobotCommander()

        # Initialize the planning scene
        self._scene = moveit_commander.PlanningSceneInterface()

        # This publishes updates to the planning scene
        self._planning_scene_publisher = rospy.Publisher('/collision_object', CollisionObject, queue_size=10)

        # Instantiate a move group
        self._group = moveit_commander.MoveGroupCommander(group_name)

        # Set the maximum time MoveIt will try to plan before giving up
        self._group.set_planning_time(10)

        # Set the bounds of the workspace
        self._group.set_workspace([-2, -2, -2, 2, 2, 2])

        # tf buffer
        self._tfb = tf2_ros.Buffer()

        # tf listener
        self._tfl = tf2_ros.TransformListener(self._tfb)

        # params
        self._group.set_max_velocity_scaling_factor(MAX_SPEED)

        self._current = PoseStamped()
        self._current.header.frame_id = "base"
        self._stitch_spacing = 0.03175
        # self._stitch_spacing = 0.05
        self.right_gripper = robot_gripper.Gripper("right_gripper")
        self.i = 0

        self._phantom = 0.1524
        self._table = 0.727964
        self._depth = 0.04
        self._radius = 0.5
        self._cdistance = 0.5
        self._direction = 1
        self._base = 0.9144
        self._speed = MAX_SPEED
        self._on_radius = True
        self._kp = MODIFICATION_SCALE * math.pow(self._speed, MODIFICATION_SPEED_POWER)
        self._gripper_y = 0.01905
        self._half_needle_len = 0.115
        
        self.string_length = 0.25

        self.X_AXIS = Vector3(1,0,0)
        self.Y_AXIS = Vector3(0,1,0)
        self.Z_AXIS = Vector3(0,0,1)

        self._tfb = tf2_ros.Buffer()
        self._tfl = tf2_ros.TransformListener(self._tfb)

        rospy.Subscriber('wound_info', wound, self.callback)
        rospy.Subscriber('robot/limb/right/endpoint_state', EndpointState, self.force_callback)

        self.force_values = []

        self.wound_x = None
        self.wound_y = None
        self.wound_length = None
        self.wound_width = None
        
        # Sleep for a bit to ensure that all inititialization has finished
        rospy.sleep(0.5)

    #####

    def first_drive(self):
        """
        Circle trajectory.
        """

        delta = self._half_needle_len - self._gripper_y - 0.025

        while not rospy.is_shutdown():
            try:
                result = PoseStamped()
                result.header.frame_id = "base"

                # log gripper x-force
                # print("Gripper force: " + str(self.right_gripper.get_force()))
                
                #result.pose.orientation = Quaternion(np.sqrt(2)/2, np.sqrt(2)/2, 0, 0)
                result.pose.orientation = Quaternion(0.5,0.5,0.5,0.5)
                p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
                result.pose.position = Point(p.translation.x, p.translation.y + delta, p.translation.z )

                plan = self.plan_to_pose(result, [])
                return plan

            except Exception as e:
                print e

        return result


    def drive_readjust(self):
        delta = -self._half_needle_len

        while not rospy.is_shutdown():
            try:
                result = PoseStamped()
                result.header.frame_id = "base"

                # log gripper x-force
                # print("Gripper force: " + str(self.right_gripper.get_force()))
                
                #result.pose.orientation = Quaternion(np.sqrt(2)/2, np.sqrt(2)/2, 0, 0)
                result.pose.orientation = Quaternion(0.5,0.5,0.5,0.5)
                p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
                result.pose.position = Point(p.translation.x, p.translation.y + delta, p.translation.z )

                plan = self.plan_to_pose(result, [])
                return plan

            except Exception as e:
                print e

        return result

    def second_drive(self):

        delta =   self._half_needle_len

        while not rospy.is_shutdown():
            try:
                result = PoseStamped()
                result.header.frame_id = "base"

                # log gripper x-force
                # print("Gripper force: " + str(self.right_gripper.get_force()))
                
                #result.pose.orientation = Quaternion(np.sqrt(2)/2, np.sqrt(2)/2, 0, 0)
                result.pose.orientation = Quaternion(0.5,0.5,0.5,0.5)
                p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
                result.pose.position = Point(p.translation.x, p.translation.y + delta, p.translation.z )

                plan = self.plan_to_pose(result, [])
                return plan

            except Exception as e:
                print e

        return result

        
    def auto_circle(self):
        """
        Circle trajectory generation.
        """
        p = self._current.pose.position
        currv = Vector3(p.x - self._center.x, p.y - self._center.y, p.z - self._center.z)
        currv.x = 0
        currv = currv.normalized()*self._radius

        angle = math.min(2*degrees(asin(self._speed/(2*self._radius))), np.pi()/8)

        nxt = curr.rotate(X_AXIS, angle*self._direction)
        delta = nxt - curr

        if (delta.length() > self._speed):
            delta = delta.normalized()*self._speed

        delta.x = 0
        return delta
        
    def tune_radius_motion(self):
        """
        Return vector 
        """
        p = self._current.pose.position
        currv = Vector3(p.x - self._center.x, p.y - self._center.y, p.z - self._center.z)
        currv.x = 0
        currv = currv.normalized()*self._radius

        if (self._cdistance > self._radius + POS_THRESHOLD):
            delta = currv.normalized()

            if (self._cdistance - self._radius < self._speed):
                delta = - (self._cdistance - self._radius) * delta
            else:
                delta = - self._speed * delta

        elif (self._cdistance < abs(self._radius - POS_THRESHOLD)):
            delta = currv.normalized()

            if (self._radius - self._cdistance < self._speed):
                delta = (-self._cdistance + self._radius) * delta
            else:
                delta = self._speed * delta

        return delta


    def set_center(self, center):
        """
        Stores current center for a circular trajectory.
        """
        self._center = Point(center)
        self._cdistance = utils.dist_helper(self._center, self._current.pose.position)
        # check_path_state()
        return True

    def set_current(self, pos, ori):
        """
        Stores current position and updates distances.

        Inputs:
        pos - translation
        ori - rotation
        """
        self._current.pose.position = Point(pos.x, pos.y, pos.z)
        self._current.pose.orientation = Quaternion(q.x, q.y, q.z, q.w)
        self._cdistance = utils.dist_helper(self._center, self._current.pose.position)
        # check_path_state()
        return True

    def check_path_state(self):
        """
        Checks if on circle radius.
        """

        self._on_circle = True

        if (abs(self._cdistance - self._radius) > POS_THRESHOLD) or (self._cdistance == 0):
            self._on_circle = False

    def lookup(self, t, s):
            done = False
            while not done:
                try:
                    trans = self._tfb.lookup_transform(t, s, rospy.Time())
                    done = True
                except Exception as e:
                    print e
                    traceback.print_exc()

            return trans

    def shutdown(self):
        """
        Code to run on shutdown. This is good practice for safety

        Currently deletes the object's MoveGroup, so that further commands will do nothing
        """
        self._group = None
        rospy.loginfo("Stopping Path Planner")

    def plan_to_pose(self, target, orientation_constraints):
        """
        Generates a plan given an end effector pose subject to orientation constraints

        Inputs:
        target: A geometry_msgs/PoseStamped message containing the end effector pose goal
        orientation_constraints: A list of moveit_msgs/OrientationConstraint messages

        Outputs:
        path: A moveit_msgs/RobotTrajectory path
        """

        self._group.set_pose_target(target)
        self._group.set_start_state_to_current_state()

        constraints = Constraints()
        constraints.orientation_constraints = orientation_constraints
        self._group.set_path_constraints(constraints)

        plan = self._group.plan()

        return plan

    def execute_plan(self, plan):
        """
        Uses the robot's built-in controllers to execute a plan

        Inputs:
        plan: a moveit_msgs/RobotTrajectory plan
        """

        print("executing")
        return self._group.execute(plan, True)


    def add_box_obstacle(self, size, name, pose):
        """
        Adds a rectangular prism obstacle to the planning scene

        Inputs:
        size: 3x' ndarray; (x, y, z) size of the box (in the box's body frame)
        name: unique name of the obstacle (used for adding and removing)
        pose: geometry_msgs/PoseStamped object for the CoM of the box in relation to some frame
        """    

        # Create a CollisionObject, which will be added to the planning scene
        co = CollisionObject()
        co.operation = CollisionObject.ADD
        co.id = name
        co.header = pose.header

        # Create a box primitive, which will be inside the CollisionObject
        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box.dimensions = size

        # Fill the collision object with primitive(s)
        co.primitives = [box]
        co.primitive_poses = [pose.pose]

        # Publish the object
        self._planning_scene_publisher.publish(co)

    def remove_obstacle(self, name):
        """
        Removes an obstacle from the planning scene

        Inputs:
        name: unique name of the obstacle
        """

        co = CollisionObject()
        co.operation = CollisionObject.REMOVE
        co.id = name

        self._planning_scene_publisher.publish(co)

    def add_obstacles(self):
        """
        Uses CV to add tissue phantom and table to planning scene.
        Table height and phantom height are known.
        """

        x = self.wound_x
        y = self.wound_y
        l = self.wound_length    

        dist = 0.6096  ## Assuming table is 2 ft away
        px, py = 0.3048, 0.0254 ## Foam dimensions

        ppose = PoseStamped()
        ppose.header.frame_id = "base"
        ppose.pose.position = Point(x, y, 0.05 + self._table - self._base)
        ppose.pose.orientation = Quaternion(0, 0, 0, 1)
        self.add_box_obstacle(np.array([px, py, 0.10]), "phantom", ppose)

        table_thickness = .03175 
        table_x, table_y = 2.0, 2.0 ## Assuming table is 2ft by 1m
        tpose = PoseStamped()
        tpose.header.frame_id = "base"
        tpose.pose.position = Point(0, 0, (self._table - self._base - (table_thickness)) )
        tpose.pose.orientation = Quaternion(0, 0, 0, 1)
        self.add_box_obstacle(np.array([table_x, table_y, table_thickness ]), "table", tpose)
        # self.add_box_obstacle(np.array([tx, ty, (self._table - self._base)]), "table", tpose)

        # back wall obstacle
        wall_x, wall_z = 1.5, 1.5
        wallpose = PoseStamped()
        #wallpose.header.frame_id = "base"
        wallpose.header.frame_id = self._group.get_planning_frame()
        wallpose.pose.position = Point(-0.2, 0, 0)
        wallpose.pose.orientation = Quaternion(0, 0, 0, 1)
        self.add_box_obstacle(np.array([0.01, wall_x, wall_z]), "wall", wallpose)


    def reset(self):
        """
        Return path for moving to reset position.

        Inputs:
        i: current throw iteration
        """
        ##FIXME: add orientation constraints for later resets

        # self._reset.pose.position.x = self._reset.pose.position.x + self._spacing*i

        # return self.plan_to_pose(self._reset, []) 
        joints = ['head_pan', 'right_j0', 'right_j1', 'right_j2', 'right_j3', 'right_j4', 'right_j5', 'right_j6', 'torso_t0']
        # thetas_ada = [-0.0247041015625, 0.7778916015625, -0.6519423828125, -0.538892578125, 1.748021484375, 0.5010029296875, -0.9936611328125, -4.4142919921875, 0.0]
        thetas = [-0.018255859375, 0.0043916015625, -0.755185546875, -0.2147705078125, 1.83649609375, -0.046044921875, -1.2278271484375, -4.12143359375, 0.0]
        # thetas = [0,0,0,0,0,0,0,0,0]

        map_dict = {joints[0]: thetas[0], joints[1]: thetas[1], joints[2]: thetas[2], joints[3]: thetas[3], joints[4]: thetas[4], joints[5]: thetas[5], joints[6]: thetas[6], joints[7]: thetas[7], joints[8]: thetas[8]}
        limb = Limb('right')
        # rate = rospy.Rate(20)
        limb.set_joint_positions(map_dict)
        print('attempted reset')


    def first_approach(self):
        p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
        waypoints = []

        wp = Pose()

        # original waypoint
        wp.orientation = p.rotation
        wp.position = p.translation
        waypoints.append(deepcopy(wp))


        # pull out
        #wp.position.x -= 0.2286
        wp.position.y -= 0.25
        waypoints.append(deepcopy(wp))

        # shift up
       

        rospy.sleep(0.5)
        #self._gripper.close()
        rospy.sleep(0.5)

        frac = 0.0
        maxtries = 100
        attempts = 0

        while frac < 1.0 and attempts < maxtries:
            (plan_wp, frac) = self._group.compute_cartesian_path(waypoints, 0.01, 0.0)

            attempts += 1

        # return once we have a complete plan
        if frac == 1.0:
            return plan_wp

        else:
            print("FAILED FIRST REGRASP")
            return None


    def compute_approach(self, i):
        """
        Return pose for suture approach.

        Inputs:
        i: current suture iteration
        arc: estimated arc length from CV
        """
     

        #Use CV for gripper dimensions? 
        #needle sticking out 

        p = self._entry[i]
        p[1] -= self._half_needle_len 

        while not rospy.is_shutdown():
            try:
                a = PoseStamped()
                a.header.frame_id = "base"
                a.pose.position = Point(p[0], p[1], p[2])
                a.pose.orientation = Quaternion(0.5,0.5,0.5,0.5)

                plan = self.plan_to_pose(a, [])
                return plan

            except Exception as e:
                print e

    def compute_null(self):
        """
        Generates a stationary command.
        """

        tf_incr = tf.Transform()
        self._delta.setValue(0, 0, 0)
        tf_incr.setOrigin(self._delta)
        tf_incr.setRotation(Quaternion(0, 0, 0, 1))

        return tf_incr

    def force_callback(self, message):
        self.force_values.append(message.wrench.force.x)


    def callback(self, message):
        self.wound_x = message.x
        self.wound_y = message.y
        self.wound_length = message.length
        self.wound_width = message.width
        # print(message)


    def generate_points(self):
        """
        Uses CV to generate splines along midpoint, upper, and lower bounds
        of tissue phantom (ignoring depth) and calculate entry and exits points
        along the boundaries s.t.
        """

        px = 0.3048 
        py = 0.0254 ## Foam dimensions
        x = self.wound_x
        y = self.wound_y
        l = self.wound_length

        # print(x, y, l)

        n = int(l // self._stitch_spacing)
        z = self._table - self._base +.09 # spacing for clay phantom

        self._entry, self._exit = np.ndarray((n, 3)), np.ndarray((n, 3))
        xl_point =  x- (l/2)
        yl_point = (y - py/2)
        yu_point = (y + py/2)

        for i in range(0, n):
            self._entry[i] = np.array([xl_point + i * self._stitch_spacing, yl_point, z])
            self._exit[i] = np.array([xl_point + i * self._stitch_spacing, yu_point, z])


    def compute_first_straight_regrasp(self):
        """
        Add proper obstacles to scene and return  path.
        """
        ## FIXME
        py = 0.0254
        p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
        waypoints = []

        wp = Pose()

        # original waypoint
        wp.orientation = p.rotation
        wp.position = p.translation
        waypoints.append(deepcopy(wp))

        # pull out enough to clear phantom
        wp.position.x -= 0.05
        waypoints.append(deepcopy(wp))

        # shift up
        wp.position.z += 0.1
        waypoints.append(deepcopy(wp))

        # shift by +y (over foam)
        wp.position.y += py + (4.5 * self._gripper_y)# + self._half_needle_len 
        waypoints.append(deepcopy(wp))

        # shift up
        wp.position.z -= 0.1
        waypoints.append(deepcopy(wp))

         # push back in
        wp.position.x += 0.05
        waypoints.append(deepcopy(wp))

        rospy.sleep(0.5)
        rospy.sleep(0.5)

        frac = 0.0
        maxtries = 100
        attempts = 0

        while frac < 1.0 and attempts < maxtries:
            (plan_wp, frac) = self._group.compute_cartesian_path(waypoints, 0.01, 0.0)

            attempts += 1

        # return once we have a complete plan
        if frac == 1.0:
            return plan_wp

        else:
            print("FAILED FIRST REGRASP")
            return None

    def compute_second_straight_regrasp_a(self):
        """
        Add proper obstacles to scene and return path.
        """

        py = 0.0254
        p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
        waypoints = []

        wp = Pose()

        # original waypoint
        wp.orientation = p.rotation
        wp.position = p.translation
        waypoints.append(deepcopy(wp))

        # shift +y
        wp.position.y += (.5) * self._half_needle_len
        waypoints.append(deepcopy(wp))

        rospy.sleep(1.0)

        frac = 0.0
        maxtries = 100
        attempts = 0

        while frac < 1.0 and attempts < maxtries:
            (plan_wp, frac) = self._group.compute_cartesian_path(waypoints, 0.01, 0.0)

            attempts += 1

        # return once we have a complete plan
        if frac == 1.0:
            return plan_wp

        else:
            print("FAILED 2nd REGRASP A")
            return None

    def compute_second_straight_regrasp_b(self):
        """
        Add proper obstacles to scene and return  path.
        """
        
        py = 0.0254
        p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
        waypoints = []

        wp = Pose()

        # original waypoint
        wp.orientation = p.rotation
        wp.position = p.translation
        waypoints.append(deepcopy(wp))

        wp.position.y -= .5 * self._half_needle_len
        waypoints.append(deepcopy(wp))

        # shift -y
        rospy.sleep(1.0)

        frac = 0.0
        maxtries = 100
        attempts = 0

        while frac < 1.0 and attempts < maxtries:
            (plan_wp, frac) = self._group.compute_cartesian_path(waypoints, 0.01, 0.0)

            attempts += 1

        # return once we have a complete plan
        if frac == 1.0:
            return plan_wp

        else:
            print("FAIiLED 2nd REGRASP B")
            return None

    def compute_second_straight_trajectory(self, final_stitch):
        """
        Straight trajectory back to next entry point
        """

        p = self._tfb.lookup_transform("base", "right_gripper_tip", rospy.Time()).transform
        waypoints = []

        wp = Pose()

        # original waypoint
        wp.orientation = p.rotation
        wp.position = p.translation
        waypoints.append(deepcopy(wp))
        # self._group.set_max_velocity_scaling_factor(0.05)

        # pull needle out (+ y)
        wp.position.y += self.string_length + self._half_needle_len
        waypoints.append(deepcopy(wp))
        print(self.string_length)

        # if final stitch, want to pull string out and be done
        if not final_stitch:
            wp.position.y -= (self.string_length + self._half_needle_len)
            wp.position.z += self.string_length 
            waypoints.append(deepcopy(wp))

            wp.position.y -= self.string_length + self._half_needle_len
            wp.position.z -= self.string_length 
            waypoints.append(deepcopy(wp))

        else:
            rospy.sleep(2.5)
            print("Final stitch. Pulling out string.")
        
        frac = 0.0
        maxtries = 500
        attempts = 0

        # self._group.set_max_velocity_scaling_factor(0.05)
        while frac < 1.0 and attempts < maxtries:
            (plan_wp, frac) = self._group.compute_cartesian_path(waypoints, 0.01, 0.0)

            attempts += 1

        # return once we have a complete plan
        if frac == 1.0:
            return plan_wp

        else:
            print("FAILED 2nd TRAJECTORY")
            return None
