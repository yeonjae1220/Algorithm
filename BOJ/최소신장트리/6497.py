# 집과 길 / 노드와 간선
# 최소신장트리

# 가중치 낮은 순대로 정렬해서 그리디로
# 전체 입력 가중치 합 - 위에서 나온 결과

import sys

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # 또 = find(x)라 함
    return parent[x]


while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break

    parent = [i for i in range(m)]
    graph = []

    all_sum = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        graph.append((x, y, z))
        all_sum += z

    
    graph.sort(key=lambda x : x[2])


    sum_weight = 0

    for x, y, z in graph:
        if find(x) == find(y):
            continue

        sum_weight += z
        union(x, y)

    print(all_sum - sum_weight)
