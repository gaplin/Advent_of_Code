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

def union(x: int, y: int, comps: list[int]) -> bool:
    x = find(x, comps)
    y = find(y, comps)
    if x == y:
        return False
    comps[x] = y
    return True

boxes = [tuple(map(int, x.split(','))) for x in open('input2.txt').read().splitlines()]

n = len(boxes)
box_dists = []
for i in range(0, n):
    for j in range(i + 1, n):
        d = distance(*boxes[i], *boxes[j])
        box_dists.append((d, i, j))

box_dists.sort()

comps = [i for i in range(n)]
n_components = n
for _, x, y in box_dists:
    if union(x, y, comps):
        n_components -= 1
        if n_components == 1:
            print(boxes[x][0] * boxes[y][0])
            break

