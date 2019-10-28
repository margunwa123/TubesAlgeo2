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
import random
import os
import cv2
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy import spatial

# 1. Feature Detection and Description
def extract_features(img_path, vector_size=32):
    
    img = cv2.imread(img_path, 1)

    try:

        # ORB mendeteksi fitur" dari gambar untuk mendeteksi kesamaan 2 gambar
        # berdasarkan sebuah analisis dari researchgate.net, ORB merupakan algoritma untuk mendapatkan keypoint paling akurat
        detectorb = cv2.ORB_create()
        # menyimpan keypoints dari gambar ke variabel keypoint
        keypoints = detectorb.detect(img)
        
        # Sorting them based on keypoint response value(bigger is better)

        keypoints = sorted(keypoints, key=lambda x: -x.response)[:vector_size]

        # computing descriptors vector

        keypoints, dsc = detectorb.compute(img, keypoints)
        # Flatten all of them in one big vector - our feature vector

        dsc = dsc.flatten()

        # Making descriptor of same size

        # Descriptor vector size is 64

        needed_size = (vector_size * 64)

        if dsc.size < needed_size:

            # if we have less the 32 descriptors then just adding zeros at the

            # end of our feature vector

            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])

    except cv2.error as e:

        print ('Error: ', e)

        return None

    return dsc





def batch_extractor(imgs_path, pickled_db_path="features.pck"):

    # Megekstraksikan image dlm imgs path ke array files
    files = [os.path.join(imgs_path, p) for p in sorted(os.listdir(imgs_path))]

    result = {}

    for f in files:
        print ('Extracting features from img %s' % f)
        name = f.split('/')[-1].lower()
        #setiap image fiturnya(vektornya) diekstrak
        result[name] = extract_features(f)

    # saving all our feature vectors in pickled file

    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)


class Matcher():

    def __init__(self, pickled_db_path="features.pck"):

        with open(pickled_db_path, 'rb') as fp:
            
            self.data = pickle.load(fp)

        self.names = []

        self.matrix = []

        for k, v in self.data.items():

            self.names.append(k)

            self.matrix.append(v)

        self.matrix = np.array(self.matrix)

        self.names = np.array(self.names)



    def cos_dist(self, vector):
        
        #mendapatkan jarak kosinus antara img dan database imgs
        #-1 disini berarti elemen yang diperlukan numpy untuk mereshape arraynya
        v = vector.reshape(1, -1)
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1)


    def match(self, img_path, topn=5):

        features = extract_features(img_path)

        img_distances = self.cos_dist(features)

        # getting top 5 records

        nearest_ids = np.argsort(img_distances)[:topn].tolist()

        nearest_img_paths = self.names[nearest_ids].tolist()



        return nearest_img_paths, img_distances[nearest_ids].tolist()
    
    
def show_img(path):
    # Membaca gambar dari path
    img = cv2.imread(path, 1)
    plt.imshow(img)
    # Menunjukan gambar ke user
    plt.show()

    


def run():

    images_path = '../img/'

    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    # getting 3 random images 

    sample = random.sample(files, 1)
    strsample = ''.join(sample) #ini untuk ngebuat array jd string

    # batch_extractor(images_path)

    ma = Matcher('features.pck')

    print ('Query image ==========================================')

    show_img(strsample)

    names, match = ma.match(strsample, topn=4)

    print ('Result images ========================================')

    for i in range(3):

        # we got cosine distance, less cosine distance between vectors

        # more they similar, thus we subtruct it from 1 to get match value

        print ('Match %s' % (1-match[i]))

        show_img(os.path.join(images_path, names[i+1]))



run()