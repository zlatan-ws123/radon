from skimage import transform
import cv2
import numpy as np
import sys
import warnings

warnings.filterwarnings('ignore')   #忽略掉一堆警告

sys.path.append(r'./')  #添加模块路径为后面引入本路径下的模块做准备
#print(sys.path)
import back_project     #加入自编反投影模块

image = cv2.imread(r"data\shepp_logan.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("test", image)     #显示shepp logan原图

tmp = transform.radon(image).astype('float64')
img_radon = np.rint(tmp / np.max(tmp) * 254).astype('uint8')   #标准化radon变换
cv2.imshow("radon", img_radon)   #显示雷登变换后的图片
#cv2.imwrite(r"result\radon.png", img_radon)
#print(img_radon)

result = back_project.bp_star(img_radon)
bp_img = np.rint(result / np.max(result) * 254).astype('uint8')   #标准化反投影
cv2.imshow("back_project", bp_img)   #显示背景反投影图片
#cv2.imwrite(r"result\back_project.png", bp_img)

'''
import fft_bp   #加入傅里叶滤波反投影模块

fft_exe = fft_bp.fft_img(img_radon)
img_fft = fft_exe.fft_start(img_radon)
img_fft = np.rint(img_fft / np.max(img_fft) * 254).astype('uint8')
cv2.imshow("fft_img", img_fft)

fft_bp_img = back_project.bp_star(img_fft)
fft_bp_img = np.rint(fft_bp_img / np.max(fft_bp_img) * 254).astype('uint8')
cv2.imshow("fft_bp_img", fft_bp_img)

rl_kernel = fft_exe.R_L_kernel(image)
rl_fft = fft_exe.fft_start(img_radon)
#print(rl_fft)
rl_img = np.rint(rl_fft / np.max(rl_fft) * 254).astype('uint8')
cv2.imshow("rl_fft_img", rl_img)

rl_bp_img = back_project.bp_star(rl_img)
rl_bp_img = np.rint(rl_bp_img / np.max(rl_bp_img) * 254).astype('uint8')   #标准化反投影
cv2.imshow("rl_back_project", rl_bp_img)
'''

import rl_filter

new_filter = rl_filter.RL_filter()  #rl滤波器理想的低通滤波器
kj = new_filter.KJ_filter()   #时域滤波器
kj_img = new_filter.KJ_start(img_radon)   #开始卷积滤波

bp_kj = back_project.bp_star(kj_img)
bp_kj += abs(np.min(bp_kj))
bp_kj = np.rint(bp_kj / np.max(bp_kj) * 255).astype('uint8')
kj_img += abs(np.min(kj_img))        #一直没出图像竟然是标准化没做好的原因，注意
kj_img = kj_img / np.max(kj_img) * 255
cv2.imshow('kjimg', kj_img.astype('uint8'))
#cv2.imwrite(r"result\filter_img.png", kj_img.astype('uint8'))
cv2.imshow('bp2', bp_kj)
#cv2.imwrite(r"result\bp_filter_img.png", bp_kj)

fr_filt = new_filter.FRE_filter()
last_img = new_filter.fft_start(img_radon, fr_filt)
last_bp = back_project.bp_star(last_img)
#last_bp += abs(np.min(last_bp))
last_bp = np.rint(last_bp / np.max(last_bp) * 255).astype('uint8')
cv2.imshow('last_fre', last_bp)
cv2.imwrite(r"result\freq_img.png", last_bp)
cv2.waitKey(0)
cv2.destroyAllWindows()
