"""
author: tao
date: 25.3

演示OpenCV在摄像头视频流上添加文本和图形
"""

# 导入必要的库
import numpy as np
import cv2
import time

# 导入自定义的包
from drawUtils import cv2AddChineseText

# 调用摄像头
cap = cv2.VideoCapture(0)
# 记录开始时间
start_time = time.time()

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    
    # 对摄像头画面进行操作
    frame = cv2.flip(frame, 1)
    
    # 绘制一个矩形
    cv2.rectangle(frame, (100, 100), (200, 200), (255, 0, 255), 10)
    
    # 添加帧率信息
    now = time.time()
    fps = 1 / (now - start_time)
    start_time = now
    
    fps_text = "帧率：" + str(fps)
    # 添加中文文本
    frame = cv2AddChineseText(frame, fps_text, (1200, 50), (0, 255, 0), 70)
    
    # 显示画面
    cv2.imshow("frame", frame)
    
    # 退出条件
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
    