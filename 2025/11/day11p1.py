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

lines = open('input2.txt').read().splitlines()

G = dict[str, list[str]]()
for line in lines:
    u, vs = line.split(': ')
    vs = vs.split()
    G[u] = vs
    for v in vs:
        if v not in G:
            G[v] = []
    
print(count_paths(G, 'you', 'out'))