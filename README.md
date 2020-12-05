# radon
# CTradon变换python实现

### 一、原始图与效果图展示：

1、shepp-logan原始图（data文件夹）

![](https://github.com/zlatan-ws123/radon/blob/master/data/shepp_logan.jpg?raw=true)

2、经radon变换后得到的Sinogram图像

![radon](https://github.com/zlatan-ws123/radon/blob/master/result/radon.png?raw=true)

3、经滤波反投影得到的重建图像

![back_project](https://github.com/zlatan-ws123/radon/blob/master/result/back_project.png?raw=true)

4、经过空间域的RL滤波器滤波过后的Sinogram图像

![filter_img](https://github.com/zlatan-ws123/radon/blob/master/result/filter_img.png?raw=true)

5、将滤波后的Sinogram反投影得到的重建图像

![bp_filter_img](https://github.com/zlatan-ws123/radon/blob/master/result/bp_filter_img.png?raw=true)

6、经频率域滤波后的重建图像（失败，未得到预期效果）

![freq_img](https://github.com/zlatan-ws123/radon/blob/master/result/freq_img.png?raw=true)

