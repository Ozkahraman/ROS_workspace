#!/usr/bin/env python3
import rospy
from ogretici_paket.srv import GecenZaman


def gecenZamanFoksiyonu(istek):
    robot_hiz=0.5
    sure = istek.hedef_konum/robot_hiz
    return sure

def cevapGonder():
    rospy.init_node("server_dugumu")
    rospy.Service("zaman",GecenZaman,gecenZamanFoksiyonu)#gecen zaman tipinde degisken istek geldiginde gecenzamnaFonksiyonunu calıstırıyo
    rospy.spin()

cevapGonder()    