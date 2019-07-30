# 这个文档用来进行去除图片的边界，以及调整大小到256*256

import os
import cv2
from PIL import Image
import warnings
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
warnings.simplefilter("ignore", category=FutureWarning)
Image.MAX_IMAGE_PIXELS = None

base_path = "input"
image_path = os.path.join(base_path, 'image')
train_path = os.path.join(base_path, 'train')


def removeBorder(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    for imgName in pathDir:
        img = cv2.imread(fileDir + '/' + imgName)
        imgtemp = cv2.resize(img, (456, 456))
        cropped = imgtemp[50:406, 50:406]
        cv2.imwrite(fileDir + '/' + imgName, cropped)


if __name__ == '__main__':
    count = 0
    for i in range(1, 1505):
        fileDir = os.path.join(image_path, str(i))
        if os.path.isdir(fileDir):
            removeBorder(fileDir)
            count += 1
            print("processed :" + str(i) + ",and " + str(count) + "/168")
