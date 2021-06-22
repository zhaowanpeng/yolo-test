# -*- coding:utf-8 -*-

def get_iou(box1, box2):

    (left_top_box,right_bottom_box)=(box1,box2) if box1[0]<box2[0] or box1[1]< box2[1] else (box2,box1)

    (xmin1,ymin1,xmax1,ymax1)=left_top_box
    (xmin2,ymin2,xmax2,ymax2)=right_bottom_box

    if xmin2>=xmax1 or ymin2>=ymax1:
        iou=0.0
    else:
        (i_xmin,i_ymin)=(xmin2,ymin2)
        (i_xmax,i_ymax)=(xmax2,ymax2) if xmax2<xmax1 or ymax2<ymax1 else (xmax1,ymax1)
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