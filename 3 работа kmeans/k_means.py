import numpy as np



def euclidean_distance(A, B):
   
    V = A - B
    r = np.sqrt(np.sum(np.power(V, 2)))
    return r

def class_of_each_point(X, centers):
    m = len(X)
    k = len(centers)

    distances = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            distances[i, j] = dist(centers[j], X[i])

    return np.argmin(distances, axis=1)


def kmeans(k, X):
   
    m, n = X.shape

    curr_iteration = prev_iteration = np.zeros(m)

   
    centers = np.random.random((k, n))
    
    centers = centers * (np.max(X, axis=0) - np.min(X, axis=0)) + np.min(X, axis=0)

    curr_iteration = class_of_each_point(X, centers)

    while True:

        prev_iteration = curr_iteration

        for i in range(k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = np.mean(sub_X, axis=0)
       
        curr_iteration = class_of_each_point(X, centers)     
        if np.all(prev_iteration == curr_iteration):
            break

    return centers
