# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:57:18 2020

@author: HAOHAN
"""
import numpy as np
import math
from scipy.signal import convolve


class RL_filter():
    def KJ_filter(self, d = 1, lenth = 256, angle = 180):
        self.weith = lenth
        self.angle = angle
        self.rl_filter = np.zeros((lenth, angle), dtype = 'float64')
        self.tmp = np.zeros(lenth, dtype = 'float64')
        n =lenth / 2
        for i in range(int(self.weith / 2)):
            n1 = i - n
            self.tmp[i] = -2 / (pow(math.pi, 2) * d**2 * (4 * pow(n1, 2) - 1))
        for k in range(int(self.weith / 2)):
            self.tmp[int(k + n)] = -2 / (pow(math.pi, 2) * d**2 * (4 * pow(k, 2) - 1))
        for j in range(self.angle):
            self.rl_filter[:, j] = self.tmp    
        #print(self.rl_filter)
        return(self.rl_filter)
    
    def FRE_filter(self, angle = 180):
        tmp2 = np.fft.fft(self.tmp)
        rl_filter2 = np.tile(tmp2, (angle, 1))
        return rl_filter2.T
    
    def KJ_start(self, img):   #空间域滤波函数  参数img为radon后的图
        new_img = np.zeros((len(img), img.shape[1]), dtype = 'float64')
        for i in range(img.shape[1]):
            filt = self.rl_filter[:, i]
            filt = filt.flatten()
            value = np.squeeze(img[:, i])
            value = value.flatten()
            # print(filt)
            # print(filt[])
            # print(np.shape(value))
            # break
            new_img[:, i] = convolve(filt, value, 'same')
            
        return new_img
    
    def fft_start(self, img, filt_fre):
        self.fft_img = np.zeros((img.shape[0], img.shape[1]), dtype = "float64")
        for i in range(img.shape[1]):
            tmp = np.expand_dims(img[:, i], axis = 0)
            #print(tmp)
            self.fft_img[:, i] = np.fft.fftshift(np.fft.fft(tmp))
        self.ifft_img = np.zeros((img.shape[0], img.shape[1]), dtype = "float64")
        for j in range(img.shape[1]):
            self.ifft_img[:, j] = np.fft.ifft(np.fft.ifftshift(filt_fre[:, j] * self.fft_img[:, j]))
            
        return self.ifft_img

if __name__ == '__main__':
    test = RL_filter()
    tt = test.KJ_filter()
    tt2 = test.FRE_filter()
    print(tt2)