import glob
import os
from os import walk

path = '/home/reza_rec/crfasrnn/caffe/examples/Gambier/data'
img_path = path + '/noisyRGB/'
label_path = path + '/gray/'

tmp_data = []
tmp_labels = []

for (img_dirpath, img_dir, img_names) in walk(img_path):
    tmp_data.extend(img_names)

for (label_dirpath, label_dir, label_names) in walk(label_path):
    tmp_labels.extend(label_names)

"""
DIR = '../Gambier/'
TXT_DIR = '../Gambier/'

orig_images = glob.glob(DIR + "gamb_orig/*.png")
gt_images = glob.glob(DIR + "gamb_gt/*.png")

sorted_orig_images = sorted(orig_images)
sorted_gt_images = sorted(gt_images)

orig_train = sorted_orig_images[:int(len(sorted_orig_images)*0.7)]
gt_train = sorted_gt_images[:int(len(sorted_gt_images)*0.7)]

orig_test = sorted_orig_images[int(len(sorted_orig_images)*0.7):]
gt_test = sorted_gt_images[int(len(sorted_gt_images)*0.7):]

l1 = len(orig_train)
l2 = len(orig_test)
"""
data = sorted(tmp_data)
labels = sorted(tmp_labels)

l1 = len(data)

with open('{}/datalist.txt'.format(path), 'w') as f:
    for e in range(0, l1):
        f.write(img_path + data[e] + ' ' + label_path + labels[e] + '\n')

##with open('{}/labels.txt'.format(path), 'w') as f:
##    for e in range(0, l1):
##        f.write(label_path + labels[e] + ' ' + str(0) +'\n')
