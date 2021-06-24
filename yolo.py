# -*- coding:utf-8 -*-
from model.YOLOv3 import YOLOv3
import cv2,random,os,time
import numpy as np
from funcs.helper import get_iou,read_img_cv2

import warnings
warnings.filterwarnings("ignore")

with open("./model/cfg/coco.names") as f:
    classes = f.read().splitlines()

yolo = YOLOv3("./model/cfg/yolo_v3.cfg", "./model/weight/yolov3.weights", "./model/cfg/coco.names",use_cuda=True)

def yolo_detect(img):
    st=time.time()
    bbox, cls_conf, cls_ids = yolo(img)
    et=time.time()
    print("yolo process time : {}".format(et-st))
    obj_num = cls_ids.shape[0]
    obj_list = []
    for i in range(obj_num):
        obj=(classes[cls_ids[i]], cls_conf[i], bbox[i].astype(np.int32))
        obj_list.append(obj)
    return obj_list

def draw_bbox_use_res(img,obj_list):
    if len(obj_list)==0:
        return img
    for obj in obj_list:
        B = random.randrange(0, 255, 10)
        G = random.randrange(0, 255, 10)
        R = random.randrange(0, 255, 10)
        cv2.rectangle(img, (obj[2][0], obj[2][1]), (obj[2][2], obj[2][3]), (B, G, R), 1)
        cv2.putText(img,"{}:{:.2f}".format(obj[0],obj[1]), (obj[2][0], obj[2][1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (B, G, R), 1)
    cv2.imshow('image', img)
    cv2.waitKey(10000*30)

def compare(img1,img2,label_filter=True,iou_thred=0.7):
    obj_list1=yolo_detect(img1)
    obj_list2=yolo_detect(img2)

    score = 0
    if len(obj_list1)==0 or len(obj_list2)==0:
        return score

    for i,obj1 in enumerate(obj_list1):
        for j,obj2 in enumerate(obj_list2):

            iou=get_iou(obj1[2],obj2[2])
            label_state = obj1[0] == obj2[0]

            if iou>=iou_thred and label_state>=label_filter:

                score += 1

    return score*2/(len(obj_list1)+ len(obj_list2))



def check(filepath,score_thred=0.7,summarize=True):
    imgs = os.listdir(filepath)
    similars=[]
    for imgName1 in imgs:
        img_path1=filepath+imgName1
        img1=read_img_cv2(img_path1)
        for imgName2 in imgs:
            img_path2 = filepath + imgName2
            img2 = read_img_cv2(img_path2)
            score = compare(img1,img2)
            s_obj = ({imgName1,imgName2},score)
            if score>=score_thred and s_obj not in similars:
               similars.append(s_obj)
    if summarize:
        for item in similars:
            ss = [item[0].pop() for i in range(len(item[0]))]
            (img1,img2)=ss if len(ss)==2 else (ss[0],ss[0])
            print("score:{}      compare {} and {}".format(item[1],img1,img2))
    return similars

check("./data/")
