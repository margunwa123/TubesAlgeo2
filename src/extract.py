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
import similarity as sim

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
        print ('Mengekstrak fitur dari bapak/ibu %s' % f)
        name = f.split('/')[-1].lower()
        #setiap image fiturnya(vektornya) diekstrak
        result[name] = extract_features(f)
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)

def sort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
#bubble sort yang paling nilainya paling gede dibelakang

def sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] < arr[j+1][1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
#bubble sort yang paling nilainya paling kecil dibelakang

def closest_match_euc(img, maxel):
    with open("features.pck", 'rb') as fp:
        data = pickle.load(fp)
        matrix = []
        for i in data.items():
            matrix.append(i) 
        # isi dari matrix adl [ ['filename',[1,2,3,...,255] ], ['file2',[123,45,255,...,212]], .... ]
        # matrix[i][0] menghasilkan path, matrix[i][1] menghasilkan vektor
        features = extract_features(img) 
        pnd = []
        #pnd adalah path and distances, isinya [['filename',distance], ['filename2',542], ....]
        for f in matrix:  #f merepresentasikan matrix[i]
            A = sim.euclidean_distance(features, f[1])
            if(len(pnd) < maxel):
                pnd.append([f[0], A])
                sort1(pnd)
            elif(A < pnd[maxel-1][1]):
                pnd.pop(maxel-1)
                pnd.append([f[0], A])
                sort1(pnd)
        return pnd

def closest_match_cosine(img, maxel):
    with open("features.pck", 'rb') as fp:
        data = pickle.load(fp)
        matrix = []
        for i in data.items():
            matrix.append(i)
        features = extract_features(img)
        pnc = []
        for f in matrix:
            A = sim.cos_similarity(features, f[1])
            if(len(pnc) < maxel):
                pnc.append([f[0], A])
                sort2(pnc)
            elif(A > pnc[maxel-1][1]):
                pnc.pop(maxel-1)
                pnc.append([f[0], A])
                sort2(pnc)
        return pnc
