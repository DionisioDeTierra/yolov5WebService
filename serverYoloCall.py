import os
import torch
import json
import numpy as np

model = {}

def loadModel():
    global model 
    model = torch.hub.load(os.getcwd()+'/yolov5','custom', path=os.getcwd()+'./yolov5/runs/train/detectFire5/weights/best.pt',source='local', force_reload=True)
    print('Model is loaded once, on first request')
    
#     yolov5Model = model

def predictForImageName(image):
    results = model("./dataset/test/images/"+image)
    jsonData = []
    if results.xyxyn[0].shape[0] < 1:
        return( '{}', 200)        
    for result in results.xyxyn:
        flatResult = np.array(result).flatten()
        jsonData.append({'class': int(flatResult[5]), 'threshold': round(float(flatResult[4]),2), 'coordinates': flatResult[0:4].astype(float).tolist()})
    return( json.dumps(jsonData), 200)    


def predictForImage(imageRaw):
    print("1234")