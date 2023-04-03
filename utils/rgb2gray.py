import cv2
import os
from PIL import Image
import glob

def main():

path = '/home/reza_rec/crfasrnn/cafee/examples/Gambier/gamb_gt/'
dst = '/home/reza_rec/crfasrnn/cafee/examples/Gambier/data'

images = load_images(path)
rgb2gray(images, dst)


def load_images(path):
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def rgb2gray(images, path)
    for image in iamges
        img = Image.open(image).convert('LA')
        img.save(image, path)


