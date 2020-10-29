#!/usr/bin/env python
import cv2
import numpy as np
from std_msgs.msg import Bool
import rospy
import time
import sys
import math
import rospkg
r = rospkg.RosPack()
path = r.get_path('dual_ubiquitous_display_projector')

def callback(msg):

    if msg.data:
        print "/projector2/switch True"
        img = cv2.imread(path + '/Images/sample.png')
        h = 1024
        w = 768
        img = cv2.resize(img,(h,w))
        cv2.namedWindow('screen2', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('screen2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow('screen2',1940,0)
        cv2.imshow('screen2', img)
        cv2.waitKey(0)
    else:
        print "/projector2/switch False"
        cv2.destroyWindow('screen2')


def projection():
    rospy.init_node('projection_node_2', anonymous=True)
    #rospy.set_param("exp_miki_img/switch", 1)
    rospy.Subscriber("projector2/switch", Bool, callback)
    rospy.spin()

if __name__ == '__main__':
    projection()
