import sys
sys.setrecursionlimit(20002)


def dfs(start, color):
    colors[start] = color
    for i in graph[start]:
        if colors[i] == color:
            return False
        if colors[i] == 0:
            if not dfs(i, -color):
                return False
    return True



K = int(sys.stdin.readline())
for _ in range(K):
    graph = {}
    V, E = map(int, sys.stdin.readline().split())
    colors = [0] * (V + 1)
    for i in range(1, V + 1):
        graph[i] = []
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)


    is_bipartite = True
    for i in range(1, V + 1):
        if colors[i] == 0:
            if not dfs(i, 1):
                is_bipartite = False
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")
