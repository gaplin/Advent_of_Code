from itertools import permutations

input = open('input2.txt').read().splitlines()

G = {}
nodes = set()
for line in input:
    line = line.split(' ')
    u, v, distance = line[0], line[2], int(line[-1])
    if u not in G:
        G[u] = {}
    if v not in G:
        G[v] = {}

    G[u][v] = distance
    G[v][u] = distance
    nodes.add(u)
    nodes.add(v)

max_value = -1
n = len(nodes)
for candidate in permutations(nodes):
    length = 0
    for i in range(1, n):
        length += G[candidate[i - 1]][candidate[i]]

    max_value = max(max_value, length)

print(max_value)
    