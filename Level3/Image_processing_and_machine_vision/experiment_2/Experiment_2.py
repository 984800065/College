import cv2 as cv
import numpy as np
import time
import math as m

def bilinear_interpolation(i, j, u, v, img, new_img, rows, cols):
   # bilinear interpolation is 2 slow!!!
   x = int(u)
   y = int(v)

   q = u - x
   p = v - y

   top_left = img[x, y]
   top_right = img[x, y + 1] if y < cols - 1 else img[x, y]
   bottom_left = img[x + 1, y] if x < rows - 1 else img[x, y]
   bottom_right = img[x + 1, y + 1] if x < rows - 1 and y < cols - 1 else img[x, y]

   new_img[i, j] = (1 - p) * ((1 - q) * top_left + q * top_right) + p * ((1 - q) * bottom_left + q * bottom_right)

def nearlest_interpolation(i, j, u, v, img, new_img, rows, cols):
   x = int(u)
   y = int(v)

   new_img[i, j] = img[x, y]

def img_zoom(img, zm):
   if np.all(img == -1):
      print("Plz select Img first")
      return
   """对于传入的图像进行缩放操作, *zm:缩放因子"""
   time1 = time.time()
   rows, cols = img.shape[:2]  #获取宽和高
   new_img = np.zeros(img.shape, dtype=np.uint8) #新建同原图大小一致的空图像
   # # 手写图像缩放代码
   if img.shape[-1] == 3:
      img = np.pad(img, ((0, 1), (0, 1), (0, 0)), 'constant', constant_values = 0)
   else:
      img = np.pad(img, ((0, 1), (0, 1)), 'constant', constant_values = 0)

   c = 1 / zm

   if zm < 1:
      for i in range(int(rows * zm)):
         for j in range(int(cols * zm)):
            ii = int(c * i)
            jj = int(c * j)
            if ii < rows and jj < cols:
               new_img[i, j] = img[ii, jj]
            else:
               new_img[i, j] = img[0, 0] * 0
   else:
      x_indices = np.arange(rows) * c
      y_indices = np.arange(cols) * c
      for i in range(rows):
         for j in range(cols):
            bilinear_interpolation(i, j, x_indices[i], y_indices[j], img, new_img, rows, cols)

            # nearlest_interpolation(i, j, x_indices[i], y_indices[j], img, new_img, rows, cols)
      
      #2 slow

   time2 = time.time()
   print("手写缩放程序处理时间： %.3f毫秒" %((time2 - time1) * 1000))

   # opencv图像缩放
   # img = cv.resize(img, (int(cols*zm), int(rows*zm)), interpolation=cv.INTER_CUBIC)
   # if zm>1: # 原图像大小显示
   #    new_img = img[0:cols, 0:rows]
   # else:
   #    new_img[0:img.shape[0], 0:img.shape[1]] = img
   # time2 = time.time()
   # print("opencv缩放程序处理时间：%.3f毫秒" %((time2 - time1) * 1000))
   return new_img

def img_translation(img, trans):
   if np.all(img == -1):
      print("Plz select Img first!")
      return
   """对于传入的图像进行左右, *trans:平移参数"""
   time1 = time.time()
   new_img = np.zeros(img.shape, dtype=np.uint8)  # 新建同原图大小一致的空图像
   rows, cols = img.shape[: 2]
   # # 手写图像平移代码
   # for i in range(rows):
   #    for j in range(cols):
   #       new_img[i, j] = img[i, j - trans] if j - trans >= 0 and j - trans < cols else img[0, 0] * 0
   # too slow 

   new_img[:, 0 if trans <= 0 else trans : cols if trans >= 0 else trans] = img[:, 0 if trans >= 0 else -trans : cols if trans <= 0 else -trans]

   time2 = time.time()
   print("手写图像平移程序处理时间：%.3f毫秒" %((time2 - time1) * 1000))
   return new_img

def img_imgMirror(img):
   """对于传入的图像进行左右翻转"""
   if np.all(img == -1):
      print("Plz select IMG first!")
      return
   time1 = time.time()
   rows, cols = img.shape[:2]  # 获取宽和高
   new_img = np.zeros(img.shape, dtype=np.uint8)  # 新建同原图大小一致的空图像

   new_img = np.fliplr(img)

   time2 = time.time()
   print("手写镜面变换程序处理时间：%.3f毫秒" %((time2 - time1) * 1000))
   return new_img

