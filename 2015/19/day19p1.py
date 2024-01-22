def get_all_molecules_after_1_step(initial_state: str, productions: dict) -> set:
    result = set()
    n = len(initial_state)
    for k in range(1, 3):
        for i in range(0, n):
            left = initial_state[i: i + k]
            if left in productions:
                for res in productions[left]:
                    result.add(initial_state[:i] + res + initial_state[i + k:])
    
    return result

input = open('input2.txt').read().splitlines()
starting_text = input[-1]

productions = {}
for line in input[:-2]:
    A, B = line.split(' => ')
    if A not in productions:
        productions[A] = []
    productions[A].append(B)

molecules = get_all_molecules_after_1_step(starting_text, productions)
print(len(molecules))