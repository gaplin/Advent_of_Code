import re

target_row, target_col = [int(x) for x in re.findall(r'\d+', open('input2.txt').read().strip())]
prev_value = 20151125
mul = 252533
mod = 33554393
row, col = 2, 1
while True:
    prev_value = prev_value * mul % mod
    if row == target_row and col == target_col:
        break
    col += 1
    row -= 1
    if row == 0:
        row = col
        col = 1

print(prev_value)