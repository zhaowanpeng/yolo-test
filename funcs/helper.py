# -*- coding:utf-8 -*-

def get_iou(box1, box2):
    iou = 0.0

    (b1_x1, b1_y1, b1_x2, b1_y2) = box1
    (b2_x1, b2_y1, b2_x2, b2_y2) = box2

    state_1 = b1_x2 > b2_x1 and b1_y2 > b2_y1  # 相交
    state_2 = b1_x1 < b2_x2 and b1_y1 < b2_y2  # 不相离

    if state_1 and state_2:
        s1 = (b1_x2 - b1_x1) * (b1_y2 - b1_y1)
        s2 = (b2_x2 - b2_x1) * (b2_y2 - b2_y1)

        (left_point,top_point)=(b1_x1,b1_y1) if b1_x1>b1_x2 else (b2_x1,b2_y1)
        (right_point,bottom_point)=(b1_x2,b1_y2) if b1_x2<b2_x2 else (b2_x2,b2_y2)
        intersection =(right_point-left_point)*(bottom_point-top_point)
        # intersection = (b1_x2 - b2_x1) * (b1_y2 - b2_y1)

        iou = intersection / (s1 + s2 - intersection)

    return iou


# def get_two_img_score(imgInfo1, imgInfo2):
#
#     img1_list=imgInfo1