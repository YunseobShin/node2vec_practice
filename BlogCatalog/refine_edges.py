with open('data/edges.csv', 'r') as f:
    g = open('edges.txt', 'w')

    for line in f:
        line = line.replace('\n', ',1\n')
        a = line.split(',')
        b = ' '.join(a)
        g.write(b)

    g.close()
