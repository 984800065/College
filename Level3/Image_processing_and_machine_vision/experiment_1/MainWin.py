# Created by: ww 2020/8/11
#界面与逻辑分离，主窗口逻辑代码

import os
import cv2
import sys
import math
from MainDetect_UI import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from Experiment_1 import *

class Main(QMainWindow, Ui_MainWindow):
    """重写主窗体类"""
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self) # 初始化窗体显示
        self.timer = QTimer(self) # 初始化定时器
        # 设置在label中自适应显示图片
        self.label_PrePicShow.setScaledContents(True)
        self.label_PrePicShow.setStyleSheet("QLabel{background-color:rgb(0,0,0);}")  # 初始黑化图像显示区域
        self.label_AftPicShow.setScaledContents(True)
        self.label_AftPicShow.setStyleSheet("QLabel{background-color:rgb(0,0,0);}")
        self.img = None
        self.aftimg = self.img

    def onbuttonclick_selectDataType(self, index):
        """选择输入数据类型(图像,视频)"""
        if index == 1:
            filename, _ = QFileDialog.getOpenFileName(self, "选择图像", os.getcwd(), "Images (*.jpg *.png *.bmp);;All (*)")
            self.img = cv2.imread(filename)
            self.label_PrePicShow.setPixmap(QPixmap(filename))
        elif index == 2:
            filename, _ = QFileDialog.getOpenFileName(self, "选择视频", os.getcwd(), "Videos (*.avi *.mp4);;All (*)")
            self.capture = cv2.VideoCapture(filename)
            self.fps = self.capture.get(cv2.CAP_PROP_FPS)  # 获得视频帧率
            self.timer.timeout.connect(self.slot_video_display)
            flag, self.img = self.capture.read()  # 显示视频第一帧
            if flag:
                self.img_show(self.label_PrePicShow, self.img)
        elif index == 3:
            filename, _ = QFileDialog.getOpenFileName(self, "选择图像", os.getcwd(),
                                                      "Images (*.jpg *.png *.bmp);;All (*)")
            self.img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            self.label_PrePicShow.setPixmap(QPixmap(filename))
        print(type(self.img))

    def onbuttonclick_videodisplay(self):
        """显示视频控制函数, 用于连接定时器超时触发槽函数"""
        if self.pushButton_VideoDisplay.text() == "检测":
            self.timer.start(1000 / self.fps)
            self.pushButton_VideoDisplay.setText("暂停")
        else:
            self.timer.stop()
            self.pushButton_VideoDisplay.setText("检测")

    def slot_video_display(self):
        """定时器超时触发槽函数, 在label上显示每帧视频, 防止卡顿"""
        flag, self.img = self.capture.read()
        if flag:
            self.img_show(self.label_PrePicShow, self.img)
        else:
            self.capture.release()
            self.timer.stop()

    def oncombox_selectColorType(self, index):
        """选择图像色彩处理方式"""
        imgDeal = color_deal(self.img, index)
        self.img_show(self.label_AftPicShow, imgDeal)

    def onintervalslider_valueChanged(self, index):
        #print(index)
        #if(self.img == None): return
        self.intervalLcdNumber.display(index)
        imgDeal = interval_deal(self.img, index)
        self.img_show(self.label_AftPicShow, imgDeal)

    def onlevelslider_valueChanged(self, index):
        index = 2 ** math.ceil(math.log2(index))
        print(index)
        self.levelLcdNumber.display(index - 1)
        #if(self.img == None): return
        imgDeal = level_deal(self.img, index)
        self.img_show(self.label_AftPicShow, imgDeal)

    def img_show(self, label, img):
        """图片在对应label中显示"""
        if img.shape[-1] == 3:
            #qimage = Qimage(img)
            #QImage的构造函数的第一个形参的类型是bytes而不是memorylist
            qimage = QImage(bytes(img.data), img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888).rgbSwapped()
        else:

            qimage = QImage(bytes(np.array(img, dtype=np.uint8).data), img.shape[1], img.shape[0], img.shape[1], QImage.Format_Indexed8)
        label.setPixmap(QPixmap.fromImage(qimage))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
