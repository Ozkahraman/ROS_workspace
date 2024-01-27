#!/usr/bin/env python3

import rospy
from ogretici_paket.msg import drone
import random

def mesajYayinla():
    rospy.init_node("drone_yayini",anonymous=True)
    pub = rospy.Publisher("drone_bilgi",drone,queue_size=10)
    rate = rospy.Rate(1)
    bilgi = drone()
    bilgi.batarya=23
    bilgi.isim="Asuman"
    bilgi.hiz=random.randint(5,25) #5-25 arasi random degerler
    while not rospy.is_shutdown():
        rospy.loginfo(bilgi)
        pub.publish(bilgi)
        rate.sleep()
        
mesajYayinla()       