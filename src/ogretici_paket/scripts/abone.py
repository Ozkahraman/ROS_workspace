#!/usr/bin/env python3
import rospy
from ogretici_paket.msg import BataryaDurum


def bataryaFonksiyonu(mesaj):
    rospy.loginfo("Robot Batarya:%s" %mesaj.batarya)


def mesajDinle():
    rospy.init_node("Abone_Dugumu")#dugumju olusturduk
    rospy.Subscriber("batarya_konusu",BataryaDurum,bataryaFonksiyonu)#publisherda yazdıgımız batarya_konusuna abone oluyor ordan data dinliyo abone olduktan sonra batarya_fonksiyonunu çalıştırıyoü
    rospy.spin()#surekli donmeyi saglıyo dongu


mesajDinle()    