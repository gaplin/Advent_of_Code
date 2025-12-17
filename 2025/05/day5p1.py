lines = open('input2.txt').read().splitlines()
n = len(lines)

ranges = []
i = 0
while lines[i] != '':
    line = lines[i]
    if line == '':
        break
    a, b = map(int, line.split('-'))
    assert a <= b
    ranges.append((a, b))
    i += 1
i += 1

result = 0
while i < n:
    line = lines[i]
    num = int(line)
    for l, r in ranges:
        if l <= num <= r:
            result += 1
            break
    i += 1

print(result)