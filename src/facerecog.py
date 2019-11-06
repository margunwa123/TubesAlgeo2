import cv2
import similarity
import extract
import img
def run(img):
    # a = int(input("Berapa banyak image mirip yang ingin dikeluarkan: "))
    # extract.batch_extractor("..\\img\\")
    # image = img.get_random_img()
    # paths = extract.closest_match_cosine(img,5)
    paths = extract.closest_match_euc(img,5)
    #img.show_img(path,"Query Image")
    #print(path)
    img.show_batch_img(paths)
    cv2.waitKey()