#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import imod
import rospy
from geometry_msgs.msg import Twist
from basit_uygulamalar.srv import CemberHaraket
from nav_msgs.msg import Odometry

#surekli data basmak servise aykırı servise bir istek gelir ve bir cevap verir

# class cemberCiz():
    
#     def __init__(self):
#         self.guncel_konumx = 0.0
#         self.guncel_konumy = 0.0
#     def odomCallback(self,mesaj):
#         self.guncel_konumx = mesaj.pose.pose.position.x

#     def cemberFonksiyonu(self,istek):
#         hiz_mesaji = Twist()
#         lineer_hiz = 0.5
#         hiz_mesaji.linear.x = lineer_hiz
#         yaricap = istek.yaricap
#         hiz_mesaji.angular.z = lineer_hiz / yaricap #acisal olarak z eksenine W omegayı atadık
#         while not rospy.is_shutdown():
#             self.pub.publish(hiz_mesaji)
#             rospy.loginfo("Aracin x,y koordinatlari"+str(self.guncel_konumx)+str(self.guncel_konumy))
        
        
#     rospy.init_node("cembersel_haraket")
#     pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
#     rospy.Service("cember_servis",CemberHaraket,cemberFonksiyonu)#cember_servis adında server olusturduk CemberHaraket türünde veri gelecek cemberFonksiyonunu calistiracak
#     rospy.Subscriber("odom",Odometry,odomCallback)
#     rospy.spin()# spin() simply keeps python from exiting until this node is stopped


def cemberFonksiyonu(istek):
        hiz_mesaji = Twist()
        lineer_hiz = 0.5
        hiz_mesaji.linear.x = lineer_hiz
        yaricap = istek.yaricap
        hiz_mesaji.angular.z = lineer_hiz / yaricap #acisal olarak z eksenine W omegayı atadık
        while not rospy.is_shutdown():
            pub.publish(hiz_mesaji)
            
            
            
rospy.init_node("cembersel_haraket")
pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
rospy.Service("cember_servis",CemberHaraket,cemberFonksiyonu)#cember_servis adında server olusturduk CemberHaraket türünde veri gelecek cemberFonksiyonunu calistiracak
rospy.spin()# spin() simply keeps python from exiting until this node is stopped