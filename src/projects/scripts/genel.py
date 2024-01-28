#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan#  360 Samples on taraf veri.ranges[0] dan baslar 0 derece sol taraf 90 derece don arka taraf 180 derece sag taraf 270 
import sys

class Cember():
    def __init__(self):
        rospy.init_node("cember_node")
        rospy.Subscriber("odom", Odometry, self.odomCallback)
        rospy.Subscriber("scan", LaserScan, self.lidarCallback)
        pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        
        self.hiz = Twist()
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.hiz.linear.x = 0.0
            self.hiz.angular.z = 0.0
            #rospy.loginfo("Hiz:0.5")
            pub.publish(self.hiz)
            self.rate.sleep()
        
    def odomCallback(self, msg):
        self.guncel_konumx = msg.pose.pose.position.x
        self.guncel_konumy = msg.pose.pose.position.y
        #rospy.loginfo("Guncel Konumx:"+str(self.guncel_konumx))
        #rospy.loginfo("Guncel Konumy:"+str(self.guncel_konumy))
        self.rate.sleep()
        
    def lidarCallback(self, veri):
        print(veri)
        #Kendi Deneysel Gozlemlerim Araciligiyla Tespit Edilmistir 90 derece sola dogru farklar arasindaki orandan gidilmistir
        self.on = veri.ranges[0]
        self.sol_on = veri.ranges[20]
        self.sag_on = veri.ranges[330]
        self.sol = veri.ranges[91]
        self.arka = veri.ranges[182]
        self.sag = veri.ranges[275]
        print(f"on uzaklik :{self.on}, sol_on uzaklikk:{self.sol_on}, sag_on uzaklik {self.sag_on} sol uzaklik {self.sol}, arka uzaklik: {self.arka} , sag uazklik: {self.sag}")
        self.rate.sleep()
        



try:  
    Cember()       
except rospy.ROSInterruptException:
    print("Dugum Sonlandi")