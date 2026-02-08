# 트리 or 그래프 수 찾기
# 유니온 파인드로 부모 노드 찾기 (같은 그룹에 속해있는지)
# 구분 방법은 .. 

import sys
input = sys.stdin.readline


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

N = int(input())
M = int(input())

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for i in range(N):
    graph_info = map(int, input().split())

    for j, c in enumerate(graph_info):
        if c == 1:
            union_parent(i + 1, j + 1)


route = list(map(int, input().split()))


ans = True
root = find_parent(route[0])
for i in range(1, M):
    if root != find_parent(route[i]):
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")


        

