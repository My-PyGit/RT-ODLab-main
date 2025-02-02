# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1276, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("#groupBox{border-image:url(:/image/images/background.jpg);\n"
"border: 0px solid #42adff;\n"
"border-radius:5px;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_3.setStyleSheet("#groupBox_3{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
";\n"
"border-radius:0px;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(50, 218, 218);\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setStyleSheet("#groupBox_8{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}\n"
"")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.input_video = QtWidgets.QLabel(self.groupBox_8)
        self.input_video.setText("")
        self.input_video.setObjectName("input_video")
        self.horizontalLayout_8.addWidget(self.input_video)
        self.output_video = QtWidgets.QLabel(self.groupBox_8)
        self.output_video.setStyleSheet("")
        self.output_video.setText("")
        self.output_video.setObjectName("output_video")
        self.horizontalLayout_8.addWidget(self.output_video)
        self.horizontalLayout.addWidget(self.groupBox_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox_2.setStyleSheet("#groupBox_2{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
";\n"
"border-radius:0px;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.statistic_label = QtWidgets.QLabel(self.groupBox_2)
        self.statistic_label.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    font-size: 16px;\n"
                                           "    font-family: \"Microsoft YaHei\";\n"
                                           "    font-weight: light;\n"
                                           "         border-radius:9px;\n"
                                           "        background:rgba(66, 195, 255, 0);\n"
                                           "color: rgb(218, 218, 218);\n"
                                           "}\n"
                                           "")
        self.statistic_label.setText("")
        self.statistic_label.setObjectName("statistic_label")
        self.horizontalLayout_6.addWidget(self.statistic_label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_2)
        self.fileButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.fileButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/images/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon)
        self.fileButton.setIconSize(QtCore.QSize(25, 25))
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_10.addWidget(self.fileButton)
        self.runButton = QtWidgets.QPushButton(self.groupBox_2)
        self.runButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.runButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/images/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/运行.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/暂停.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/运行.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/暂停.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/运行.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/image/images/暂停.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.runButton.setIcon(icon1)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setCheckable(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_10.addWidget(self.runButton)
        self.stopButton = QtWidgets.QPushButton(self.groupBox_2)
        self.stopButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.stopButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/images/终止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon2)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_10.addWidget(self.stopButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("QProgressBar{ color: rgb(255, 255, 255); font:12pt; border-radius:2px; text-align:center; border:none; background-color: rgba(215, 215, 215,100);} \n"
"QProgressBar:chunk{ border-radius:0px; background: rgba(80, 40, 80, 200);}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "绝缘子缺陷检测"))
import img_rc
