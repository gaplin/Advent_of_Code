from heapq import heappop, heappush

def get_all_molecules_after_1_step(initial_state: str, productions: dict) -> set:
    result = set()
    n = len(initial_state)
    for k in range(1, 11):
        for i in range(0, n):
            left = initial_state[i: i + k]
            if left in productions:
                for res in productions[left]:
                    result.add(initial_state[:i] + res + initial_state[i + k:])
    
    return result

def BFS(source: str, target: str, productions: dict) -> int:
    Q = [(len(source), 0, source)]
    while Q:
        _, distance, u = heappop(Q)
        if u == target:
            return distance
        
        for v in get_all_molecules_after_1_step(u, productions):
            n = len(v)
            heappush(Q, (n, distance + 1, v))

    raise Exception('target not found')

input = open('input2.txt').read().splitlines()

target = input[-1]

productions = {}
for line in input[:-2]:
    A, B = line.split(' => ')
    if A not in productions:
        productions[A] = []
    if B not in productions:
        productions[B] = []
    productions[B].append(A)

result = BFS(target, 'e', productions)
print(result)