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
