#!/usr/bin/env python

# Performs wound segmentation.
# Publishes a wound message containing the (x, y) position of the wound in world 
# coordinates, as well as the length and width computed.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

from scipy import ndimage
from scipy.misc import imresize
from skimage import filters
from sklearn.cluster import KMeans

from skimage.measure import block_reduce
import time
import pdb

import tf2_ros
import time

import rospy
from sensor_msgs.msg import Image
from segmentation.msg import wound
from cv_bridge import CvBridge, CvBridgeError

this_file = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = '/'.join(this_file.split('/')[:-2]) + '/img'

bridge = CvBridge()
img_name = 'wrist_shot1.png'

tfb = tf2_ros.Buffer()
tfl = tf2_ros.TransformListener(tfb)

# camera is 'zoomed out' at this starting position. 
# from here, we use computer vision to localize the wound 
# and determine where the spline is.

trans = tfb.lookup_transform("base", "right_hand_camera", rospy.Time()).translation
x_init, y_init, z_init = trans.x, trans.y, trans.z

def read_image(img_name, grayscale=False):
    if not grayscale:
        img = cv2.imread(img_name)
    else:
        img = cv2.imread(img_name, 0)

    return img

def write_image(img, img_name):
    cv2.imwrite(img_name, img)

def show_image(img_name, title='Fig', grayscale=False):
    if not grayscale:
        plt.imshow(img_name)
        plt.title(title)
        plt.show()
    else:
        plt.imshow(img_name, cmap='gray')
        plt.title(title)
        plt.show()


def threshold_segment_naive(gray_img, lower_thresh, upper_thresh):
    copy = gray_img
    copy = cv2.medianBlur(copy, 5)

    ret, edged = cv2.threshold(copy, 40, 60, cv2.THRESH_BINARY)
    _im2,contours,hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    #show_image(edged)

    # want to keep track of farthest bottom-right contour
    max_bottom_right = -1
    x_final, y_final, w_final, h_final = -1, -1, -1, -1

    for c in contours:
        # prevent noise
        if cv2.contourArea(c) <= 100 or cv2.contourArea(c) >= 200000:
            continue

        # create bounding rectangle pixels
        x,y,w,h = cv2.boundingRect(c)
        bottom_right = x + y + w + h
        if bottom_right > max_bottom_right:
            max_bottom_right = bottom_right
            x_final = x
            y_final = y
            w_final = w
            h_final = h

        # rule out peripheral contours
        if (x < 150 or x > 600 or y < 80 or y > 400):
            continue

    print(x_final + (w_final/2), y_final + (h_final/2))
    copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2RGB)
    cv2.rectangle(copy, (x_final, y_final), (x_final + w_final, y_final + h_final), color=(0, 0, 255), thickness=3)
    resized = cv2.resize(copy, (1600, 900))
    cv2.imshow("Show", resized)
    cv2.waitKey(100)

    return edged, x, y, w, h


def to_grayscale(rgb_img):
    return np.dot(rgb_img[... , :3] , [0.299 , 0.587, 0.114])

def test_thresh_naive(img, lower_thresh, upper_thresh):
    thresh, x, y, w, h = threshold_segment_naive(img, lower_thresh, upper_thresh)
    # show_image(thresh, title='thresh naive')
    cv2.imwrite(IMG_DIR + "/thresh.jpg", thresh)

    return compute_spline(x, y, w, h)
    

def compute_spline(x, y, w, h):
    img_height = 480

    #pixel_to_meter = 0.0004401
    pixel_to_meter = 0.000491
    # print("w: " + str(w))
    #print("h: " + str(h))

    # center of wound, in pixels
    center_x_coord = y + (h/2.0)
    center_y_coord = x + (w/2.0)

    x_offset_in_pixels = center_x_coord - (img_height / 2)
    y_offset_in_pixels = center_y_coord - (img_width / 2)

    # computed offset from homographies, with a single known 2D -> 3D mapping
    x = x_init - (x_offset_in_pixels * pixel_to_meter) - 0.0445
    y = y_init - (y_offset_in_pixels * pixel_to_meter) - 0.01795

    wound_length_meters = h * pixel_to_meter
    wound_width_meters = w * pixel_to_meter

    return (x, y, wound_length_meters, wound_width_meters)


def image_callback(msg):
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

    except CvBridgeError, e:
        print(e)
    else:
        # save image
        cv2.imwrite(IMG_DIR + '/' + "wrist_shot1.png", cv2_img)
        test_img = read_image(IMG_DIR + '/' + img_name, grayscale=True)
        # it will plot the image and also save it

        (x, y, wound_length_meters, wound_width_meters) = test_thresh_naive(test_img, 0, 10)
        # print(x, y, wound_length_meters, wound_width_meters)

        # here, want to publish the 4 unpacked values 
        pub = rospy.Publisher('wound_info', wound, queue_size=10)

        w = wound()
        w.x = x
        w.y = y
        w.length = wound_length_meters
        w.width = wound_width_meters
        pub.publish(w)

    # sub.unregister()

rospy.init_node('image_segmentation')
image_topic = '/io/internal_camera/right_hand_camera/image_raw'
sub = rospy.Subscriber(image_topic, Image, image_callback)

def main():
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.spin()
        r.sleep()

main()