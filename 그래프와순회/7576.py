import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
not_ripted = 0


apples = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if apples[i][j] == 1:
            queue.append((i, j, 0))
        elif apples[i][j] == 0:
            not_ripted += 1

if not_ripted == 0:
    print(0)
    exit()

def bfs():
    ans = 0
    
    while queue:
        a, b, c = queue.popleft()
        ans = max(ans, c)
        for next_apple in ([a + 1, b], [a, b - 1], [a - 1, b], [a, b + 1]):
            if 0 <= next_apple[0] < N and 0 <= next_apple[1] < M:
                if apples[next_apple[0]][next_apple[1]] == 0:
                    apples[next_apple[0]][next_apple[1]] = 1
                    queue.append((next_apple[0], next_apple[1], c + 1))

    return ans

ans = bfs()


for i in range(N):
    for j in range(M):
        if apples[i][j] == 0:
            print(-1)
            exit()

print(ans)



