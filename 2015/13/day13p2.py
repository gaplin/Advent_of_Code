from itertools import permutations

input = open('input2.txt').read().splitlines()

happiness = {}
nodes = set()
for line in input:
    line = line.split(' ')
    u, v = line[0], line[-1][:-1]
    hap_value = int(line[3])
    if line[2] == 'lose':
        hap_value *= -1

    for node in [u, v]:
        if node not in happiness:
            happiness[node] = {}
    
    happiness[u][v] = hap_value
    nodes.add(u)
me = 'me'
happiness[me] = {v: 0 for v in nodes}
for v in nodes:
    happiness[v][me] = 0
nodes.add(me)


first_one = nodes.pop()
n = len(nodes)
change = 0
for arr in permutations(nodes):
    happ = happiness[arr[0]][first_one] + happiness[first_one][arr[0]] + happiness[first_one][arr[-1]] + happiness[arr[-1]][first_one]
    for i in range(1, n):
        happ += happiness[arr[i]][arr[i - 1]] + happiness[arr[i - 1]][arr[i]]
    change = max(change, happ)

print(change)