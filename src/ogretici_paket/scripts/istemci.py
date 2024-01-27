#!/usr/bin/env python3
import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")#zaman adlı servisi bekliyoruz
    try:
        servis = rospy.ServiceProxy("zaman",GecenZaman)
        cevap = servis(x)
        return cevap.gecen_zaman
    
    except rospy.ServiceException:
        print("Servisle Alakali Hata")
        
        
hedef=float(input("Hedef Konumu Giriniz:"))        
t=istekteBulun(hedef)
print("Hedefe varana kadar gecen sure:",t)