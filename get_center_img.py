# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image 

def pil_show_cropped_img(imgname):

    img = Image.open(imgname)  #open img
    plt.figure("time-frequence-figure")
    plt.subplot(1,2,1), plt.title('origin')
    plt.imshow(img),plt.axis('off')

    box=(135,63,923,748)
    roi=img.crop(box)

    plt.subplot(1,2,2), plt.title('center_cropped')
    plt.imshow(roi),plt.axis('off')
    plt.show()

def pil_cropped_center_img(root_dir, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for name in os.listdir(root_dir):
        if name == ".DS_Store":
            continue
        if not os.path.exists(os.path.join(save_dir, name)):
            os.mkdir(os.path.join(save_dir, name))
        img_dir = os.path.join(root_dir, name)
        for imgname in os.listdir(img_dir):
            if imgname == ".DS_Store":
                continue
            src = os.path.join(img_dir, imgname)
            dst = os.path.join(os.path.join(save_dir, name), imgname)
            img = Image.open(src)
            box=(135,63,923,748)
            roi=img.crop(box)
            roi.save(dst)

           


if __name__ == "__main__":
    # imgname = ""
    # pil_show_cropped_img(imgname)

    root_dir = ""
    save_dir = ""
    pil_cropped_center_img(root_dir, save_dir)