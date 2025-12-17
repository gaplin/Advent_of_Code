from collections import deque

lines = open('input2.txt').read().splitlines()
n = len(lines)
m = len(lines[0])
beam_start = 0
while lines[0][beam_start] != 'S':
    beam_start += 1

visited = {(0, beam_start)}
q = deque()
q.append((0, beam_start))

result = 0
while q:
    i, ii = q.popleft()
    candidates = []
    if lines[i][ii] == '^':
        candidates.append((i, ii + 1))
        candidates.append((i, ii - 1))
        result += 1
    else:
        candidates.append((i + 1, ii))

    for n_i, n_ii in candidates:
        if 0 <= n_i < n and 0 <= n_ii < m and (n_i, n_ii) not in visited:
            visited.add((n_i, n_ii))
            q.append((n_i, n_ii))

print(result)