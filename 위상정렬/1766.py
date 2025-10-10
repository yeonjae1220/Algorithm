# 입력 받은 거 뒤의 숫자 바로 뒤에 넣기
# 넣을 때 숫자 크기 비교해서 넣은 값 보다 큰 값 나오는 자리에 넣어야 함

# 1 2 3 4
# 1 3 4 2
# 3 1 4 2


# 1 2 3 4
# 1 -> 2
# 2 -> 3
# 3 -> 4
# 4

# 4 -> 2


import sys
from collections import deque
import heapq

N, M = map(int, sys.stdin.readline().split())
depth = [0 for _ in range(N + 1)]
graph = {}
for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    depth[b] += 1

queue = []
ans = []

for i in range(1, N + 1):
    if depth[i] == 0:
        heapq.heappush(queue, i)
    
while queue:
    temp = heapq.heappop(queue)
    ans.append(temp)
    for i in graph[temp]:
        depth[i] -= 1
        if depth[i] == 0:
            heapq.heappush(queue, i)
    
print(*ans)