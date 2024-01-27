#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist #rosun kendi kutuphanesi

def haraket():
    rospy.init_node("duz_git")
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz_mesaji = Twist()#twist tipinde hiz mesaji yayinlayacaz
    hiz_mesaji.linear.x = -0.5
    mesafe = 20
    yer_degistirme = 0
    t0 = rospy.Time.now().to_sec()
    while yer_degistirme < mesafe:
        pub.publish(hiz_mesaji)
        rate=rospy.Rate(1) #saniyede 1 kez olacak sekilde 1 hertz yani
        t1 = rospy.Time.now().to_sec()
        yer_degistirme = hiz_mesaji.linear.x * (t1-t0)
        rospy.loginfo("Yer Degistirme:"+str(yer_degistirme))
        rate.sleep()#rate kadar uyu dedik ve saniyede 1 kere data basiyo
    hiz_mesaji.linear.x = 0.0
    pub.publish(hiz_mesaji)
    rospy.loginfo("Hedefe Varildi")
    
try:      
    haraket()        
except rospy.ROSInterruptException:
    rospy.loginfo("Calisma Sonlandirildi")