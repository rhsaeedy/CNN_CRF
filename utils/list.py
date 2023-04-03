import glob
import os
from os import walk

path = './bp/'
images = []

for (img_dirpath, img_dir, img_names) in walk(path):
    images.extend(img_names)

images = sorted(images)

l = len(images)

with open('{}/bp_test.txt'.format(path), 'w') as f:
    for e in range(0, l):
        f.write(images[e] + '\n')
