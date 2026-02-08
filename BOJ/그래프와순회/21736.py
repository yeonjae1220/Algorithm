"""
21736의 Docstring
bfs로 쭉 돌리면서 사람 나올 때 cnt + 1
cnt == 0 이면 TT 출력
"""

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)] 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    friends = 0

    while q:
        now_x, now_y = q.popleft()

        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] == 'X':
                    continue
                else: 
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    if graph[ny][nx] == 'P':
                        friends += 1
    
    return friends


iam_x = 0
iam_y = 0

for j in range(N):
    for i in range(M):
        if graph[j][i] == 'I':
            iam_x = i
            iam_y = j


result = bfs(iam_x, iam_y)
if result == 0:
    print('TT')
else:
    print(result)


    
