import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# graph = [[i] for i in range(n)]
parent = [0] * (n)
for i in range(n):
    parent[i] = i

def find_parent(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



ans = 0

for i in range(m):
    u, v = map(int, input().split())
    # graph[u].append(v)
    # graph[v].append(u)

    u = find_parent(u)
    v = find_parent(v)
    if u == v:
        ans = i + 1
        break
    else:
        union_parent(u, v)
        

print(ans)