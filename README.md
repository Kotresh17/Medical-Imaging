# Medical-Imaging
This repository contains my work on semantic segmentation for thyroid ultrasound images

I have created a multi class segmentation dataset like Pascal-VOC for this data.
http://cimalab.intec.co/?lang=en&mod=project&id=31

I have used FCN8 architecture to build a model currently am in a process to tweaking my model. 

data description:
Its a 4 class segmentation dataset 
classes are:
 1. Benign
 <p align="center">
  <img width="460" height="300" src="https://github.com/Kotresh17/Medical-Imaging/blob/master/images/2_1.jpg?raw=true">
</p>
 2. Malign_TIRADS_4a (tumor with less harmful)
 <p align="center">
  <img width="460" height="300" src="https://github.com/Kotresh17/Medical-Imaging/blob/master/images/3_1.jpg?raw=true">
</p>
 3. Malign_TIRADS_4b (tumor with some harmful cells)
 <p align="center">
  <img width="460" height="300" src="https://github.com/Kotresh17/Medical-Imaging/blob/master/images/10_1.jpg?raw=true">
</p>
 4. Malign_TIRADS_5 (tumor with harmful cells)
 <p align="center">
  <img width="460" height="300" src="https://github.com/Kotresh17/Medical-Imaging/blob/master/images/29_1.jpg?raw=true">
</p>
 the data set contains two folders 
 1. jpg images
 2. Segmentation images
 
 and two csv files one for train data and another for valid data.
 

thanks to wkentaro for his wonderful package labelme
https://github.com/wkentaro/labelme
I created my dataset using his library. a 
