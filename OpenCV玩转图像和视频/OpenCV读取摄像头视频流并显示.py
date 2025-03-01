"""
author: tao
date: 25.3

演示OpenCV读取摄像头视频流并显示,保存为视频文件
"""
# 导入必要的包
import numpy as np
import cv2

# 调用摄像头
cap = cv2.VideoCapture(0)

# DIVX X264
fourcc = cv2.VideoWriter_fourcc(*"x264")
fps = 20
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("./video/myDemo.mp4", fourcc=fourcc, fps=fps, frameSize=(width, height))

while True:
    ret, frame = cap.read()
    
    # 镜像显示
    frame = cv2.flip(frame,1)
    
    # 显示摄像头画面
    cv2.imshow("frame", frame)
    
    writer.write(frame)
    
    # 按下ESC键退出
    if cv2.waitKey(10) & 0xFF == 27:
        break

# 关闭资源
writer.release()
cap.release()
cv2.destoryAllWindows()