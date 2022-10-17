# Custom objects recognition using Yolov5

This Repository is designed for beginners, who never worked with Yolov5 and want to implement the full process of object detection for their own classes and dataset

## What you will learn here:

- setup YoloV5 so that it later can be started on both your machine or container
- define recognition classes
- prepare dataset and annotate classes
- train model
- understand how to use trained model in server environment
- start web server and get prediction results for your image sent via web request (Postman or anything else)

## Step by Step Manual

- [Part 1: Dataset preparation](./docs/datasetPrepatation.md)
- [Part 2: YOLO v5 setup and train the model](./docs/YOLOv5SetupAndTrain.md)
- [Part 3: Setup Flask Web Server for YOLOv5](./docs/SetupWebServerForYolo.md)

## Main Challenges for Beginners

- Dataset may already not be available
- Annotation tools may not be available
- For starting Server Instance (to consume pretrained model on web), more than 4Gb Container Space is required.
  In the end, the service may need less than 4 Gb, but the disk space has to be more, during libraries download and unpackaging.
  As the only available container had limit of 4 Gb, I could not find out more details here.
  There are not free python server hosts on web proposing more than half of Gb Storage.
  So the easiest option I will use here is to start a local Flask Server
