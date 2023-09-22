import cv2 as cv
import time

import cv2.gapi
import numpy as np


def color_deal(img, deal_Type):
    """根据用户的选择，对于图像做相应的处理"""
    if img.shape[-1] != 3 and deal_Type != 1:
        pass
    if deal_Type == 1:
        # 手写图像取反色处理
        # time1 = time.time()
        # width = img.shape[1]
        # height = img.shape[0]
        # if img.shape[-1] == 3:
        #     for row in range(height):  # 遍历每一行
        #         for col in range(width):  # 遍历每一列
        #             for channel in range(3):  # 遍历每个通道（三个通道分别是BGR）
        #                 img[row][col][channel] = 255 - img[row][col][channel]
        # else:
        #     for row in range(height):  # 遍历每一行
        #         for col in range(width):  # 遍历每一列
        #             img[row][col] = 255 - img[row][col]
        # time2 = time.time()
        # print("数据检索遍历时间：", (time2 - time1) * 1000)

        # 自己手写的使用for循环的反色方法
        # begTime = time.time()
        # if img.shape[-1] == 3:
        #     for row in range(img.shape[0]):
        #         for col in range(img.shape[1]):
        #             for cha in range(3):
        #                 img[row][col][cha] = 255 - img[row][col][cha]
        # else:
        #     for row in range(img.shape[0]):
        #         for col in range(img.shape[1]):
        #             img[row][col] = 255 - img[row][col]
        #
        # endTime = time.time()
        # print("数据检索遍历时间：", (endTime - begTime) * 1000)

        #自己手写方便的反色方法
        begTime = time.time()
        img = 255 - img
        endTime = time.time()
        print("数据检索遍历时间：", (endTime - begTime) * 1000)


        # opencv求反色函数
        #time1 = time.time()
        #img = cv.bitwise_not(img)
        #time2 = time.time()
        #print("opencv遍历时间：", (time2 - time1) * 1000)

    elif deal_Type == 2:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif deal_Type == 3:
        img = cv.cvtColor(img, cv.COLOR_BGR2Lab)
    elif deal_Type == 4:
        img = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
    elif deal_Type == 5:
        img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    else:
        pass
    return img

def img_sample(img, index):
    #print(type(img))
    #print(img.data)
    if np.all(img == -1):
        print("Plz read img first!")
        return -1
    if img.shape[-1] == 3:
        img = img[0:-1:index, 0:-1:index, :]
    else:
        img = img[0:-1:index, 0:-1:index]
    #print(img.data)
    #print(type(img))
    #print("采样完成")
    return img

def img_quanty(img, index):
    #print('inlevel_deal')
    base = np.floor(256 / index)
    tmp = ((img/base).astype(np.uint8) * base).astype(np.uint8)
    #print(img.shape, tmp.shape)
    return tmp

