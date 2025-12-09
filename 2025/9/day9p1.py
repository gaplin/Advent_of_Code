def area(x1, y1, x2, y2) -> int:
    X = abs(x1 - x2) + 1
    Y = abs(y2 - y1) + 1
    return X * Y

points = [tuple(map(int, line.split(','))) for line in open('input2.txt').read().splitlines()]
n = len(points)

result = 0
for i in range(n):
    for j in range(i + 1, n):
        cand_area = area(*points[i], *points[j])
        result = max(result, cand_area)

print(result)