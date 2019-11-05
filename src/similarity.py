import math

def euclidean_distance(x,y):
    #mendapatkan euclidean distance dari x dan y
    euc = 0
    for i in range(4096):
        temp = x[i] - y[i]
        euc += (temp**2)
    return math.sqrt(euc)

def pjg_vektor(x):
    pjg = 0
    for i in range (4096):
        pjg += x[i] ** 2 
    return math.sqrt(pjg)

def dotProduct(x,y):
    dot = 0
    for i in range(4096):
        dot += x[i] * y[i]
    return dot

def cos_similarity(x,y):
    px = pjg_vektor(x)
    py = pjg_vektor(y)
    return (dotProduct(x,y)/(px*py))
