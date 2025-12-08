def distance(ax, ay, az, bx, by, bz):
    d_x = bx - ax
    d_y = by - ay
    d_z = bz - az
    return d_x * d_x + d_y * d_y + d_z * d_z

def find(x: int, comps: list[int]) -> int:
    if x == comps[x]:
        return x
    comps[x] = find(comps[x], comps)
    return comps[x]

def union(x: int, y: int, comps: list[int]):
    x = find(x, comps)
    y = find(y, comps)
    if x == y:
        return
    comps[x] = y

boxes = [tuple(map(int, x.split(','))) for x in open('input2.txt').read().splitlines()]

n = len(boxes)
box_dists = []
for i in range(0, n):
    for j in range(i + 1, n):
        d = distance(*boxes[i], *boxes[j])
        box_dists.append((d, i, j))

box_dists.sort()

comps = [i for i in range(n)]

for i in range(1000):
    _, x, y = box_dists[i]
    union(x, y, comps)

counts = [0 for _ in range(n)]
for i in range(1000):
    counts[find(i, comps)] += 1

counts.sort(reverse=True)
print(counts[0] * counts[1] * counts[2])