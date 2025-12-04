lines = open('input2.txt').read().splitlines()

n = len(lines)
m = len(lines[0])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
result = 0
for i in range(n):
    for ii in range(m):
        if lines[i][ii] == '@':
            adj_rolls = 0
            for di, dii in dirs:
                n_i, n_ii = i + di, ii + dii
                if 0 <= n_i < n and 0 <= n_ii < m and lines[n_i][n_ii] == '@':
                    adj_rolls += 1
            if adj_rolls < 4:
                result += 1

print(result)