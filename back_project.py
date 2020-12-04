from skimage import transform
import cv2
import numpy as np

def bp_star(img, angle = 180):
    lenth = len(img)
    img_sum = np.zeros((lenth, lenth), dtype = 'float')
    #print(img_sum)
    for i in range(angle):
        tmp = np.expand_dims(img[:, i], axis = 0)
        tmp2 = np.repeat(tmp, lenth, axis = 0)
        #print(tmp2)
        img_sum += transform.rotate(tmp2, i)

    return(img_sum)


if __name__ == "__main__":
    image = cv2.imread(r"data\shepp_logan.jpg", cv2.IMREAD_GRAYSCALE)
    test = bp_star(image, angle = 2)
    cv2.imshow("test", test)
