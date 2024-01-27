#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class RobotKamera():
    def __init__(self):
        rospy.init_node("kamera")
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.bridge = CvBridge()
        rospy.spin()
        
    def kameraCallback(self,veri):
        self.foto = self.bridge.imgmsg_to_cv2(veri,"bgr8")#foto degiskenine bridge in o fonksiyonla bgr8 turune cevirilmisini atadık
        cv2.imshow("Robot Kamerasi",self.foto) 
        cv2.waitKey(1)

nesen = RobotKamera()   