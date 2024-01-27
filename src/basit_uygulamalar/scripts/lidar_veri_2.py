#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
import time
def lidarVeri():
    rospy.init_node("lidar_verisi", anonymous=True)
    rospy.Subscriber("scan",LaserScan,anlamlandir)
    rospy.spin()
        
    
        

def anlamlandir(veri):
    adet =len(veri.ranges)
    print("bir taramada üretilen lidar verisi = "+str(adet))
    time.sleep(1)
    #720 TANE GELEN VERIYI 180 DERECE TARAYAN LIDAR SENSORU ICIN CEKIMLEDIK 5 PARCA ALAN VAR 720/5=144
#    sag_on = min(min(lVeri.ranges[144:287]),30)#EGER VERI INF GELIRSE MAX 30 DIYE SINIRLANDIRDIK
#    sag = min(min(lVeri.ranges[0:143]),30)
#    sol_on = min(min(lVeri.ranges[432:575]),30)
#    on = sol_on + sag_on
#    sol = min(min(lVeri.ranges[576:719]),30)
#    print(sag,sag_on,sol,sol_on,on)
    
    # Bir taramada uretilen lidar verisi 360 geliyo onu 360 derece olarak kabul ettim
    
    # CALISMAZZZZZZ LIDARVERISINDEKI DATALARA BAK
    # sag =  min(min(veri.ranges[1,25]),30)
    # sag_on = min(min(veri.ranges[25,60]),30)
    # sol = min(min(veri.ranges[155,180]),30)
    # sol_on = min(min(veri.ranges[120,155]),30)
    # on = min(min(veri.ranges[60,120]),30)
    # print("sag:"+sag)
    # print("sag on:"+sag_on)
    # print("sol:"+sol)
    # print("sol on:"+sol_on)
    # print("on:"+on)
    # time.sleep(1)
lidarVeri()