"""
author: tao
date: 25.3

演示OpenCV读取视频文件并显示
"""

# 导入必要的包
import numpy as np
import cv2

# 读取视频文件
cap = cv2.VideoCapture("./video/myDemo.mp4")

if not cap.isOpened():
    print("Error: video not opened")
    
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        # 有画面就显示
        cv2.imshow("frame", frame)
        
        # 退出条件
        if cv2.waitKey(10) & 0xFF == 27:
            break
    else:
        # 画面读取完毕自动退出
        break
    
cap.release()
cv2.destroyAllWindows()
    
