import os
import random
import cv2

def show_img(path,winname):
    img = cv2.imread(path)
    cv2.imshow(winname, img)

def show_batch_img(img_arr):
    count = 0
    for i in img_arr:
        winname = 'Result Image ' + str(count+1)
        i[0] = "..\\" + i[0]
        show_img(i[0],winname)
        count += 1
    cv2.waitKey()


def get_random_img():
    images_path = "..\\img\\"
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    sample = random.sample(files,1)
    return sample[0]
