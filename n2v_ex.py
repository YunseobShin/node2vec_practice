import networkx as nx
from node2vec import Node2Vec
import numpy as np
import time
from time_check import tic
from time_check import toc

def make_graph(filename):
    with open(filename, 'r') as data:
        edges = []
        for line in data:
            t = tuple(line.split(','))
            edges.append(t)

    return nx.DiGraph(edges)

def train(filename):
    # Create a graph
    graph = make_graph(filename)
    print('number of nodes: ', nx.number_of_nodes(graph))
    # H=nx.DiGraph(G)   # create a DiGraph using the connections from G
    # H.edges()
    # edgelist=[(0,1),(1,2),(2,3)]
    # H=nx.Graph(edgelist)

    # Precompute probabilities and generate walks
    node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4)
    # Embed
    model = node2vec.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)
    # Look for most similar nodes
    model.wv.most_similar('2')  # Output node names are always strings
    # Save embeddings for later use
    model.wv.save('embeddings2.bin')

    # Save model for later use
    model.save('ex_model')

if __name__ == '__main__':
    tic()
    train('BlogCatalog/data/edges.csv')
    toc()
