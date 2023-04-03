from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
     
mypath='/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_gt2/'
dst = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/gamb_gt/'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )

grays = []
for i in range(0, len(onlyfiles)):
    grays.append(cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY))
    #grays[i] = grays[i][np.newaxis,np.newaxis, ...]
    cv2.imwrite(dst + 'gt_' + str(i).zfill(4) + '.png', grays[i])

    
    
