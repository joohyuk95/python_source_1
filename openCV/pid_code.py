# x 방향 pid
import numpy as np
p, d = 0.5, 0.5

errorLR = w // 2 - cx
posX = p * errorLR + d * (errorLR - perrorLR)
posX = np.interp(posX, [-w//2, w//2], [20, 160])    # range mapping 함수 posX 값을 [20, 160] 범위로 매핑
perrorLR = errorLR

# object tracking pd control