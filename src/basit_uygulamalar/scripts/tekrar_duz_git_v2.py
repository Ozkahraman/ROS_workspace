#!/usr/bin/env python3

#3. bir terminalden alttaki satirla mesaj yayinlaman gerekiyor hedef konum bilgisi
#rostopic pub /mesafe basit_uygulamalar/mesafe "mesafe: 5" 


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from basit_uygulamalar.msg import mesafe

class HedefeGit():
    def __init__(self) :
        rospy.init_node("duz_gitme")
        
        self.hedef_konum = 0
        self.guncel_konum = 0
        self.flag = True
        
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        rospy.Subscriber("mesafe",mesafe,self.mesafeCallback)
        pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        hiz_mesaji = Twist()
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.flag:
                hiz_mesaji.linear.x = 0.5
                pub.publish(hiz_mesaji)
                rospy.loginfo("Guncel Konum = "+str(self.guncel_konum))
                rate.sleep()
            else:
                hiz_mesaji.linear.x = 0.0
                pub.publish(hiz_mesaji)
                rospy.loginfo("Hedefe varildi")
                rate.sleep()
        
    def odomCallback(self, mesaj):
           self.guncel_konum = mesaj.pose.pose.position.x
           if self.guncel_konum <= self.hedef_konum:
               self.flag = True
           else:
               self.flag = False
               
    def mesafeCallback(self, mesaj):
        self.hedef_konum = mesaj.mesafe
    
    
try:
    HedefeGit()
    
except rospy.ROSInterruptException:
    print("Dugumu Sonlandirdiniz")