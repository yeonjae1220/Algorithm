import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')

N = int(input())

graph = [[] for _ in range(N + 1)]
subTreeCount = [0] * (N + 1)
dp_child = [0] * (N + 1)
dp_parent = [0] * (N + 1)

for _ in range(N - 1):
    U, V, D = map(int, input().split())
    graph[U].append((V, D))
    graph[V].append((U, D))

def dfs(cur, parent):
    subTreeCount[cur] = 1
    dp_child[cur] = 0
    for neighbor, weight in graph[cur]:
        if neighbor != parent:
            dfs(neighbor, cur)
            subTreeCount[cur] += subTreeCount[neighbor]
            dp_child[cur] += (dp_child[neighbor] + weight*subTreeCount[neighbor])

        
# 자식 서브 트리까지는 계산이 되는데, 다른 애들 계산 해줘야 함
# 부모 노드 전체 거리 에서 자기 전체 거리 뺴고, (부모 서브 트리 노드 개수 - 현재 서브 트리 노드 개수) * 부모와 현재 노드 거리 값을 더해주기
# 이걸 이제 재귀나 반복 돌려가며 찾아 주면 될 듯?

def dfs_up(cur, parent):
    for child, weight in graph[cur]:
        if child != parent:
            dp_parent[child] = dp_parent[cur] + dp_child[cur] - (dp_child[child] + weight * subTreeCount[child])  + (N - subTreeCount[child]) * weight
            dfs_up(child, cur)

dfs(1, 0)
dfs_up(1, 0)

for i in range(1, N+1):
    print(dp_child[i] + dp_parent[i])



            






"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')

N = int(input())


graph = [[] for _ in range(N + 1)]
# SubTreeCount[i]: i를 루트로 하는 서브트리의 노드 개수
subtree_count = [0] * (N + 1)
# DPDown[i]: i의 서브트리 내 모든 노드까지의 거리 합
dp_down = [0] * (N + 1)
# DPUp[i]: i의 서브트리 바깥에 있는 모든 노드까지의 거리 합
dp_up = [0] * (N + 1)

for _ in range(N - 1):
    try:
        U, V, D = map(int, input().split())
    except:
        continue
    graph[U].append((V, D))
    graph[V].append((U, D))

# --- DFS 1: Bottom-Up (서브트리 정보 계산) ---
def dfs_bottom_up(current, parent):
    # 각 노드 current를 루트로 하는 서브트리 정보를 계산합니다.
    # 1. subtree_count[current]: 서브트리 노드 개수
    # 2. dp_down[current]: 서브트리 내 모든 노드까지의 거리 합
    subtree_count[current] = 1
    dp_down[current] = 0

    for neighbor, dist in graph[current]:
        if neighbor != parent:
            dfs_bottom_up(neighbor, current)
            
            # Subtree Count 합산: 자식 서브트리의 노드 개수를 더함
            subtree_count[current] += subtree_count[neighbor]
            
            # DPDown 갱신:
            # 1. 자식 서브트리 내 거리 합 (dp_down[neighbor])
            # 2. 자식 서브트리 노드 개수 * 엣지 거리 (current -> neighbor를 거쳐야 함)
            dp_down[current] += (dp_down[neighbor] + subtree_count[neighbor] * dist)

# --- DFS 2: Top-Down (루트에서부터 전파) ---
def dfs_top_down(current, parent):
    
#    루트(1번 노드)에서 계산된 dp_down 값을 이용하여
 #   각 노드의 dp_up (서브트리 바깥까지의 거리 합)을 계산합니다.
    
    for neighbor, dist in graph[current]:
        if neighbor != parent:
            # 1. Outer Dist (DPUp[current]에 포함된 거리 합)
            #    current의 바깥 노드들 (N - subtree_count[current]개)은
            #    neighbor에서 볼 때 current를 통해 dist만큼 더 이동해야 함
            outer_dist_sum = dp_up[current] + (N - subtree_count[current]) * dist
            
            # 2. Sibling Dist (current의 나머지 서브트리 내 거리 합)
            #    current의 서브트리에서 neighbor 서브트리를 제외한 나머지 노드들까지의 거리 합.
            #    = dp_down[current] - (dp_down[neighbor] + subtree_count[neighbor] * dist)
            #    이 노드들 (subtree_count[current] - subtree_count[neighbor]개)은
            #    neighbor에서 볼 때 current를 통해 dist만큼 더 이동해야 함
            sibling_dist_sum = (
                (dp_down[current] - (dp_down[neighbor] + subtree_count[neighbor] * dist)) + 
                (subtree_count[current] - subtree_count[neighbor]) * dist
            )
            
            # DPUp[neighbor] 갱신
            dp_up[neighbor] = outer_dist_sum + sibling_dist_sum
            
            dfs_top_down(neighbor, current)

