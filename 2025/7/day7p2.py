from collections import deque

lines = open('input2.txt').read().splitlines()
n = len(lines)
m = len(lines[0])
beam_start = 0
while lines[0][beam_start] != 'S':
    beam_start += 1


number_of_paths = [[0 for _ in range(m)] for _ in range(n)]
number_of_paths[0][beam_start] = 1
visited = {(0, beam_start)}
q = deque()
q.append((0, beam_start))

result = 0
while q:
    i, ii = q.popleft()
    candidates = []

    if i + 1 < n:
        if lines[i + 1][ii] == '^':
            candidates.append((i + 1, ii + 1))
            candidates.append((i + 1, ii - 1))
        else:
            candidates.append((i + 1, ii))

    continuation = False
    for n_i, n_ii in candidates:
        if 0 <= n_i < n and 0 <= n_ii < m:
            number_of_paths[n_i][n_ii] += number_of_paths[i][ii]
            continuation = True

            if (n_i, n_ii) not in visited:
                visited.add((n_i, n_ii))
                q.append((n_i, n_ii))

    if continuation == False:
        result += number_of_paths[i][ii]

print(result)