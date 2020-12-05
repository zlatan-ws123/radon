# CTradon变换python实现

### 一、原始图与效果图展示：

1、shepp-logan原始图（data文件夹）

![](D:\My_file\radon\data\shepp_logan.jpg)

2、经radon变换后得到的Sinogram图像

![radon](D:\My_file\radon\result\radon.png)

3、经滤波反投影得到的重建图像

![back_project](D:\My_file\radon\result\back_project.png)

4、经过空间域的RL滤波器滤波过后的Sinogram图像

![filter_img](D:\My_file\radon\result\filter_img.png)

5、将滤波后的Sinogram反投影得到的重建图像

![bp_filter_img](D:\My_file\radon\result\bp_filter_img.png)

6、经频率域滤波后的重建图像（失败，未得到预期效果）

![freq_img](D:\My_file\radon\result\freq_img.png)

