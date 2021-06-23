# -*- coding:utf-8 -*-
from PIL import Image, ImageFile
from io import BytesIO
import cv2,warnings
import numpy as np
warnings.filterwarnings("ignore")
ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


#still exist part imgs can not be read
def read_img(imgpath,color=True):
    try:
        pic = Image.open(BytesIO(get_file_content(imgpath)))
        if color:
            pic = pic.convert("RGB")
        else:
            pic = pic.convert("L")
        return pic
    except:
        img=read_img_cv(imgpath,color)
        return img

def read_img_cv2(imgpath):
    try:
        pic = Image.open(BytesIO(get_file_content(imgpath)))
        pic = pic.convert("RGB")
        pic = cv2.cvtColor(np.asarray(pic))
        # img = cv2.cvtColor(np.asarray(pic), cv2.COLOR_RGB2BGR)
        return pic
    except:
        img=cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), 1)
        return img


def read_img_cv(imgpath,color=True):
    try:
        img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), 1)
        if color:
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        else:
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        return img
    except:
        return None

def get_iou(box1, box2):
    (left_top_box,right_bottom_box)=(box1,box2) if box1[0]<=box2[0] and box1[1]<= box2[1] else (box2,box1)

    (xmin1,ymin1,xmax1,ymax1)=left_top_box
    (xmin2,ymin2,xmax2,ymax2)=right_bottom_box

    if xmin2>=xmax1 or ymin2>=ymax1:
        iou=0.0

    else:
        (i_xmin,i_ymin)=(xmin2,ymin2)

        (i_xmax,i_ymax)=(xmax2,ymax2) if xmax2<=xmax1 and ymax2<=ymax1 else (xmax1,ymax1)
        intersection = (i_xmax - i_xmin) * (i_ymax - i_ymin)
        s1 = (xmax1 - xmin1) * (ymax1 - ymin1)
        s2 = (xmax2 - xmin2) * (ymax2 - ymin2)
        iou = intersection / (s1 + s2 - intersection)

    return iou



# b1=[0,0,5,5]
# b2=[1,1,3,3]
# c=get_iou(b1,b2)
# d=get_iou(b2,b1)
#
# print(c)
# print(d)
# def get_two_img_score(imgInfo1, imgInfo2):
#
#     img1_list=imgInfo1