# 좌표들 받아서 좌표 사이에 최단 거리?
# 이건 그리디로 푸는게 좋을듯 해당 좌표에서 가장 가까운 좌표 찾아서 연결하기
# 일일이 전부 순회하며 비교해야하나?

# 일단 다 각각 독립적인 그래프로 보고, 하나씩 연결? parent기준은 뭘로? 
# 애초에 가중치 낮은 순으로 정렬할 수 가 없는데

# 현재 위치에서 가장 가까운 별로 이동, 만약 같은 거리가 있다면 x와 y가 더 작은 쪽 먼저 가기

# 0, 0 기준으로 가장 가까운 곳 순으로 정렬하면 뭐가 있나? -> 성립 x

# prim으로 풀면 될듯

# 근데 큐에 방문하지 않은 모든 노드를 넣는게 맞나?
# 아니지 큐를 계속 해당 노드에 맞춰서 초기화 시켜버리면 되네. min을 쉽게 좌표와 함께 뽑을 수 있다. visited만 걸러주면


import heapq
import math

n = int(input())
stars = []
# visited = [False] * (n + 1)
visited = set()
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))


distance = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if distance[i][j] == 0:
            distance[i][j] = math.sqrt((stars[j][0] - stars[i][0]) ** 2 + ((stars[j][1] - stars[i][1]) ** 2))


queue = []
heapq.heappush(queue, (0, 0))

sum_val = 0
while queue:
    w, cur = heapq.heappop(queue)
    if cur in visited:
        continue

    visited.add(cur)
    sum_val += w

    # queue = [] # 초기화 한번 하고

    for i in range(n):
        # queue.append((distance[x][i], stars[i-1][0], stars[i-1][1]))
        if cur != i and i not in visited:
            heapq.heappush(queue, (distance[cur][i], i))


print(sum_val)






