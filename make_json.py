import json
import time
from time_check import tic
from time_check import toc

tic()
with open('embeddings2.txt', 'r') as f:
    dic = {}
    f.readline()
    d = 64
    for line in f:
        if len(line) == 0:
            continue
        if len(line) < 10:
            node_id = int(line.split()[0])
        else:
            sl = line.split(' ')
            if len(sl) < 2:
                node_id = sl
            else:
                ebd = sl
                ebd[-1] = ebd[-1].replace('\n', '')
                embedding = [float(x) for x in ebd[1:]]
                dic[int(node_id)] = embedding
                # print('[node]: ', node_id)
                # print('[ebd]: ', embedding[0:3], len(embedding))

        # if i % 2 == 0: # node_id
        #     print(i)
        #     print('@@: ',line)
        #     node_id = int(line.split()[0])
        # else:   # embedding
        #     ebd = line.split(' ')
        #     ebd[-1] = ebd[-1].replace('\n', '')
        #     print('##: ', ebd[1:])
        #     embedding = [float(x) for x in ebd[1:]]
        #     dic[node_id] = embedding
        # i += 1
    with open('embeddings.json', 'w') as g:
        print(len(dic))
        json.dump(dic, g)
toc()
