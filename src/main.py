import cv2
import similarity
import extract
import img

a = int(input("Berapa banyak image mirip yang ingin dikeluarkan: "))
# extract.batch_extractor("..\\img\\")
image = img.get_random_img()
path = extract.closest_match_cosine(image,a)
img.show_img(image,"Query Image")
print(path)
img.show_batch_img(path)
cv2.waitKey()