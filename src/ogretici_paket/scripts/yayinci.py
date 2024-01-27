#!/usr/bin/env python3
import rospy
from ogretici_paket.msg import BataryaDurum
import random

def mesajYayinla():
    rospy.init_node("yayinci_dugumu",anonymous=True) #Dugum baslatiyoruz
    pub = rospy.Publisher("batarya_konusu",BataryaDurum,queue_size=10)#yayıncı oluşturuyoruz BataryaDurum mesajını yayınlayacaz queue de alınan mesajın buyuklugunu belirtiyo
    rate = rospy.Rate(1)    #hertz cinsinden saniyede 1 kere yayın yapıyoruz
    while not rospy.is_shutdown():
        durum="%52"
        rospy.loginfo(durum)#terminale loginfoyla yazdırıyoz
        pub.publish(durum)#durumu yayınladık
        rate.sleep()#yukarıda hertzi 1 verdik whilein icinde surekli basmamasi icin veriyi delay veriyoruz
        


mesajYayinla()        
