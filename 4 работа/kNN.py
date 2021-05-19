import numpy as np
import math



def k_nearest(X, k, obj):
    Xn = X[:, 0:-1]
    Xnmean = np.mean(Xn, axis=0)
    Xnstd = np.std(Xn,axis=0)
   
    Xn = (Xn-Xnmean)/Xnstd
    objn = (obj-Xnmean)/Xnstd
    dist_arr =[dist(x, objn) for x in Xn]

    dist_arr =np.argsort(dist_arr)
    nearest_classes = X[dist_arr[:k], -1]
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]

    return object_class
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
