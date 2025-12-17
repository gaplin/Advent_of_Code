import re

def transpose(grid: list[list[str]], n: int, m: int) -> list[list[str]]:
    result = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = grid[i][j]

    return result

lines = open('input2.txt').read().splitlines()
grid = [[x for x in line] for line in lines[:-1]]
n = len(grid)
m = len(grid[0])

ops = list(re.findall(r'[+*]', lines[-1]))
transposed = transpose(grid, n, m)
result = 0
current_result = None
op = None
idx = 0
for row in transposed:
    text = ''.join(row).strip()
    if text != '':
        num = int(text)
        if current_result == None:
            current_result = num
        else:
            if op == None:
                op = ops[idx]
                idx += 1
            if op == '*':
                current_result *= num
            else:
                current_result += num
    else:
        result += current_result
        current_result, op = None, None

result += current_result
print(result)