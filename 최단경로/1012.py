"""
BOJ.최단경로.1012의 Docstring
큐에 넣을 때 visited 처리 하기 (Pop 할 때 하면 이상해짐, 중복 삽입 방지)
"""

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = []
    visited = [[True] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage.append((x, y))
        visited[y][x] = False
    
    ans = 0
    for x, y in cabbage:
        if visited[y][x]:
            continue

        q = deque()
        q.append((x, y))
        visited[y][x] = True
        
        while q:
            a, b = q.popleft()

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
            
        ans += 1
    
    print(ans)