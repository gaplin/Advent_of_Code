def count_paths(G: dict[str, list[str]], source: str, dest: str) -> int:
    cache = {}
    def DFS(u: str) -> int:
        if u == dest:
            return 1
        
        if u in cache:
            return cache[u]
        
        paths = 0
        for v in G[u]:
            paths += DFS(v)
        
        cache[u] = paths
        return paths
    
    return DFS(source)

def path_exists(G: dict[str, list[str]], source: str, dest: str) -> bool:
    visited = set()
    def DFS(u: str) -> bool:
        if u == dest:
            return True
        visited.add(u)
        for v in G[u]:
            if v not in visited and DFS(v):
                return True
        return False
    return DFS(source)

lines = open('input2.txt').read().splitlines()

G = dict[str, list[str]]()
for line in lines:
    u, vs = line.split(': ')
    vs = vs.split()
    G[u] = vs
    for v in vs:
        if v not in G:
            G[v] = []

full_path = ['svr', 'fft', 'dac', 'out']
fft_dac_exists = path_exists(G, 'fft', 'dac')
dac_fft_exists = path_exists(G, 'dac', 'fft')
assert fft_dac_exists == False or dac_fft_exists == False
if dac_fft_exists:
    full_path[1], full_path[2] = 'dac', 'fft'

result = 1
for u, v in zip(full_path, full_path[1:]):
    result *= count_paths(G, u, v)

print(result)