import os
import sys
import lmdb
import numpy as np
from PIL import Image
from os import walk
import caffe
import cv2

##def main():
##  mypath = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_orig/'
##  path_dst = '/home/reza_rec/crfasrnn/caffe/examples/Gambier'
##  path_src = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_orig/'
##  
##  src_imgs = []
##  for (dirpath, dirnames, filenames) in walk(mypath):
##    src_imgs.extend(filenames)
##
##  convert2lmdb(path_src, src_imgs, path_dst)
##
##  
SIZE = 512

with open( 'data.txt', 'r' ) as T :
    lines = T.readlines()
lines = [line.rstrip('\n') for line in lines]

Data = np.zeros( (len(lines), 3, SIZE, SIZE), dtype='uint8' )
Label = np.zeros( (len(lines), 1, SIZE, SIZE), dtype='uint8' ) 

for i,l in enumerate(lines):
    sp = l.split(' ')
    img_data = cv2.imread(sp[0])
    img_label = cv2.imread(sp[1])
    
    img_data = caffe.io.resize(img_data, (SIZE, SIZE, 3) ) # resize to fixed size
    img_label = caffe.io.resize(img_label, (SIZE, SIZE, 1))
    
    transposed_img_label = img_label.transpose((2,0,1))[::-1,:,:] # RGB->BGR
    transposed_img_data = img_data.transpose((2,0,1))#[::-1,:,:]
    
    Data[i] =transposed_ img_data
    Label[i] = transposed_img_label

def convert2lmdb(path_src, src_imgs, path_dst):

  db = lmdb.open(path_dst, map_size=int(1e12))

  with db.begin(write=True) as in_txn:
    for idx, img_name in enumerate(src_imgs):
      #img = np.array(Image.open(os.path.join(path_src + img_name)))
      #img = img.astype(np.uint8)
      #print(np.shape(img))
      #img = np.array(img)[np.newaxis]
      #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
      #img = img[:,:,::-1]
      #img = np.resize(img, [3, 512, 512])
      #print(np.shape(img))
      #img = img.transpose((2,0,1))
      img_dat = caffe.io.array_to_datum(img)
      in_txn.put(('{:0>10d}'.format(idx)).encode(), img_dat.SerializeToString())
  db.close()





if __name__ == '__main__':
  main()

