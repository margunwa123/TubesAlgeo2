"""
Membandingkan 2 image, langkah2 men-register image
1. Feature Detection and Description
2. Feature Matching
3. Outlier Rejection
4. Derivation of Transformation Function
5. Image Reconstruction.
sumber:
https://www.researchgate.net/publication/323561586_A_comparative_analysis_of_SIFT_SURF_KAZE_AKAZE_ORB_and_BRISK
"""

# ! Menggunakan python version 3.7.4
import pickle
import os
import cv2
import numpy as np

# 1. Feature Detection and Description
def extract_features(img_path, vector_size=64):
# Mengekstrak fitur- fitur dari image dan memasukannya dalam bentuk vektor
    img = cv2.imread(img_path)
    try:
        detAkaze = cv2.AKAZE_create()
        keypoints = detAkaze.detect(img)
        keypoints = sorted(keypoints, key=lambda x: -x.response)[:vector_size]
        keypoints, dsc = detAkaze.compute(img, keypoints)
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None
    return dsc

def batch_extractor(imgs_path, pickled_db_path="features.pck"):
# Mengekstraksikan image dlm imgs path ke array files
    files = [os.path.join(imgs_path, p) for p in sorted(os.listdir(imgs_path))]
    result = {}
    for f in files:
        print ('Extracting features from img %s' % f)
        name = f.split('/')[-1].lower()
        #setiap image fiturnya(vektornya) diekstrak
        result[name] = extract_features(f)
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)
