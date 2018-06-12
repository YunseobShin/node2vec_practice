import networkx as nx
from node2vec import Node2Vec
import numpy as np

def make_graph(filename):
    with open(filename, 'r') as data:
        edges = []
        for line in data:
            t = tuple(line.split(','))
            edges.append(t)

    graph = nx.DiGraph(edges)
    return graph

def main():
    # Create a graph
    # graph = nx.fast_gnp_random_graph(n=100, p=0.5)
    graph = make_graph('BlogCatalog/data/edges.csv')
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
    model.wv.save_word2vec_format('ex_output')

    # Save model for later use
    model.save('ex_model')



main()
