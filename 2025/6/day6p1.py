import re

lines = open('input2.txt').read().splitlines()
n = len(lines)
rows = []
for line in lines[:-1]:
    rows.append(list(map(int, re.findall(r'\d+', line))))

ops = re.findall(r'[+*]', lines[-1])
result = 0
m = len(rows[0])
for idx, op in zip(range(m), ops):
    col_result = rows[0][idx]
    for row in rows[1:]:
        if op == '*':
            col_result *= row[idx]
        else:
            col_result += row[idx]
    result += col_result

print(result)

