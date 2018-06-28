import random
import numpy as np

# v: vector to check, solution: 기준 vector, radius: the thresolds
def check_in(v, radius, solution):
    v = np.array(v)
    s = np.array(solution)
    res = (v-s)**2
    # print(v.shape)
    # print(s.shape)
    c = res < radius**2
    if c.all():
        return True
    else:
        return False


d = int(input('dimension: '))
r = int(input('radius: '))

s = []
for i in range(d):
    x = random.randint(0, 10)
    s.append(x)

t = []
for i in range(10):
    g = []
    for j in range(d):
        y = random.randint(0, 20)
        g.append(y)
    t.append(g)

print('sol: ', s)
for i in range(10):
    print('v: ', t[i])
    print(check_in(t[i], r, s, d))