def img_rotation(img, rot):
   """对于传入的图像进行旋转，可以绕任一点旋转, *rot:旋转角度"""

   time1 = time.time()

   # # 手写图像绕任一点旋转代码
   h, w = img.shape[: 2] # 获取宽和高

   tmp1 = (w - 1) / 2
   tmp2 = (h - 1) / 2

   costheta = np.cos(np.radians(rot))
   sintheta = np.sin(np.radians(rot))

   fDstX1, fDstY1 = (-tmp1 * costheta + tmp2 * sintheta, tmp1 * sintheta + tmp2 * costheta)
   fDstX2, fDstY2 = (tmp1 * costheta + tmp2 * sintheta, -tmp1 * sintheta + tmp2 * costheta)
   fDstX3, fDstY3 = (-tmp1 * costheta - tmp2 * sintheta, tmp1 * sintheta - tmp2 * costheta)
   fDstX4, fDstY4 = (tmp1 * costheta - tmp2 * sintheta, -tmp1 * sintheta - tmp2 * costheta)

   # print(fDstX1, fDstY1)
   # print(fDstX2, fDstY2)
   # print(fDstX3, fDstY3)
   # print(fDstX4, fDstY4)

   wout = int(abs(np.max([fDstX1, fDstX2, fDstX3, fDstX4]) - np.min([fDstX1, fDstX2, fDstX3, fDstX4])))
   hout = int(abs(np.max([fDstY1, fDstY2, fDstY3, fDstY4]) - np.min([fDstY1, fDstY2, fDstY3, fDstY4])))

   new_shape = (hout, wout, 3) if img.shape[-1] == 3 else (hout, wout)
   
   new_img = np.zeros(new_shape, dtype = np.uint8)

   a = tmp1
   b = tmp2 
   c = (wout - 1) / 2
   d = (hout - 1) / 2

   f1 = -c * costheta + d * sintheta + a
   f2 = -c * sintheta - d * costheta + b

   # print(img.shape)
   # print(new_shape)
   # print(rot)
   # print(hout, wout)
   # print(costheta, sintheta)
   # print(f1, f2)

   for i in range(new_shape[0]):
      for j in range(new_shape[1]):
         # new cod
         xx = j # cod
         yy = i # cod
         # org cod

         u = xx * costheta - yy * sintheta + f1 # cod
         v = xx * sintheta + yy * costheta + f2 # cod
         
         # pos in new_img is (i, j)
         # pos in org_img is (u + a, v + b)

         # print(xx, yy, u, v)
         orgx = int(u)
         orgy = int(v)

         if orgx >= 0 and orgx < img.shape[1] - 1 and orgy >= 0 and orgy < img.shape[0] - 1:
            bilinear_interpolation(i, j, v, u, img, new_img, hout, wout)

            # nearlest_interpolation(i, j, v, u, img, new_img, hout, wout)

   time2 = time.time()
   print("手写旋转程序处理时间：%.3f毫秒" %((time2 - time1) * 1000))

   # opencv绕任一点旋转代码
   # rows, cols = img.shape[:2]
   # b, a = rows / 2, cols / 2  # 设置旋转点位置
   # h, w = rows / 2, cols / 2
   # 第一个参数是旋转中心，第二个参数是旋转角度，第三个因子是旋转后的缩放因子
   # M = cv.getRotationMatrix2D((a, b), rot, 1)
   # cos, sin = np.abs(M[0, 0]), np.abs(M[0, 1])
   # new_cols = int((rows * sin) + (cols * cos))
   # new_rows = int((rows * cos) + (cols * sin))
   # M[0, 2] += (new_cols / 2) - w
   # M[1, 2] += (new_rows / 2) - h
   # new_img = cv.warpAffine(img, M, (new_cols, new_rows))  # 第三个参数是输出图像的尺寸中心，图像的宽和高
   # time2 = time.time()
   # print("opencv旋转程序处理时间：%.3f毫秒" %((time2 - time1) * 1000))
   return new_img

def onmouse_pick_points(event, x, y, flags, l_ImgPot):
   """card_correction的鼠标回调函数, """
   if event == cv.EVENT_LBUTTONDOWN:
      print('x = %d, y = %d' % (x, y))
      l_ImgPot[2].append((x, y))
      cv.drawMarker(l_ImgPot[1], (x, y), (0, 0, 255))
   if event == cv.EVENT_RBUTTONDOWN:
      l_ImgPot[1] = l_ImgPot[0].copy() # 将没有画十字的原图重新赋值给显示图像
      if len(l_ImgPot[2]) != 0:
         l_ImgPot[2].pop() # 将最后一次绘制的标记清除
         for i in range(len(l_ImgPot[2])): # 重新绘制全部标记
            cv.drawMarker(l_ImgPot[1], l_ImgPot[2][i], (0, 0, 255))

def card_correction(img):
   """对于传入的图像进行鼠标交互，选择四个顶点进行名片矫正"""
   l_ImgPot = [img, img.copy(), []] # 记录画标识的图像和标识点  [0]原图 【1】处理后图
   cv.namedWindow('card', cv.WINDOW_AUTOSIZE)
   cv.setMouseCallback('card', onmouse_pick_points, l_ImgPot)
   while True:
      cv.imshow('card', l_ImgPot[1])
      key = cv.waitKey(30)
      if key == 27:  # ESC
         break
   cv.destroyAllWindows()
   time1 = time.time()
   # 900 * 540
   # for i in range(len(l_ImgPot)):
   #    print(i, l_ImgPot[i])
   # # 透视变换矫正名片核心代码(可opencv)
   # left_up right_up left_down right_down
   pts1 = np.float32(l_ImgPot[2])
   pts2 = np.float32([[0, 0], [540, 0], [0, 900], [540, 900]])   

   print(pts1)
   print(pts2)


   M = cv.getPerspectiveTransform(pts1,pts2)

   new_img = cv.warpPerspective(img, M, (540,900))

   time2 = time.time()
   print("opencv名片矫正处理时间：%.3f毫秒" %((time2 - time1) * 1000))

   return new_img