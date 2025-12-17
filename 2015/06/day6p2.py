import re

input = open('input2.txt').read().splitlines()
commands = []
for line in input:
    cords = [int(x) for x in re.findall(r'\d+', line)]
    if line.startswith('toggle'):
        commands.append(('toggle', cords))
    elif 'on' in line:
        commands.append(('on', cords))
    else:
        commands.append(('off', cords))

n = 1000
lights = [[0 for _ in range(n)] for _ in range(n)]
for op, cords in commands:
    if op == 'toggle':
        for i in range(cords[0], cords[2] + 1):
            for ii in range(cords[1], cords[3] + 1):
                lights[i][ii] += 2
    elif op == 'on':
        for i in range(cords[0], cords[2] + 1):
            for ii in range(cords[1], cords[3] + 1):
                lights[i][ii] += 1
    else:
        for i in range(cords[0], cords[2] + 1):
            for ii in range(cords[1], cords[3] + 1):
                lights[i][ii] = max(0, lights[i][ii] - 1)

res = 0
for i in range(n):
    for ii in range(n):
        res += lights[i][ii]

print(res)