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
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def get_treshold(vecs):
    mu = float(input('Enter the threshold hyperparameter mu: '))
    sample = vecs[np.random.choice(vecs.shape[0], 500, replace=False), :]
    distances = []
    len = sample.shape[1]
    for i in range(len):
        for j in range(len):
            distances.append(dis(sample[i], sample[j]))
    res = np.mean(array(distances))
    print('The average distance of sample: ', res)
    res /= mu
    return res

def check_link(v, s, threshold):
    res = dis(v, s) < np.sqrt(threshold)
    if res.all():
        return True
    else:
        return False

def parallel_check_link(vecs, v, v_id, threshold):
# def parallel_check_link(vecs, **kwargs):
    # print('#####################parallel check#####################')
    # print(vecs)
    g = open('new_graph', 'a')
    for i in range(vecs.shape[0]):
        if np.array_equal(v, vecs[i]):
            continue
        if check_link(v, vecs[i], threshold):
            # print(str(v_id+1)+' '+ str(i+1))
            g.write(str(v_id+1)+' '+ str(i+1)+'\n')
    g.close()

def split_vecs(vecs, pool_size):
    length = vecs.shape[0]
    size = length // pool_size
    margin = length % pool_size
    s = 0
    t = size
    res = []
    for i in range(pool_size-1):
        res.append(vecs[s:t])
        s += size
        t += size
    res.append(vecs[s:length])
    return res

def vec_to_node(vecs, threshold, length, pool_size=1):
    print('vec_to_node')
    chunks = split_vecs(vecs, pool_size)
    #vecs: length * dim, thresolds: dim * 1
    # print(chunks)
    print(array(chunks).shape)
    # print(chunks)

    links = []
    print('converting vectors back into a graph...')
    tic()
    for i in range(length):
        # print('node #' + str(i+1))
        with poolcontext(processes=pool_size) as pool:
            pool.map(partial(parallel_check_link, v = vecs[i], v_id = i, threshold = threshold), chunks)
        if i % 10 == 0 :
            print(str(i)+'/'+str(length))
            toc()
            tic()
    # g = open('new_graph', 'a')
    # for i in range(length):
    #     for j in range(length):
    #         if np.array_equal(vecs[i], vecs[j]):
    #             continue
    #         if check_link(vecs[i], vecs[j], threshold):
    #             g.write(str(i+1)+' '+ str(j+1)+'\n')
    #             # links.append((i+1, j+1))
    #     if i % 200 == 0 :
    #         print(str(i)+'/'+str(length))
    #         toc()
    #         tic()
    #
    # g.close()

    # print('saving a new graph...')
    # with open('new_graph.txt', 'w') as g:
    #     g.write(links)


if __name__ == '__main__':
    pool_size = int(input('Enter the pool size: '))
    print('You are using', pool_size, 'processesors in', multiprocessing.cpo_count(), 'processesors.')
    tic()
    g = open('new_graph', 'w')
    with open('embeddings.json', 'r') as em:
        vec = json.load(em)
        vecs = array(list(vec.values()))
        # vec_to_node(vecs, 4)
    length = vecs.shape[0]
    threshold = get_treshold(vecs)
    print('the distance thresold:', threshold)
    vec_to_node(vecs, threshold, length, pool_size)


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
