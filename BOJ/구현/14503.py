import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def is_cleaned(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0 and not visited[nr][nc]:
                return False
    return True
    

cnt = 0

while True:
    if arr[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        cnt += 1

    if is_cleaned(r, c):
        next_d = (d + 2) % 4
        br = r + dr[next_d]
        bc = c + dc[next_d]

        if arr[br][bc] == 1:
            break
        r, c = br, bc
    
    else:
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if arr[nr][nc] == 0 and not visited[nr][nc]:
            r = nr
            c = nc
    
print(cnt)
    


    
    
