## Prerequisites:

- Installed Python version as indicated on [yolov5 repository](https://github.com/ultralytics/yolov5)
- Installed virtualenv: python3 -m pip install --user virtualenv
- Dataset is prepared and is located in the folder "dataset" under root folder.
- data.yaml is created in the dataset folder and looks like that (below example for Fire Detection dataset from Kaggle):

```
train: ../../dataset/train/images
val: ../../dataset/valid/images

nc: 1
names: ['fire']
```

### Explanation:

train - path to train images,
val - path to validation images
nc - number of classes
names - array of class names
<br/>
<br/>

## Setup Yolo model:

In the root folder of this project, execute terminal commands in given order:

```
git clone https://github.com/ultralytics/yolov5.git
virtualenv yoloEnv (so that yolo is executed in the own python container, to avoid inconsistencies between python libraries in yolo folder and your current libraries)
yoloEnv/Scripts/activate (this command has to be repeated everytime, you reopen this project)
```

If this command was successful, there should be a new terminal line with prefix "(yoloEnv)")
Only if you have this prefix, execute this terminal command:

```
pip install -r yolov5/requirements.txt
```

## Train yolo model

After the yoloEnv was activated in the terminal, run this script from the root folder:

```
python yolov5/train.py --img 640 --cfg yolov5s.yaml --batch 32 --epochs 150 --data ../dataset/data.yaml --weights yolov5s.pt --workers 24 --name detectFire
```

### Important:

- model training can take quite a lot of time, depending on your pc. On my laptop, it took around (Started around 15:10)
- it is very important, that you get informed about all parameters used here as they can be crucial to build successful model

### Short notes:

For successful training, parameter mAP50 should grow slowly( though can degrade in some epocs), and in the end should be higher as 0.70,
optimally even higher as 0.90

You can increase epocs to be much bigger, once the model recognizes, there is no growth anymore, it will abort training on its own.

## Test yolo model
