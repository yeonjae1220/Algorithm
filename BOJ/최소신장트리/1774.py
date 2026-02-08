import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
coord = [(0, 0)] # 0번 인덱스 더미

for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x,y))

for i in range(1, N):
    for j in range(i + 1, N + 1):
        graph.append((math.sqrt((coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2), i, j))

for _ in range(M):
    x, y = map(int, input().split())
    graph.append((0, x, y))

graph.sort()


parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    else:
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

for cost, a, b in graph:
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        continue
    else:
        ans += cost
        union_parent(a, b)


print(f"{ans:.2f}")

    


