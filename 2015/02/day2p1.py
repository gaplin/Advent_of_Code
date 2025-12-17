cubes = [[int(y) for y in x.split('x')] for x in open('input2.txt').read().splitlines()]

result = 0
for l, w, h in cubes:
    sides = (l * w, l * h, w * h)
    area = 2 * (sides[0] + sides[1] + sides[2])
    result += area + min(sides)

print(result)