import similarity
import extract
import img
import cv2

image = "../img/cindy.jpg"
path = extract.closest_match_euc(image)
img.show_img(image,"Query Image")
print(path)
img.show_batch_img(path)
cv2.waitKey()