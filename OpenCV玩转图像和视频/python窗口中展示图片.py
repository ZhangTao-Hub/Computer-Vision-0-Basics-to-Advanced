"""
author: tao
date: 25.3

演示python窗口展示图片
"""

import cv2
import numpy as np

cat_img = cv2.imread("./img/cat.jpg")

while True:
    cv2.imshow("cat", cat_img)
    
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
cv2.destoryAllWindows()