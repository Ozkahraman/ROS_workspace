#!/usr/bin/env python3
import rospy
import actionlib
from ogretici_paket.msg import GorevDurumAction,GorevDurumFeedback,GorevDurumResult

class ActionServer():
    def __init__(self):
        rospy.init_node("action_server_dugumu")
        self.a_server = actionlib.SimpleActionServer("gorev",GorevDurumAction,execute_cb=self.cevabUret,auto_start=False)#gorev adında GorevDurumAction tipinde istek gelince cevabUret fonksiyonunu calıstırıto
        self.a_server.start()
        rospy.spin()

    def cevabUret(self,istek):
        geri_bildirim = GorevDurumFeedback()
        sonuc = GorevDurumResult()
        rate = rospy.Rate(1)#saniyede 1 kere feedback verecek
        for i in range(1,istek.birim):
            durum="%"+ str(i*100/istek.birim)
            geri_bildirim.oran = durum
            self.a_server.publish_feedback(geri_bildirim)
            rate.sleep()

        sonuc.sonuc = "Gorev Tammlandi"    
        self.a_server.set_succeeded(sonuc)

a_s = ActionServer()