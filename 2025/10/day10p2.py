from pulp import *
import numpy as np

def button_to_list(button: tuple[int], n_jolts: int) -> list[int]:
    result = [0 for _ in range(n_jolts)]
    for idx in button:
        result[idx] += 1

    return result

def solve(buttons: list[tuple[int]], jolts: tuple[int]) -> int:
    n_jolts = len(jolts)
    A = np.array([button_to_list(button, n_jolts) for button in buttons])
    b = np.array(list(jolts))
    n = A.shape[0]
    prob = LpProblem("Min_moves", const.LpMinimize)
    x = [LpVariable(f'x{i}', cat=const.LpInteger, lowBound=0) for i in range(n)]
    prob += lpSum(x)
    for j in range(A.shape[1]):
        prob += (lpSum(x[i] * A[i][j] for i in range(n)) == b[j])

    prob.solve(PULP_CBC_CMD(msg=False))
    return int(value(prob.objective))

lines = open('input2.txt').read().splitlines()

result = 0
for line in lines:
    words = line.split()
    buttons = [tuple(map(int, x[1:-1].split(','))) for x in words[1:-1]]
    joltages = tuple(map(int, words[-1][1:-1].split(',')))
    
    result += solve(buttons, joltages)

print(result)