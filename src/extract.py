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
import scipy

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

def closest_match_euc(img):
    with open("features.pck",'rb') as fp:
        data = pickle.load(fp)
        matrix = []
        for i in data.items():
            matrix.append(i)
        #matrix = np.array(matrix)
        print("matrix:",matrix[2][1])
        features = extract_features(img)
        print("features:",features)
        print(sim.cos_similarity(matrix[2][1],features))
        print(sim.euclidean_distance(matrix[2][1],features))
        mindist = sim.euclidean_distance(features,matrix[2][1])
        print("mindist 1",mindist)
        path = matrix[0][0]
        print(path)
        i = 0
        for f in matrix:
            A = sim.euclidean_distance(features,f[1])
            if A < mindist:
                mindist = A
                path = f[0]
            i += 1
        return path

def closest_match_cosine(img):
    with open("features.pck",'rb') as fp:
        data = pickle.load(fp)
        matrix = []
        for i in data.items():
            matrix.append(i)
        matrix = np.array(matrix)
        
        features = extract_features(img)
        mindist = sim.cos_similarity(features,matrix[0])
        path = matrix[0]
        for f in matrix:
            A = sim.cos_similarity(features,f)
            if A < mindist:
                mindist = A
                path = f
        return path

"""
class Matcher(object):
    def __init__(self, pickled_db_path="features.pck"):
        with open(pickled_db_path) as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.iteritems():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        v = vector.reshape(1, -1)
        print("matrix pertama: "+ self.matrix[0])
        print("name pertama: "+ self.names[0])
        print("cos cdist:" + scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1))
        return scipy.spatial.distance.cdist(self.matrix, v, 'cosine').reshape(-1) #ini tuh udah bentuk array

    def match(self, image_path, topn=5):
        features = extract_features(image_path)
        img_distances = self.cos_cdist(features)
        print("Img distance:" + img_distances)
        nearest_ids = np.argsort(img_distances)[:topn].tolist() #buat ngesort cdist paling gede lalu dimasukin ke list
        nearest_img_paths = self.names[nearest_ids].tolist() #buat ngedapetin nama path
        return nearest_img_paths, img_distances[nearest_ids].tolist()
"""