# bfs, dfs대신 유니온 파인드로 풀이 해보기

def union(x, y):
    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return

    # 1. 합치기 전에, 두 집합 중 사이클이 있었는지 미리 확인합니다.
    is_already_cycle = is_cycle[root_u] or is_cycle[root_v]

    # 2. 두 집합을 합칩니다.
    if root_u < root_v:
        parent[root_v] = root_u
        # 3. 새로운 루트(root_u)에 사이클 정보를 갱신합니다.
        if is_already_cycle:
            is_cycle[root_u] = True
    else:
        parent[root_u] = root_v
        # 3. 새로운 루트(root_v)에 사이클 정보를 갱신합니다.
        if is_already_cycle:
            is_cycle[root_v] = True


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

case_num = 0
while True:
    case_num += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    is_cycle = [False] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            is_cycle[root_u] = True
        else:
            union(u, v)

    
    cnt = 0
    roots = set()
    for i in range(1, n + 1):
        root = find(i)
        roots.add(root)

    for root in roots:
        if not is_cycle[root]:
            cnt += 1

    if cnt == 0:
        print(f"Case {case_num}: No trees.")
    elif cnt == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {cnt} trees.")
         

    
    

