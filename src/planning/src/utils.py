#!/usr/bin/env python
"""
Path Planner utils
"""
import sys
import rospy
import moveit_commander
import scipy
import numpy as np
from scipy.interpolate import UnivariateSpline
from moveit_msgs.msg import OrientationConstraint, Constraints, CollisionObject
from geometry_msgs.msg import PoseStamped
from shape_msgs.msg import SolidPrimitive

# _spacing doesnt exist here
stitch_spacing = .04

def points(tan, i, z, xl, xm, xu, lspline, mspline, uspline):
    for j in xl:
            for k in xu:
                v = np.array([k - j, uspline(k) - lspline(j)])
                #p1 = np.array([j, lspline(j)])
                #p2 = np.array([xm[0] + i*stitch_spacing, mspline(xm[0] + i*stitch_spacing)])
                if np.dot(tan, v) == 0:
                    return (np.array([[j, lspline(j), z]]), np.array([[k, uspline(k), z]]))

def passes(v, p1, p2):
    tol = 1e-2
    xl = np.linspace(p1[0], v[0] + p1[0], 100)
    yl = np.linspace(p1[1], v[1] + p1[1], 100)
    for (i, j) in zip(xl, yl):
        if abs(i-p2[0]) <= tol and abs(j+p2[1]) <= tol:
            return True
        else:
            return False

def dist_helper(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dz = p1.z - p2.z

    return sqrt(dw**2 + dy**2 + dz**2)            