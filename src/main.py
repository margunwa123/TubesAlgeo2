import similarity
import extract
import img
import cv2

path = extract.closest_match_euc("../img/Aaron Paul0_262.jpg")
print(path)
path2 = "..\\" + path
img.show_img(path2,"hehe")
cv2.waitKey()
"""
v1 = extract.extract_features("../img/Aaron Paul0_262.jpg")
img.show_img("../img/Aaron Paul0_262.jpg",'first img')
v2 = extract.extract_features("../img/Aaron Paul0_262.jpg")
img.show_img("../img/Aaron Paul0_262.jpg",'second img')
#extract.batch_extractor("../img")
cv2.waitKey()
sim = similarity.cos_similarity(v1, v2)
$euc = similarity.euclidean_distance(v1, v2)
>>print(sim)
!print(euc)
"""