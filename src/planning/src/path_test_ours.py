#!/usr/bin/env python
"""
Adapted from EECS 106A lab 7 Path Planning Script by Valmik Prabhu
"""
# import sys
# assert sys.argv[1] in ("sawyer", "baxter")
# ROBOT = sys.argv[1]

# if ROBOT == "baxter":
#     from baxter_interface import Limb
# else:
#     from intera_interface import Limb


# from geometry_msgs.msg import PoseStamped, Point, Vector3, Quaternion, TransformStamped

# from intera_interface import gripper as robot_gripper

import csv
import matplotlib.pyplot as plt

import numpy as np
# import traceback
# import rospy

# from moveit_msgs.msg import OrientationConstraint

# from mts_planner3 import PathPlanner
# from controller import Controller

# rospy.init_node("planning")
# # right_gripper = robot_gripper.Gripper("right_gripper")
# # controller = Controller(Kp, Ki, Kd, Kw, Limb('right'))
# planner = PathPlanner("right_arm")
# limb = Limb('right')


# GRIPPER_POS = 0.005

def initialize_gripper():
    # right_gripper.MIN_POSITION = GRIPPER_POS

    print('Calibrating...')
    planner.right_gripper.calibrate()
    rospy.sleep(1.0)

    planner.right_gripper.open()
    rospy.sleep(3.0)

    planner.right_gripper.close()
    rospy.sleep(1.0)


def move_to_reset():
    print('Resetting...\n')
    # planner.reset()
    joints = limb.joint_names()
    # print(joints)

    # joints = [ 'right_j0', 'right_j1', 'right_j2', 'right_j3', 'right_j4', 'right_j5', 'right_j6']
    # thetas = [0.0122939453125, 0.16250390625, -0.4944921875, -0.24884375, 1.317568359375, 0.258123046875, -0.7834189453125, -4.0236328125, 0.0]
    # thetas = [0.16250390625, -0.4944921875, -0.24884375, 1.317568359375, 0.258123046875, -0.7834189453125, -4.0236328125]
    # thetas = [0,0,0,0,0,0,0,0,0]
    thetas = [0.0456904296875, -0.556919921875, -0.071533203125, 1.43940234375, 0.006359375, -0.7705859375, -2.9321025390625]

    map_dict = {joints[0]: thetas[0], joints[1]: thetas[1], joints[2]: thetas[2], joints[3]: thetas[3], joints[4]: thetas[4], joints[5]: thetas[5], joints[6]: thetas[6]}
        # rate = rospy.Rate(20)

    for i in range(10000):
        limb.set_joint_positions(map_dict)
        # print('attempted reset')


def main():
    #print("Gripper force: " + str(planner.right_gripper.get_force()))
    #print("Gripping?" + str(planner.right_gripper.is_gripping()))
    #planner.right_gripper.open()
    #rospy.sleep(5.0)
    initialize_gripper()
    rospy.sleep(4.0)
    move_to_reset()
    rospy.sleep(2.0)
    planner.add_obstacles()
    #rospy.sleep(1.0)

    planner.execute_plan(planner.first_approach())
    rospy.sleep(1.5)
    
    # segmentation happens herfe
    planner.generate_points() # self.entry, self.exit are created
    print(planner._entry)
    print(planner._exit)
    final_stitch = False

    for i in range(planner._entry.shape[0]):
        planner.right_gripper.close()
        # planner._group.set_max_velocity_scaling_factor(0.1)
        print("Attempting compute approach:")
        planner.execute_plan(planner.compute_approach(i))
        # rospy.sleep(1.0)
        # planner.remove_obstacle('phantom')
        rospy.sleep(1.5)
        #if i == 0:
            #print("Gripper force: " + str(planner.right_gripper.get_force()))
            #print("Gripping? " + str(planner.right_gripper.is_gripping()))

        #planner._group.set_max_velocity_scaling_factor(0.1)

        print("Attempting straight trajectory:")
        planner.force_values.append(-100)
        planner.execute_plan(planner.first_drive())
        rospy.sleep(1.0)

        planner.right_gripper.open()
        planner.force_values.append(-100)
        planner.execute_plan(planner.drive_readjust())
        rospy.sleep(1.0)
        planner.right_gripper.close()
        rospy.sleep(1.0)
        planner.force_values.append(-100)
        planner.execute_plan(planner.second_drive())
        
        rospy.sleep(1.0)


        planner.right_gripper.open()
        print("Attempting regrasp 1:")
        planner.force_values.append(-100)
        planner.execute_plan(planner.compute_first_straight_regrasp())
        rospy.sleep(1.0)
        planner.right_gripper.close()
        rospy.sleep(1.0)

        file = open('/home/cc/ee106a/fa19/class/ee106a-aft/ros_workspaces/lab7/src/planning/src/force_values_foam.csv', 'w')
        print('WRITING FILE')
        for val in planner.force_values:
            file.write(str(val))
            file.write('\n')

        file.close()
        break

        # right_gripper.open()
        print("Attempting regrasp 2a:")
        planner.execute_plan(planner.compute_second_straight_regrasp_a())
        rospy.sleep(2.0)
        planner.right_gripper.open()
        rospy.sleep(2.0)

        print("Attempting regrasp 2b:")
        planner.execute_plan(planner.compute_second_straight_regrasp_b())
        rospy.sleep(2.0)
        planner.right_gripper.close()
        rospy.sleep(2.0)

        # slow down
        print("Slowing down...")
        # planner._group.set_max_velocity_scaling_factor(0.1)

        #planner.right_gripper.close()
        print('Attempting 2nd trajectory:')

        # special case : last second_trajectory, controlled by final_stitch flag
        if (i == planner._entry.shape[0] - 1):
            final_stitch = True

        planner.execute_plan(planner.compute_second_straight_trajectory(final_stitch))
        rospy.sleep(2.0)
        planner.i += 1

    move_to_reset()


def plot_forces(filename):
    import seaborn as sns
    sns.set_style("darkgrid")

    x = []
    y = []
    #boundaries = [1804, 1978, 2267, 2456]
    boundaries = [2506, 2683, 2991, 3172]

    with open(filename, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter='\n')
        timestep = 0
        for row in plots:
            val = float(row[0])
            #print(val)
            x.append(timestep)
            if val > -50:
                y.append(val)
            else:
                y.append(0)
                #boundaries.append(timestep)

            timestep += 1



    print(boundaries)

    fig = plt.figure()
    plt.plot(x[1000:], y[1000:])
    for xc in boundaries:
        plt.axvline(x=xc, dashes=(2,2,1,2), color="red")

    ax = plt.gca()
    ax.set_xticks(boundaries)
    ax.set_xticklabels(["1st\n needle drive", "", "2nd\n needle drive", ""])

    fig.suptitle('End Effector force vs. time : Foam Phantom', fontsize=20)
    plt.xlabel('Timestep', fontsize=15)
    plt.ylabel('X-Force on End Effector (Newtons)', fontsize=15)
    plt.show()


if __name__ == '__main__':
    #main()
    #plot_forces('/home/cc/ee106a/fa19/class/ee106a-aft/ros_workspaces/lab7/src/planning/src/force_values_clay.csv')
    #plot_forces('/home/cc/ee106a/fa19/class/ee106a-aft/ros_workspaces/lab7/src/planning/src/force_values_foam.csv')
    plot_forces('/Users/shaantam/Documents/106a/src/planning/src/force_values_foam.csv')


