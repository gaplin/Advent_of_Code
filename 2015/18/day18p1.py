def step(grid: list, n: int, directions: list) -> list:
    result = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for ii in range(n):
            on = 0
            for di, dii in directions:
                new_i, new_ii = i + di, ii + dii
                if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n or grid[new_i][new_ii] == '.':
                    continue
                on += 1
            if grid[i][ii] == '#':
                if on in [2, 3]:
                    result[i][ii] = '#'
                else:
                    result[i][ii] = '.'
            else:
                if on == 3:
                    result[i][ii] = '#'
                else:
                    result[i][ii] = '.'

    return result

grid = open('input2.txt').read().splitlines()
n = len(grid)
for i in range(n):
    grid[i] = [x for x in grid[i]]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
iterations = 100
while iterations > 0:
    grid = step(grid, n, directions)
    iterations -= 1

result = 0
for row in grid:
    result += row.count('#')

print(result)