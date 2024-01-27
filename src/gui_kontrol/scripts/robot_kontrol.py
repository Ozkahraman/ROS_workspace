#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_ileri = QtWidgets.QPushButton(self.centralwidget)
        self.button_ileri.setGeometry(QtCore.QRect(120, 70, 89, 25))
        self.button_ileri.setObjectName("button_ileri")
        self.button_sola = QtWidgets.QPushButton(self.centralwidget)
        self.button_sola.setGeometry(QtCore.QRect(20, 120, 89, 25))
        self.button_sola.setObjectName("button_sola")
        self.button_saga = QtWidgets.QPushButton(self.centralwidget)
        self.button_saga.setGeometry(QtCore.QRect(220, 120, 89, 25))
        self.button_saga.setObjectName("button_saga")
        self.button_geri = QtWidgets.QPushButton(self.centralwidget)
        self.button_geri.setGeometry(QtCore.QRect(120, 170, 89, 25))
        self.button_geri.setObjectName("button_geri")
        self.button_dur = QtWidgets.QPushButton(self.centralwidget)
        self.button_dur.setGeometry(QtCore.QRect(120, 120, 89, 25))
        self.button_dur.setObjectName("button_dur")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 40, 231, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_lineer = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_lineer.setObjectName("label_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_lineer)
        self.lineEdit_lineer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_lineer.setReadOnly(True)
        self.lineEdit_lineer.setObjectName("lineEdit_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_lineer)
        self.lineEdit_acisal = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_acisal.setReadOnly(True)
        self.lineEdit_acisal.setObjectName("lineEdit_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_acisal)
        self.label_acisal = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_acisal.setObjectName("label_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_acisal)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 10, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(370, 170, 231, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_X = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_X.setObjectName("label_X")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_X)
        self.label_Y = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_Y.setObjectName("label_Y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Y)
        self.lineEdit_X = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_X.setReadOnly(True)
        self.lineEdit_X.setObjectName("lineEdit_X")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_X)
        self.lineEdit_Y = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_Y.setReadOnly(True)
        self.lineEdit_Y.setObjectName("lineEdit_Y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Y)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 150, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_ileri.setText(_translate("MainWindow", "İleri"))
        self.button_sola.setText(_translate("MainWindow", "Sola"))
        self.button_saga.setText(_translate("MainWindow", "Sağa"))
        self.button_geri.setText(_translate("MainWindow", "Geri"))
        self.button_dur.setText(_translate("MainWindow", "Dur"))
        self.label_lineer.setText(_translate("MainWindow", "Lineer Hız(m/s):"))
        self.label_acisal.setText(_translate("MainWindow", "Açısal Hız(rad/s):"))
        self.label_3.setText(_translate("MainWindow", "Hız Göstergesi"))
        self.label_X.setText(_translate("MainWindow", "Konum X(m):"))
        self.label_Y.setText(_translate("MainWindow", "Konum Y(m):"))
        self.label_6.setText(_translate("MainWindow", "Konum Göstergesi"))
        self.label.setText(_translate("MainWindow", "Robot Kontrol"))

        rospy.init_node("robot_arayuz")
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        
        
        self.button_dur.clicked.connect(self.robotDur)
        self.button_geri.clicked.connect(self.geriGit)
        self.button_ileri.clicked.connect(self.ileriGit)
        self.button_sola.clicked.connect(self.solaDon)
        self.button_saga.clicked.connect(self.sagaDon)
        
        self.lineEdit_acisal.setText(str(0.0))
        self.lineEdit_lineer.setText(str(0.0))
        self.lineEdit_X.setText(str(0.0))
        self.lineEdit_Y.setText(str(0.0))
    
    def odomCallback(self,veri):
        self.lineEdit_X.setText(str(round(veri.pose.pose.position.x,4)))#round: virgulden sonra 4 basamak
        self.lineEdit_Y.setText(str(round(veri.pose.pose.position.x,4)))
        
    def robotDur(self):
        self.hiz_mesaji.linear.x = 0.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        
        self.lineEdit_acisal.setText(str(self.hiz_mesaji.angular.z))
        self.lineEdit_lineer.setText(str(self.hiz_mesaji.linear.x))
        
    def geriGit(self):
        self.hiz_mesaji.linear.x = -1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        
        self.lineEdit_acisal.setText(str(self.hiz_mesaji.angular.z))
        self.lineEdit_lineer.setText(str(self.hiz_mesaji.linear.x))
        
    def ileriGit(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        
        self.lineEdit_acisal.setText(str(self.hiz_mesaji.angular.z))
        self.lineEdit_lineer.setText(str(self.hiz_mesaji.linear.x))
        
    def solaDon(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = 1.0
        self.pub.publish(self.hiz_mesaji)
        
        self.lineEdit_acisal.setText(str(self.hiz_mesaji.angular.z))
        self.lineEdit_lineer.setText(str(self.hiz_mesaji.linear.x))
        
    def sagaDon(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = -1.0
        self.pub.publish(self.hiz_mesaji)
        
        self.lineEdit_acisal.setText(str(self.hiz_mesaji.angular.z))
        self.lineEdit_lineer.setText(str(self.hiz_mesaji.linear.x))
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

