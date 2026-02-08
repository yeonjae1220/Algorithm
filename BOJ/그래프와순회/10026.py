"""
한번의 순회에 색약과 아닌 사람들의 그룹 찾을 수 있나?

첫 순회때 초록색의 그룹을 찾고 개수 저장
확인한 곳의 초록색을 빨간색으로 바꿔두기
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

green_group = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def color_bfs():
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                cur_color = graph[i][j]

                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[ny][nx] and graph[ny][nx] == cur_color:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                
    return cnt

normal = color_bfs()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

disabled = color_bfs()

print(normal, disabled)