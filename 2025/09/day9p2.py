from typing import Callable

def area(x1, y1, x2, y2) -> int:
    X = abs(x1 - x2) + 1
    Y = abs(y2 - y1) + 1
    return X * Y

def get_direction(A: tuple[int, int], B: tuple[int, int]) -> tuple[int, int]:
    direction = [0, 0]
    if A[0] > B[0]:
        direction[0] = -1
    elif A[0] < B[0]:
        direction[0] = 1
    elif A[1] > B[1]:
        direction[1] = -1
    elif A[1] < B[1]:
        direction[1] = 1
    assert direction[0] != direction[1]

    return tuple(direction)

def prepare_rows_and_cols(points: list[tuple[int, int]], n: int) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    rows = dict[int, list]()
    cols = dict[int, list]()
    for i in range(n):
        A, B = points[i], points[i + 1]
        d_x, d_y = get_direction(A, B)
        while A != B:
            if A[0] not in cols:
                cols[A[0]] = []
            if A[1] not in rows:
                rows[A[1]] = []
            cols[A[0]].append(A[1])
            rows[A[1]].append(A[0])
            A = (A[0] + d_x, A[1] + d_y)

    for row in rows.values():
        row.sort()
    for col in cols.values():
        col.sort()

    return (rows, cols)

def fill_direct_neighbours_count_in_direction(
        point_factory: Callable[[int], tuple[int, int]], 
        elements: list[int],
        start: int,
        stop: int,
        step: int,
        delta: int,
        dict_to_fill: dict[tuple[int, int], list[int]], 
        fill_idx: int):
    
    inside = True
    current_length = 0

    for i in range(start, stop, step):
        if elements[i] == elements[i - step] + delta:
            current_length += 1
            inside = True
        else:
            if inside:
                current_length = abs((elements[i] - elements[i - step]))
            else:
                current_length = 0
            inside = not inside

        point = point_factory(elements[i])
        if point in dict_to_fill:
            dict_to_fill[point][fill_idx] = current_length
    
    
def valid_rectangle(A: tuple[int, int], B: tuple[int, int], A_neighbours: list[int], B_neighbours: list[int]) -> bool:
    x_distance = abs(A[0] - B[0])
    lefts, rights, tops, bots = 0, 1, 2, 3
    if A[0] < B[0]: # B on the right
        if B_neighbours[lefts] < x_distance or A_neighbours[rights] < x_distance:
            return False
    else: # A on the right
        if A_neighbours[lefts] < x_distance or B_neighbours[rights] < x_distance:
            return False
        
    y_distance = abs(A[1] - B[1])
    if A[1] < B[1]: # B on the bottom
        if B_neighbours[tops] < y_distance or A_neighbours[bots] < y_distance:
            return False
    else: # A on the bottom
        if A_neighbours[tops] < y_distance or B_neighbours[bots] < y_distance:
            return False
        
    return True

points = [tuple(map(int, line.split(','))) for line in open('input2.txt').read().splitlines()]
n = len(points)
points.append(points[0])
longest_line_from_red = {p: [0, 0, 0, 0] for p in points[:-1]} # [l, r, t, b] -> longest line starting at p going left, right, top, bottom

rows, cols = prepare_rows_and_cols(points, n)
for y, row in rows.items():
    n_row = len(row)
    fill_direct_neighbours_count_in_direction(
        lambda x: (x, y),
        row,
        1,
        n_row,
        1,
        1,
        longest_line_from_red,
        0
    )
    fill_direct_neighbours_count_in_direction(
        lambda x: (x, y),
        row,
        n_row - 2,
        -1,
        -1,
        -1,
        longest_line_from_red,
        1
    )

for x, col in cols.items():
    n_col = len(col)
    fill_direct_neighbours_count_in_direction(
        lambda y: (x, y),
        col,
        1,
        n_col,
        1,
        1,
        longest_line_from_red,
        2
    )
    fill_direct_neighbours_count_in_direction(
        lambda y: (x, y),
        col,
        n_col - 2,
        -1,
        -1,
        -1,
        longest_line_from_red,
        3
    )

result = 0
for i in range(n):
    for j in range(i + 1, n):
        if valid_rectangle(points[i], points[j], longest_line_from_red[points[i]], longest_line_from_red[points[j]]):
            result = max(result, area(*points[i], *points[j]))

print(result)