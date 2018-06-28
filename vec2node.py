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
from multiprocessing import Pool
from contextlib import contextmanager
from functools import partial

@contextmanager
def poolcontext(*args, **kwargs):
    pool = Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def get_avg_distance(vecs, length):
    sample = np.random.chooice(vecs, 500, replace=False)
    distances = []
    for i in range(length):
        for j in range(length):



def get_treshold(vecs, dim, length):
    std_vec = []
    for i in range(dim):
        # print(vecs[:,i])
        # mean_vec.append(np.mean(vecs[:,i]))
        std_vec.append(np.std(vecs[:,i]))

    return np.mean(array(std_vec))

def check_link(v, s, threshold):
    res = (v-s)**2 < threshold**2
    if res.all():
        return True
    else:
        return False

def vec_to_node(vecs, threshold, length, pool_size=1):
    print('vec_to_node')
    # print(chunks)
    #vecs: length * dim, thresolds: dim * 1
    # chunks = np.array_split(vecs, pool_size)

    links = []
    print('converting vectors back into a graph...')
    g = open('new_graph', 'a')
    for i in range(length):
        for j in range(length):
            if np.array_equal(vecs[i], vecs[j]):
                continue
            is_linked = check_link(vecs[i], vecs[j], threshold)
            if is_linked:
                g.write(str(i+1)+' '+ str(j+1)+'\n')
                # links.append((i+1, j+1))
        if i % 10 == 0 :
            print(str(i)+'/'+str(length))
            toc()
            tic()

    g.close()
    # print('saving a new graph...')
    # with open('new_graph.txt', 'w') as g:
    #     g.write(links)


if __name__ == '__main__':
    # pool_size = int(input('Enter the pool size: '))
    tic()
    g = open('new_graph', 'w')
    with open('embeddings.json', 'r') as em:
        vec = json.load(em)
        size = len(vec)
        dim = 64
        vecs = array(list(vec.values()))
        # vec_to_node(vecs, 4)
    length = vecs.shape[0]
    thresholds = get_treshold(vecs, dim, length)
    vec_to_node(vecs, thresholds, length)


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
