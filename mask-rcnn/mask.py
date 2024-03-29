# It saves masked images at the respective image location

import numpy as np
import argparse
import random
import time
import cv2
import os
from mask_rcnn import mask_rcnn




# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input images")
# ap.add_argument("-m", "--mask-rcnn", required=True,
# 	help="base path to mask-rcnn directory")
ap.add_argument("-v", "--visualize", type=int, default=0,
	help="whether or not we are going to visualize each instance")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="minimum threshold for pixel-wise mask segmentation")
args = vars(ap.parse_args())

file = sorted(os.listdir(args["image"]))
for i in range(len(file)):
      file[i] = os.path.join(args["image"],file[i])
# print (file)      
traintxt = open("/home/zorawar/Desktop/SfMLearner-master/kitti-processed/train.txt","w+")
for i in range(len(file)):      
      images = sorted(os.listdir(file[i]))
      # print (images)
      # print (len(images))
      x = []
      for k in images:
            if '.jpg' in k:
                  x.append(k)

      for k in range(len(x)):
            traintxt.write(file[i] + " "+ x[k][:10] +"\n")
            x[k] = os.path.join(file[i],x[k])
                        
      # print (x)  
      # print (len(x))   
      
      # for t in range(len(x)):
      #       # print (file)
      #       print (x[t])
      #       k = mask_rcnn(x[t],args["mask_rcnn"],args["visualize"],args["confidence"],args["threshold"])
      #       if len(k)!=0:
      #             cv2.imwrite(os.path.join(file[i],"%010d-fseg.png"%(t+1)),k[0])