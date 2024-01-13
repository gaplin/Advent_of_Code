cubes = [sorted([int(y) for y in x.split('x')]) for x in open('input2.txt').read().splitlines()]

result = 0
for l, w, h in cubes:
    result += 2 * (l + w) + l * w * h

print(result)