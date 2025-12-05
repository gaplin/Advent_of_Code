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

ranges.sort()
R = len(ranges)
last = 0
for i in range(1, R):
    prev_l, prev_r = ranges[last]
    current_l, current_r = ranges[i]
    if current_l > prev_r:
        last += 1
        ranges[last] = (current_l, current_r)
    else:
        ranges[last] = (prev_l, max(prev_r, current_r))

result = 0
while last >= 0:
    l, r = ranges[last]
    result += r - l + 1
    last -= 1

print(result)