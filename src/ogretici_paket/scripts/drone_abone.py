#!/usr/bin/env python3

import rospy
from ogretici_paket.msg import drone

def mesajDinle():
    rospy.init_node("Abone_dugumu",anonymous=True)
    rospy.Subscriber("drone_bilgi",drone,yazdir)
    rospy.spin()
    
def yazdir(mesaj):
    rospy.loginfo("Drone Adı:%s",mesaj.isim)
    rospy.loginfo("Drone Batarya:%s",mesaj.batarya)
    rospy.loginfo("Drone Hızı:%d",mesaj.hiz)
    
mesajDinle()