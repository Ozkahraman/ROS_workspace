#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3. bir terminalden alttaki satirla mesaj yayinlaman gerekiyor hedef konum bilgisi
#rostopic pub /mesafe_git basit_uygulamalar/mesafe "mesafe: 5" 

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry #aracin guncel konumunu yayinlayan bir kutuphane
from basit_uygulamalar.msg import mesafe

class HedefeGit():
    def __init__(self):
        rospy.init_node("duz_git")
        
        self.hedef_konum = 0.0
        self.guncel_konum = 0.0
        self.kontrol = True
        
        rospy.Subscriber("odom",Odometry,self.odomCallback) #odom yayın aracının yaydıgı Odometry Türünden datayla aracın guncel konumunu aldık 
        rospy.Subscriber("mesafe_git",mesafe,self.mesafeCallback)
        pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)#ve o guncel konumu cmd_vel uzerinden Twist turunde datayla yayın yaptık
        hiz_mesaji = Twist()
        rate=rospy.Rate(10)     #10 hertz saniyede 10 kere
        while not rospy.is_shutdown():
            if self.kontrol:#guncel konum hedeften azsa
                hiz_mesaji.linear.x = 0.5
                pub.publish(hiz_mesaji)
                rospy.loginfo("Guncel Konum:"+str(self.guncel_konum))
                rate.sleep()

            else:
                hiz_mesaji.linear.x = 0.0
                pub.publish(hiz_mesaji)
                rospy.loginfo("Hedefe Varildi")
                rate.sleep()   
        
    def odomCallback(self,mesaj):
        self.guncel_konum = mesaj.pose.pose.position.x #odometry kutuphanesinin yaydigi x eksenindeki konumu
        if self.guncel_konum <= self.hedef_konum:
            self.kontrol = True
        else:
            self.kontrol = False
    
    def mesafeCallback(self,mesaj):
        self.hedef_konum = mesaj.mesafe        
try:  
    HedefeGit()       
except rospy.ROSInterruptException:
    print("Dugum Sonlandi")