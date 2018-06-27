import time
from time_check import tic
from time_check import toc
import json
import numpy as np
from numpy import array
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean as dis
import multiprocessing
# from multiprocessing import Pool
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def get_treshold(vecs, dim, length):
    std_vec = []
    for i in range(dim):
        # print(vecs[:,i])
        # mean_vec.append(np.mean(vecs[:,i]))
        std_vec.append(np.std(vecs[:,i]))

    return array(std_vec)/2

def get_distances(x, V):
    print(x)
    res = []
    for v in V:
        print(dis(x, v))
        res.append(dis(x, v))
    return res

def vec_to_node(vecs, threshold, length, pool_size):
    print('vec_to_node')
    chunks = np.array_split(vecs, pool_size)
    # print(chunks)
    #vecs: length * dim, thresolds: dim * 1
    with poolcontext(processes = pool_size) as pool:
        for i in range(length):
            res = pool.map(partial(get_distances, x=vecs[i]), chunks)

    links = array([])


    # for i in range(length):
    #     v = vecs[i,:]
    #     neighbors = where(dis(, threshold))



if __name__ == '__main__':
    pool_size = int(input('Enter the pool size: '))
    tic()
    with open('embeddings.json', 'r') as em:
        vec = json.load(em)
        size = len(vec)
        dim = 64
        vecs = array(list(vec.values()))
        # vec_to_node(vecs, 4)
    length = vecs.shape[0]
    thresholds = get_treshold(vecs, dim, length)
    vec_to_node(vecs, dim, length, pool_size)


    toc()








# def shilouette(vecs, k):
    #sil_scores=[]
    # for k in range(5, 21):
    #     print('clustering...')
    #     tic()
    #     kmeans = KMeans(n_clusters = k, random_state=0).fit(vecs)
    #     labels = kmeans.labels_
    #     toc()
    #     print('Calculating Silhouette score...')
    #     sil_score = silhouette_score(vecs, labels)
    #
    #     print(sil_score)
    #     sil_scores.append(sil_score)
    # with open('sil_scores.txt', 'w') as sil:
    #     sil.write(sil_scores)





###################
