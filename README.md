# Medical-Imaging
This repository contains my work on semantic segmentation for thyroid ultrasound images

I have created a multi class segmentation dataset like Pascal-VOC for this data.
http://cimalab.intec.co/?lang=en&mod=project&id=31

I have used FCN8 architecture to build a model currently am in a process to tweaking my model. 

data description:
Its a 4 class segmentation dataset 
classes are:
 1. Benign
 2. Malign_TIRADS_4a (tumor with less harmful)
 3. Malign_TIRADS_4a (tumor with some harmful cells)
 4. Malign_TIRADS_4a (tumor with harmful cells)
 
 the data set contains two folders 
 1. jpg images
 2. Segmentation images
 
 and two csv files one for train data and another for valid data.
 
 link of the dataset in my drive is 
you can access my dataset here 
https://drive.google.com/open?id=1gYe8UI_-9yUC5qHKwyuVmEqwP1qtdNoK

thanks to wkentaro for his wonderful package labelme
https://github.com/wkentaro/labelme
I created my dataset using his library. 
