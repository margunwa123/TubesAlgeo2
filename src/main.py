import similarity
import extract
import img
import cv2

path = extract.closest_match_euc("../img/Aaron Paul0_262.jpg")
print(path)
img.show_batch_img(path)
cv2.waitKey()