# -*- coding:utf-8 -*-
from model.YOLOv3 import YOLOv3
import cv2
import numpy as np

with open("./model/cfg/coco.names") as f:
    classes = f.read().splitlines()

def yolo_detect(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    yolo = YOLOv3("./model/cfg/yolo_v3.cfg", "./model/weight/yolov3.weights", "./model/cfg/coco.names")
    bbox, cls_conf, cls_ids = yolo(img)
    obj_num = cls_ids.shape[0]
    obj_list = []
    for i in range(obj_num):
        obj_list.append(
            (classes[cls_ids[i]], cls_conf[i], bbox[i])
        )
    return obj_list


def demo():


    yolo = YOLOv3("./model/cfg/yolo_v3.cfg", "./model/weight/yolov3.weights", "./model/cfg/coco.names")
    img_path="./data/004545.jpg"
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bbox, cls_conf, cls_ids = yolo(img)

    obj_num=cls_ids.shape[0]
    obj_list=[]
    for i in range(obj_num):
        obj_list.append(
            (classes[cls_ids[i]],cls_conf[i],bbox[i].astype(np.int32))
        )

    # print(obj_list)
    #
    # point_size = 10
    # point_color = (0, 0, 255)  # BGR
    # thickness = 4  # 可以为 0 、4、8
    #
    # # 要画的点的坐标
    # points_list = [(272, 20), (350,223)]
    #
    # for point in points_list:
    #     cv2.circle(img, point, point_size, point_color, thickness)
    #
    # cv2.imshow('image', img)
    # cv2.waitKey(10000)  # 显示 10000 ms 即 10s 后消失
    #print(bbox)
    #print(bbox[0])


if __name__ == "__main__":
    pass
    #demo()
#yolo = YOLOv3("cfg/yolo_v3.cfg", "weight/yolov3.weights", "cfg/coco.names")