import re
from functools import reduce

def get_all_possiblilities(N: int, count: int) -> list:
    if count == 1:
        return [[N]]
    
    result = []
    total = N
    while N >= 0:
        other_nums = get_all_possiblilities(total - N, count - 1)
        for nums in other_nums:
            result.append([N] + nums)
        N -= 1
    
    return result

input = open('input2.txt').read().splitlines()
n = len(input)
ingredients = []
for line in input:
    ingredients.append(list(map(int, re.findall(r'[0-9-]+', line))))

total = 100
divisions = get_all_possiblilities(total, n)
result = 0
for division in divisions:
    values = [0 for _ in range(4)]
    for i in range(4):
        for count, ingr in zip(division, ingredients):
            values[i] += count * ingr[i]
        values[i] = max(0, values[i])
    current_result = reduce(lambda acc, x: acc * x, values)
    result = max(result, current_result)

print(result)