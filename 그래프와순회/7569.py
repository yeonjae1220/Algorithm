import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
not_ripted = 0


apples = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if apples[i][j][k] == 1:
                queue.append((i, j, k, 0))
            elif apples[i][j][k] == 0:
                not_ripted += 1

if not_ripted == 0:
    print(0)
    exit()

def bfs():
    ans = 0
    
    while queue:
        a, b, c, d = queue.popleft()
        ans = max(ans, d)
        for next_apple in ([a + 1, b, c], [a, b - 1, c], [a - 1, b, c], [a, b + 1, c], [a, b, c + 1], [a, b, c - 1]):
            if 0 <= next_apple[0] < H and 0 <= next_apple[1] < N and 0 <= next_apple[2] < M:
                if apples[next_apple[0]][next_apple[1]][next_apple[2]] == 0:
                    apples[next_apple[0]][next_apple[1]][next_apple[2]] = 1
                    queue.append((next_apple[0], next_apple[1], next_apple[2], d + 1))

    return ans

ans = bfs()


for i in range(H):
    for j in range(N):
        for k in range(M):
            if apples[i][j][k] == 0:
                print(-1)
                exit()

print(ans)



