import time
from time_check import tic
from time_check import toc
import json
import numpy as np
from numpy import where
from numpy import array
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from multiprocessing import Pool

def vec_to_node(vecs,  threshold):
    vecs

def shilouette(vecs, k):
    #sil_scores=[]
    # for k in range(5, 21):
    #     print('clustering...')
    #     tic()
    #     kmeans = KMeans(n_clusters = k, random_state=0).fit(vals)
    #     labels = kmeans.labels_
    #     toc()
    #     print('Calculating Silhouette score...')
    #     sil_score = silhouette_score(vals, labels)
    #
    #     print(sil_score)
    #     sil_scores.append(sil_score)
    # with open('sil_scores.txt', 'w') as sil:
    #     sil.write(sil_scores)

def main():
    tic()
    with open('embeddings.json', 'r') as em:
        vec = json.load(em)
        size = len(vec)
        dim = 64
        vals = np.array(list(vec.values()))
        vec_to_node(vals, 4)
    toc()


main()
