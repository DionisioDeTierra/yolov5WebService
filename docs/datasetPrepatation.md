## Part 1: Dataset Preparation

## YOLO v5 Dataset Requirements

Yolo v5 requires dataset to be splitted into folders:

- train
- valid
- test (optional)

Inside of each folder (except the test one), data has to be splitted into subfolders:

- images
  - Place here all your images (jpg, jpeg, png or other yolov5 supported format)
- labels

  - a list of .txt files, with same name as the image.
    On each new line every found class id and coordinates are indicated. Example:

```
        0 0.7203900480263002 0.5613704815146779 0.36335113328316737 0.3485424760512498
```

## Options to prepare and annotate dataset

1. Take all images you need and put them at some folder in your PC.
2. Annotate the images. Here I know about following options:
   - [VGG Image Annotator](https://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html?ref=hackernoon.com) - this was my choice.
     Upload there all my images via Menu "Image"-"Load or Add Images", then labelled them, then used Menu "Annotation"-"Save as JSON".
     You can also label just some part of images and save the annotation. Then, at next start, after you added images, you have to use Menu "Annotation"-"Import" to recover your annotation
   - [LabelImg](https://pypi.org/project/labelImg). It is quite popular and known, but I could not use it, as it requires Visual Studio Build Tools, which needs a proper license.
   - Any other Image Annotation Tool, like "LabelMe", "Scalable", "RectLabel", etc.

## Convert data to YOLOv5 format:

- In my case I uploaded Use [Roboflow web service](https://app.roboflow.com) to annotate (free for up to 1000 images dataset). When you finished the annotations, in the last step, you can select "Export" -> "YOLO v5 PyTorch", which will deliver you the dataset in required format. You will only need to unzip it to correct place.

- If you do not want to use Roboflow, there are still a lot of options to transform your annotations to YOLOv5 format. There are plenty of python scripts examples which can do it. Just ensure your data is prepared as indicated in Section "YOLO v5 Dataset Requirements"

<br />
<br />

# IMPORTANT

## If you do not have data prepared, but want to test the whole process, take fully prepared [Kaggle Dataset (Fire Detection) of 16Mb](https://www.kaggle.com/datasets/ankan1998/fire-detection-in-yolo-format)

With the time, some datasets can be not available. Then search for any other Kaggle dataset, which has content according to Section "Dataset requirements"
