import cv2

def show_img(path,winname):
    img = cv2.imread(path)
    cv2.imshow(winname,img)

def show_batch_img(img_arr):
    count = 0
    for i in img_arr:
        if count == 0:
            winname = 'Query Image'
        else:
            winname = 'Result Image' + str(count)
        show_img(i,winname)
        count += 1
    cv2.waitKey()
