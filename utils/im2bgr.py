import os
import sys
import glob
import numpy as np
from PIL import Image
from os import walk
import caffe
import cv2

def main():
    src_imgs = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_orig/'
    path_dst = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/input'
    path_src = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_orig/'

    convert2bgr(src_imgs, path_dst)

"""
    image_list = []
    for (dirpath, dirnames, filenames) in walk(src_imgs):
        image_list.extend(filenames)
"""
    
"""
def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images
"""
def convert2bgr(src_imgs, path_dst):

    #image_list = load_images(src_imgs)
    #image_list = []
    #for filename in glob.glob(src_imgs): 
        #img = Image.open(filename)
        #image_list.append(img)
    for filename in os.listdir(src_imgs):
        img = cv2.imread(os.path.join(src_imgs,filename))
        #img = img.transpose((2,0,1))
        #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.imwrite(os.path.join(path_dst, filename), img)
    #for idx, img_name in enumerate(image_list):
        #img = np.array(Image.open(os.path.join(src_imgs,img_name)))
        #print(np.shape(img))
        #img = cv2.imread(img_name)
        #img = img.astype(np.uint8)
        #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        #print(img.shape)
        #img = img.transpose((2,0,1))
        #print(img.shape)
        #cv2.imwrite(os.path.join(path_dst, img_name), img)
        #cv2.imwrite('gamb-' + str(idx).zfill(4) + '.png', img)
        #cv2.waitkey(0)
    

if __name__ == '__main__':
  main()
