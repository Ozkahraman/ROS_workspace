#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Robotun on kismi 0 derceden baslar sola dogru 90 derce arta arta gider

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class lidarVerisi():
    def __init__(self):
        rospy.init_node("lidar_verisi")
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("scan",LaserScan,self.lidarCallback)
        rospy.spin()   
        
    def lidarCallback(self,veri):
        self.sol_on = list(veri.ranges[0:9])       #0-9 derece tariyo
        self.sag_on = list(veri.ranges[350:359])   
        self.on_kisim = self.sol_on + self.sag_on
        self.sol = list(veri.ranges[80:100])       #80-100 derece arasi tariyo yani aslinda 90 dercelik kisim olan sol tarafini tariyo
        self.sag = list(veri.ranges[260:280])
        self.arka = list(veri.ranges[170:190])
        self.min_on = min(self.on_kisim)
        self.min_sol = min(self.sol)
        self.min_sag = min(self.sag)
        self.min_arka = min(self.arka)
        print(self.min_on, self.min_sol, self.min_sag, self.min_arka)
        
        if self.min_on < 1.0:
            self.hiz_mesaji.linear.x = 0.0
            self.hiz_mesaji.linear.y = 0.25
            self.hiz_mesaji.linear.z = 0.25
            self.hiz_mesaji.angular.y = 0.25
            self.pub.publish(self.hiz_mesaji)
        else:
            self.hiz_mesaji.linear.x = 0.25
            self.hiz_mesaji.linear.y = 0.0
            self.hiz_mesaji.linear.z = 0.0
            self.pub.publish(self.hiz_mesaji)
        
lidarVerisi()