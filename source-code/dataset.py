from PIL import Image
import glob
import random
import torch
from torch.utils.data import Dataset
import torchvision.transforms.functional as TVF
import torch.optim as optim
import numpy as np
import pandas as pd
import collections
import os
import PIL.Image

CLASS_NAMES = ['_background_', 'Benign','Malign_TIRADS_4a','Malign_TIRADS_4b','Malign_TIRADS_5']
COLOR_2_INDEX = np.asarray([[0, 0, 0],[128, 0, 0],[0, 128, 0],[128, 128, 0],[0, 0, 128]])


class ThyroidSeg(Dataset):
#    CLASS_NAMES = np.array(['_background_', 'Benign','Malign_TIRADS_4a','Malign_TIRADS_4b','Malign_TIRADS_5'])
    #mean_bgr = np.array([104.00698793, 116.66876762, 122.67891434])
#    COLOR_2_INDEX = np.asarray([[0, 0, 0],[128, 0, 0],[0, 128, 0],[128, 128, 0],[0, 0, 128]])
    
    def __init__(self, root_dir, split,img_size,device):
        self.root_dir = root_dir
#        self._transform = transform
        self.split = split
        self.img_size = img_size
        #self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.device = device
        self.files = collections.defaultdict(list)
        df = pd.read_csv(self.root_dir+'/'+split+'.csv')
        #print(df)
        for i in range(df.shape[0]):
            img_file = os.path.join(self.root_dir, 'JPEGImages/%s' %df.loc[i]['image_id'])
            lbl_file = os.path.join(self.root_dir, 'SegmentationClassPNG/%s.png' %df.loc[i]['image_id'][:-4])
            self.files[self.split].append({'img':img_file, 'lbl':lbl_file})
        #print(self.files[self.split])
    def __len__(self):
        return len(self.files[self.split])
    
    def create_label_mask(mask_img):
        mask = np.array(mask_img).astype(int)
        label_mask = np.zeros((mask.shape[0], mask.shape[1]), dtype=np.int16)

        for idx, label in enumerate(COLOR_2_INDEX):
            label_mask[np.where(np.all(mask == label, axis=-1))[:2]] = idx

        label_mask = label_mask.astype(int)
        return label_mask

    def load_imgs(self, index):
        self.data_file = self.files[self.split][index]
        img_file = self.data_file['img']

        img = PIL.Image.open(img_file)  
        img = img.resize((self.img_size, self.img_size))

        lbl_file = self.data_file['lbl']
        mask_img = PIL.Image.open(lbl_file)
        mask_img = mask_img.resize((self.img_size, self.img_size))
        
        return img, mask_img     
    
    def  __getitem__(self, index):
        #data_file = self.files[self.split][index]
        #img_file = data_file['img']
        #print(data_file, img_file)
        #load image
        #img = PIL.Image.open(img_file)
        #img = img.resize((self.img_size, self.img_size))
        #img = np.array(img, dtype=np.uint8)
        #load label
        #lbl_file = data_file['lbl']
        #mask_img = PIL.Image.open(lbl_file)
        #mask_img = mask_img.resize((self.img_size, self.img_size))
        img, mask_img = self.load_imgs(index)
        if random.random()>0.5:
            img = TVF.hflip(img)
            mask_img = TVF.hflip(mask_img)
        
        #mask_img = ThyroidSeg.create_label_mask(mask_img) 
        mask_img = np.array(mask_img).astype(int)
        mask_img = torch.from_numpy(mask_img).long()
        
        img = TVF.to_tensor(img)
        img = TVF.normalize(img,
                            mean=(0.485, 0.456, 0.406), 
                            std=(0.229, 0.224, 0.225)
                           )
        img = img.to(self.device)
        mask_img = mask_img.to(self.device)

        return (img, mask_img)

