input = open('input2.txt').read().splitlines()

G = {}
for line in input:
    source, destination = line.split(' -> ')
    G[destination] = source

def get_value_at(G: dict, u: str, mask: int, cache: dict) -> int:
    if u in cache:
        return cache[u]
    
    result = 0
    if u not in G:
        result = int(u)

    else:
        operation = G[u].split(' ')
        if len(operation) == 1:
            result = get_value_at(G, operation[0], mask, cache)
        elif operation[0] == 'NOT':
            result = get_value_at(G, operation[1], mask, cache)
            result ^= mask

        else:
            A, B = get_value_at(G, operation[0], mask, cache), get_value_at(G, operation[2], mask, cache)
            if operation[1] == 'AND':
                result = A & B
            elif operation[1] == 'LSHIFT':
                result = (A << B) & mask
            elif operation[1] == 'OR':
                result =  A | B
            else:
                result = A >> B
    
    cache[u] = result
    return result

mask = (1 << 16) - 1
a_value = get_value_at(G, 'a', mask, {})
G['b'] = str(a_value)
result = get_value_at(G, 'a', mask, {})
print(result)