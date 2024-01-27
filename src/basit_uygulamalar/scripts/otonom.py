#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan #lidar verisini kullanabilmek icin
from geometry_msgs.msg import Twist

class lidarVerisi():
    def __init__(self):
        rospy.init_node("lidar_verisi",anonymous=True)
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz = Twist()
        rospy.Subscriber("scan",LaserScan,self.anlamlandir)
        rospy.spin()
    
    def anlamlandir(self,veri):
        self.sag_on = min(list(veri.ranges[340:359]))
        self.sag = min(list(veri.ranges[255:285]))
        self.sol_on = min(list(veri.ranges[0:20]))
        self.on = self.sol_on + self.sag_on
        self.sol = min(list(veri.ranges[75:105]) )
        
        print(self.sag_on,self.sag,self.sol_on,self.sol,self.on)
        # if self.on > 0.7:
        #      self.hiz_mesaji = 0.6

        #      if self.sag_on <1.5:
                
        #          self.hiz_mesaji = 0.6
        #          self.donus = 0.6    #sola donduruyo
            
        #      elif self.sol_on <1.5:
               
        #          self.hiz_mesaji = 0.6
        #          self.donus = -0.6   #sağa donduruyo
                
            
        #      else:
        #          self.hiz_mesaji = 0.6
        #          self.donus = 0.0      
            
        # else:
        #      self.hiz_mesaji = 0.0


        if self.on > 1:
            self.hiz_mesaji = 0.4

            if self.sag - self.sol > 1.0:
               self.hiz_mesaji = 0.4 
               self.donus = -0.8
               
            elif self.sol - self.sag > 1.0:
                self.hiz_mesaji =0.4 
                self.donus = 0.8
            
            else:
                self.hiz_mesaji = 0.4 
                self.donus = 0.0
        
        else:
            self.hiz_mesaji=0.0
            self.donus = 0.0 
        
        
        # if self.on > 1.0:
        #     self.hiz_mesaji = 1.0
        #     self.donus = 0.0
            
        #     if self.sag - self.sol > 0.5:
        #         while not self.sag == self.sol:
        #             self.hiz_mesaji = 1.0 
        #             self.donus = -1.0
            
        #     elif self.sol - self.sag > 0.5:
        #         while not self.sag == self.sol:
        #             self.hiz_mesaji = 1.0  
        #             self.donus = 1.0

        #     else:
        #         self.hiz_mesaji = 1.0  
        #         self.donus = 0.0
        
        # else:
        #     self.hiz_mesaji = 0.0
        #     self.donus = 0.0 
            
        self.hiz.linear.x = self.hiz_mesaji
        self.hiz.angular.z = self.donus
        self.pub.publish(self.hiz)
        rospy.Rate(10)

otonomom = lidarVerisi()        