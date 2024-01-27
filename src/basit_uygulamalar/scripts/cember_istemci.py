#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from basit_uygulamalar.srv import CemberHaraket

rospy.wait_for_service("cember_servis")
try:
    yaricap = float(input("Yaricap Giriniz:"))
    servis = rospy.ServiceProxy("cember_servis",CemberHaraket)
    servis(yaricap)
except rospy.ServiceException:
    print("Servisle alakali hata !!!")
    