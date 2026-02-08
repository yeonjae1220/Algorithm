import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
del_node = int(input())

def dfs(num, graph):
    graph[num] = -2
    for i in range(len(graph)):
        if num == graph[i]:
            dfs(i, graph)

dfs(del_node, graph)
ans = 0
for i in range(len(graph)):
    if graph[i] != -2 and i not in graph:
        ans += 1

print(ans)
