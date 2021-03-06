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

images = ["png","jpg","jpeg"]
videos = ["mov","mp4"]

def shutdown():
    # cv2.destroyWindow('screen2')
    pass

if __name__ == '__main__':
    rospy.init_node('right_projector_imshow', anonymous=True)

    rospy.on_shutdown(shutdown)

    rospy.set_param('right_projector/switch', True)
    rospy.set_param("right_projector/file_name", "sample.png")

    while not rospy.is_shutdown():
        sw = rospy.get_param("right_projector/switch")

        if sw:
            file_name = rospy.get_param("right_projector/file_name")
            ext = file_name.split('.')[1]
            if ext in images:
                img = cv2.imread(path + '/Images/' + file_name)
                h = 1920
                w = 1080
                img = cv2.resize(img,(h,w))
                cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.moveWindow('screen',1940,0)
                cv2.imshow('screen', img)
                cv2.waitKey(1)
            elif ext in videos:
                cap = cv2.VideoCapture(path + '/Images/' + file_name)
                cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
                cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.moveWindow('screen',1940,0)
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    else:
                        last_frame = frame
                    cv2.imshow("screen", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cv2.imshow("screen", last_frame)
                cv2.waitKey(5000)
            else:
                pass
        else:
            black_img = np.zeros((768,1024,3),np.uint8)
            cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow('screen',1940,0)
            cv2.imshow('screen', black_img)
            cv2.waitKey(1)
