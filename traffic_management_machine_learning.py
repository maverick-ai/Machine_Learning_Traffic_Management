from imageai.Detection import ObjectDetection
import os
import numpy as np
import cv2

execution_path = r"C:\Users\sbans\Desktop"
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


def car_detector(image_arr):
    c=0
    _, detections = detector.detectObjectsFromImage(input_type="array",input_image=image_arr, output_type="array", minimum_percentage_probability=70)
    for eachObject in detections:
        if eachObject["name"]=="car":
            c=c+1   
    return c
def load_image(lane_number):
    camera = cv2.VideoCapture(lane_number)
    _,image=camera.read()
    image_arr = np.asarray(image, dtype='float64')
    return image_arr
def populate_array_cars(array_cars):
    for i in range(len(array_cars)):
        image=load_image(i)
        array_cars[i]=car_detector(image)
n=4
time_alloted={0:0,1:0,2:0,3:0}
total_time=180
array_cars=[0,0,0,0]
prior=[[0,-1],[0,-1],[0,-1],[0,-1]]
is_lane=[1,1,1,1]
q=0
while(True):
    t_factor=0
    not_executing=-1
    t=total_time
    count=0
    populate_array_cars(array_cars) 
    for i in range(4):
        prior[i][0]=array_cars[i]
        prior[i][1]=i
    prior.sort()
    prior.reverse()
    for i in range(4):
        if is_lane[i]==1:
            t_factor=t_factor+array_cars[i]
    while(t):
        for i in range(4):
            if is_lane[prior[i][1]]==0:
               time_alloted[prior[i][1]]=0
            if is_lane[prior[i][1]]==1:
               time_alloted[prior[i][1]]=prior[i][0]*t/t_factor
               t_factor=t_factor-prior[i][0]
               t=t-time_alloted[prior[i][1]]
               count=count+1
               if t_factor==0:
                   t=0
            if count==4 and q==0:
                is_lane[prior[i][1]]=0
                not_executing=prior[i][1]
            elif count==3 and q!=0:
                is_lane[prior[i][1]]=0
                not_executing=prior[i][1]
    for i in range(4):
        if prior[i][1]!=not_executing:
            is_lane[prior[i][1]]=1
    for i in range(4):
        print("Time alloted for lane ",i, " :",time_alloted[i])
    print("Time Successfully assigned")
    q=q+1