# --- 실행 ---

# 1. Bottom-Up 계산 (루트 1부터 시작)
dfs_bottom_up(1, 0)

# 2. Top-Down 전파 (루트 1부터 시작)
dfs_top_down(1, 0)

# 3. 결과 출력
for i in range(1, N + 1):
    # Total Distance Sum = 서브트리 내 거리 합 + 서브트리 바깥 거리 합
    print(dp_down[i] + dp_up[i])

"""

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# INF = float('inf')

# N = int(input())

# graph = [[] for _ in range(1 + N)]
# visited = [False] * (N + 1) 
# dp = [[INF] * (N + 1) for _ in range(N + 1)]

# for _ in range(N-1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))


# def dfs(cur):
#     visited[cur] = True
#     dp[cur][cur] = 0

#     # 이웃 끼리 먼저 처리
#     n = len(graph[cur])
#     for i in range(n - 1):
#         for j in range(i, n):
#             u1, w1 = graph[cur][i]
#             u2, w2 = graph[cur][j]
#             dp[u1][u2] = w1 + w2
#             dp[u2][u1] = w1 + w2

            
    
#     for child, weight in graph[cur]:
#         if not visited[child]:
#             dfs(child)
#             for i in range(1, N + 1):
#                 dp[i][child] = min(dp[i][child], dp[i][cur] + weight)
#                 dp[child][i] = dp[i][child]

# dfs(1)




# # for i in range(1, N + 1):
# #     sum = 0
# #     for j in range(1, N + 1):    
# #         sum += dp[i][j]
# #     print(sum)
    
# for i in range(1, N + 1):
#     print(f"node = {i}")
#     for j in range(1, N + 1):    
#         print(dp[i][j])




# 트리 형태 인게 핵심인듯
# 자식 쭉 이을 때 상위 부모까지의 거리는 부모와 상위 부모의 거리 + 자신과 부모 사이의 거리
# 형제들 끼리의 거리는 음.. 
# 1. 부모 통해서 
# 2. 자식 통해서..? x 이러면 그래프 같은 구조 되야 가능




# import sys
# import heapq
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# INF = 1e8

# N = int(input())

# graph = [[] for _ in range(1 + N)]

# for _ in range(N-1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distence[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)

#         if distence[now] < dist:
#             continue

#         for i in graph[now]:
#             if dist + i[1] < distence[i[0]]:
#                 distence[i[0]] = dist + i[1]
#                 # distence[i[0]][start] = distence[start][i[0]]
#                 heapq.heappush(q, (dist+i[1], i[0]))

# for i in range(1, N + 1):
#     distence = [INF]*(N + 1)
#     dijkstra(i)

#     sum = 0
#     for i in range(1, N + 1):    
#         sum += distence[i]
#     print(sum)


# 각 노드 별 n -> n 최단 거리를 구해서 합을 더하면 될듯 함








########




# import sys
# import heapq
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# INF = 1e8

# N = int(input())

# graph = [[] for _ in range(1 + N)]

# distence = [[INF] * (N + 1) for _ in range(N + 1)] # 각각 다익스트라 돌리기 위한 거리 배열, N <= 3*10^5인데 좀 큰가?]

# for _ in range(N-1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distence[start][start] = 0

#     while q:
#         dist, now = heapq.heappop(q)

#         if distence[start][now] < dist:
#             continue

#         for i in graph[now]:
#             if dist + i[1] < distence[start][i[0]]:
#                 distence[start][i[0]] = dist + i[1]
#                 # distence[i[0]][start] = distence[start][i[0]]
#                 heapq.heappush(q, (dist+i[1], i[0]))

# for i in range(1, N + 1):
#     dijkstra(i)

# for i in range(1, N + 1):
#     sum = 0
#     for j in range(1, N + 1):
#         sum += distence[i][j]
#     print(sum)
    

# # 각 노드 별 n -> n 최단 거리를 구해서 합을 더하면 될듯 함



