# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDetect_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1408, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_AftShow = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_AftShow.setGeometry(QtCore.QRect(710, 10, 690, 490))
        self.groupBox_AftShow.setObjectName("groupBox_AftShow")
        self.label_AftPicShow = QtWidgets.QLabel(self.groupBox_AftShow)
        self.label_AftPicShow.setGeometry(QtCore.QRect(10, 30, 670, 460))
        self.label_AftPicShow.setText("")
        self.label_AftPicShow.setObjectName("label_AftPicShow")
        self.groupBox_PreShow = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_PreShow.setGeometry(QtCore.QRect(10, 10, 690, 490))
        self.groupBox_PreShow.setObjectName("groupBox_PreShow")
        self.label_PrePicShow = QtWidgets.QLabel(self.groupBox_PreShow)
        self.label_PrePicShow.setGeometry(QtCore.QRect(10, 30, 670, 460))
        self.label_PrePicShow.setText("")
        self.label_PrePicShow.setScaledContents(True)
        self.label_PrePicShow.setObjectName("label_PrePicShow")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 510, 371, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_datatype_2 = QtWidgets.QLabel(self.groupBox)
        self.label_datatype_2.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.label_datatype_2.setObjectName("label_datatype_2")
        self.comboBox_ColorDeal = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ColorDeal.setGeometry(QtCore.QRect(80, 20, 101, 22))
        self.comboBox_ColorDeal.setObjectName("comboBox_ColorDeal")
        self.comboBox_ColorDeal.addItem("")
        self.comboBox_ColorDeal.setItemText(0, "")
        self.comboBox_ColorDeal.addItem("")
        self.comboBox_ColorDeal.addItem("")
        self.comboBox_ColorDeal.addItem("")
        self.comboBox_ColorDeal.addItem("")
        self.comboBox_ColorDeal.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 351, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.intervalLabel = QtWidgets.QLabel(self.layoutWidget)
        self.intervalLabel.setObjectName("intervalLabel")
        self.horizontalLayout.addWidget(self.intervalLabel)
        self.intervalHorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.intervalHorizontalSlider.setMinimum(1)
        self.intervalHorizontalSlider.setMaximum(10)
        self.intervalHorizontalSlider.setProperty("value", 1)
        self.intervalHorizontalSlider.setSliderPosition(1)
        self.intervalHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.intervalHorizontalSlider.setObjectName("intervalHorizontalSlider")
        self.horizontalLayout.addWidget(self.intervalHorizontalSlider)
        self.intervalLcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.intervalLcdNumber.setLineWidth(0)
        self.intervalLcdNumber.setProperty("value", 1.0)
        self.intervalLcdNumber.setProperty("intValue", 1)
        self.intervalLcdNumber.setObjectName("intervalLcdNumber")
        self.horizontalLayout.addWidget(self.intervalLcdNumber)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 351, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.levelLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.levelLabel.setObjectName("levelLabel")
        self.horizontalLayout_2.addWidget(self.levelLabel)
        self.levelHorizontalSlider = QtWidgets.QSlider(self.layoutWidget1)
        self.levelHorizontalSlider.setMinimum(2)
        self.levelHorizontalSlider.setMaximum(255)
        self.levelHorizontalSlider.setProperty("value", 255)
        self.levelHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.levelHorizontalSlider.setObjectName("levelHorizontalSlider")
        self.horizontalLayout_2.addWidget(self.levelHorizontalSlider)
        self.levelLcdNumber = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.levelLcdNumber.setLineWidth(0)
        self.levelLcdNumber.setProperty("intValue", 255)
        self.levelLcdNumber.setObjectName("levelLcdNumber")
        self.horizontalLayout_2.addWidget(self.levelLcdNumber)
        self.label_datatype = QtWidgets.QLabel(self.centralwidget)
        self.label_datatype.setGeometry(QtCore.QRect(400, 630, 81, 20))
        self.label_datatype.setObjectName("label_datatype")
        self.pushButton_VideoDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_VideoDisplay.setGeometry(QtCore.QRect(590, 630, 71, 23))
        self.pushButton_VideoDisplay.setObjectName("pushButton_VideoDisplay")
        self.comboBox_SelectData = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_SelectData.setGeometry(QtCore.QRect(480, 630, 101, 22))
        self.comboBox_SelectData.setObjectName("comboBox_SelectData")
        self.comboBox_SelectData.addItem("")
        self.comboBox_SelectData.setItemText(0, "")
        self.comboBox_SelectData.addItem("")
        self.comboBox_SelectData.addItem("")
        self.comboBox_SelectData.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1408, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_SelectData.currentIndexChanged['int'].connect(MainWindow.onbuttonclick_selectDataType) # type: ignore
        self.pushButton_VideoDisplay.clicked.connect(MainWindow.onbuttonclick_videodisplay) # type: ignore
        self.comboBox_ColorDeal.currentIndexChanged['int'].connect(MainWindow.oncombox_selectColorType) # type: ignore
        self.intervalHorizontalSlider.valueChanged['int'].connect(MainWindow.onintervalslider_valueChanged) # type: ignore
        self.levelHorizontalSlider.valueChanged['int'].connect(MainWindow.onlevelslider_valueChanged) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_AftShow.setTitle(_translate("MainWindow", "测试实例"))
        self.groupBox_PreShow.setTitle(_translate("MainWindow", "输入实例"))
        self.groupBox.setTitle(_translate("MainWindow", "第一章"))
        self.label_datatype_2.setText(_translate("MainWindow", "色彩处理："))
        self.comboBox_ColorDeal.setItemText(1, _translate("MainWindow", "反色处理"))
        self.comboBox_ColorDeal.setItemText(2, _translate("MainWindow", "灰值化"))
        self.comboBox_ColorDeal.setItemText(3, _translate("MainWindow", "Lab颜色模型"))
        self.comboBox_ColorDeal.setItemText(4, _translate("MainWindow", "YCrCb颜色模型"))
        self.comboBox_ColorDeal.setItemText(5, _translate("MainWindow", "HSI颜色模型"))
        self.intervalLabel.setText(_translate("MainWindow", "采样间隔"))
        self.levelLabel.setText(_translate("MainWindow", "量化级数"))
        self.label_datatype.setText(_translate("MainWindow", "选择数据类型："))
        self.pushButton_VideoDisplay.setText(_translate("MainWindow", "检测"))
        self.comboBox_SelectData.setItemText(1, _translate("MainWindow", "读入图像"))
        self.comboBox_SelectData.setItemText(2, _translate("MainWindow", "读入本地视频"))
        self.comboBox_SelectData.setItemText(3, _translate("MainWindow", "读入灰度图像"))
