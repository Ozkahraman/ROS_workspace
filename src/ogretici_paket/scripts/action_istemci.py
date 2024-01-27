#!/usr/bin/env python3
import rospy
import actionlib
from ogretici_paket.msg import GorevDurumAction, GorevDurumGoal

def bildirimFonksiyonu(bilgi):
    print("Gorev Tamamlama Durumu :",bilgi.oran)

def istekteBulun():
    rospy.init_node("action_istemci_dugumu")
    istemci = actionlib.SimpleActionClient("gorev",GorevDurumAction )
    istemci.wait_for_server()
    istek = GorevDurumGoal()
    istek.birim=5
    istemci.send_goal(istek,feedback_cb=bildirimFonksiyonu)
    istemci.wait_for_result()
    x = istemci.get_result().sonuc
    return x

cikti = istekteBulun()
print("Gorevin Son Durumu:",cikti)