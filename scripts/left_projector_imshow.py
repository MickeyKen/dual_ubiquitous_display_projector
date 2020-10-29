#!/usr/bin/env python
import cv2
import numpy as np
from std_msgs.msg import Bool
import rospy
import time
import sys
import math
import rospkg
import rosparam
r = rospkg.RosPack()
path = r.get_path('dual_ubiquitous_display_projector')


def shutdown():
    # cv2.destroyWindow('screen2')
    pass

if __name__ == '__main__':
    rospy.init_node('left_projector_imshow', anonymous=True)

    rospy.on_shutdown(shutdown)

    rospy.set_param('left_projector/switch', True)
    rospy.set_param("left_projector/file_name", "sample.png")

    while not rospy.is_shutdown():
        sw = rospy.get_param("left_projector/switch")

        if sw:
            file_name = rospy.get_param("left_projector/file_name")
            img = cv2.imread(path + '/Images/' + file_name)
            h = 1920
            w = 1080
            img = cv2.resize(img,(h,w))
            cv2.namedWindow('screen2', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('screen2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            # cv2.moveWindow('screen',1940,0)
            cv2.imshow('screen2', img)
            cv2.waitKey(1)
        else:
            black_img = np.zeros((768,1024,3),np.uint8)
            cv2.namedWindow('screen2', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('screen2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            # cv2.moveWindow('screen',1940,0)
            cv2.imshow('screen2', black_img)
            cv2.waitKey(1)
