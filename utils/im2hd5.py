import h5py, os
import caffe
import numpy as np
from PIL import Image
import cv2

SIZE = 512

with open( '../data/datalist.txt', 'r' ) as T :
    lines = T.readlines()
lines = [line.rstrip('\n') for line in lines]

Data = np.zeros( (len(lines), 3, SIZE, SIZE), dtype='f4' )
Label = np.zeros( (len(lines), 1, SIZE, SIZE), dtype='f4' ) 

for i,l in enumerate(lines):
    sp = l.split(' ')
    img_data = cv2.imread(sp[0])
    img_label = cv2.imread(sp[1])
    
    img_data = caffe.io.resize(img_data, (SIZE, SIZE, 3) ) # resize to fixed size
    img_label = caffe.io.resize(img_label, (SIZE, SIZE, 1))
    
    transposed_img_label = img_label.transpose((2,0,1))[::-1,:,:] # RGB->BGR
    transposed_img_data = img_data.transpose((2,0,1))#[::-1,:,:]
    
    Data[i] =transposed_img_data
    Label[i] = transposed_img_label
   
with h5py.File('traindb.h5','w') as H:
    H.create_dataset( 'Data', data = Data) # note the name X given to the dataset!
    H.create_dataset( 'Label', data = Label )
with open('traindb_h5_list.txt','w') as L:
    L.write( 'traindb.h5' ) # list all h5 files you are going to use

