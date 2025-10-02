# 5 
# 4 6 10
# 6 10 3 8
# 10 3 8 7 12
# 3 8 7 12 9 11 20
# 8 7 12 9 20 2 
# 7 12 9 20 2 9 16


import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

MAX_POS = 100000
visited = [False] * (MAX_POS + 1)



def bfs(n):
    global K
    depth = 0
    queue = deque([(n, depth)])
    visited[n] = True

    while queue:
        e, ans = queue.popleft()
        if e == K:
            return ans
        if e - 1 >= 0 and not visited[e -1]:
            queue.append([e - 1, ans + 1])
            visited[e -1] = True
        if e + 1 <= MAX_POS and not visited[e + 1]:
            queue.append([e + 1, ans + 1])
            visited[e + 1] = True
        if e * 2 <= MAX_POS and not visited[e * 2]:
            queue.append([e * 2, ans + 1])
            visited[e * 2] = True

        
            


print(bfs(N))
