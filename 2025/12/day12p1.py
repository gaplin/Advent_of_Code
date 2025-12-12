lines = open('input2.txt').read().splitlines()

i = 0
n = len(lines)
shapes = []
while 'x' not in lines[i]:
    i += 1
    shape = []
    while lines[i] != '':
        shape.append(lines[i])
        i += 1
    i += 1
    shapes.append(shape)

sizes = []
for shape in shapes:
    size = 0
    for row in shape:
        size += sum(1 if c == '#' else 0 for c in row)
    sizes.append(size)

candidates = 0
while i < n:
    grid_size, quantities = lines[i].split(': ')
    grid_i, grid_j = map(int, grid_size.split('x'))
    quantities = tuple(map(int, quantities.split()))
    expected_sum = 0
    expected_shapes = sum(quantities)
    max_3x3_fit = grid_i // 3 * grid_j // 3
    if expected_shapes <= max_3x3_fit:
        candidates += 1
        i += 1
        continue
    for idx, quantity in enumerate(quantities):
        expected_sum += quantity * sizes[idx]
    
    grid_size = grid_i * grid_j
    if expected_sum > grid_size:
        i += 1
        continue

    assert(False) # if triggered -> inconclusive checks. Triggered only for example input
    
print(candidates)