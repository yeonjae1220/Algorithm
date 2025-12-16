"""
지훈이 다음 이동할 칸이 전부 벽이거나 불일 때 -> IMPOSSIBLE
지훈이 가장자리로 이동했을 때 -> 탈출
먼가 풀다 보니 꼬였음
"""

# import sys
# from collections import deque
# input = sys.stdin.readline

# R, C = map(int, input().split())

# maze = [list(input().strip()) for _ in range(R)]
# visited = [[False] * C for _ in range(R)]

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# jx = jy = 0
# fx = fy = 0

# for i in range(R):
#     for j in range(C):
#         if maze[i][j] == 'J': 
#             jx, jy = j, i
#         if maze[i][j] == 'F':
#             fx, fy = j, i

# def bfs(jx, jy):
#     q = deque([(jx, jy, 0)])
#     q_fire = deque([(fx, fy, 0)])
#     visited[jy][jx] = True
#     last_t = 0 # 불이랑 지훈이랑 시간별 진행 상황 맞추기 위해
#     while q:
#         x, y, t = q.popleft()
#         if visited[y][x]:
#             continue
#         visited[y][x] = True

#         if x == 0 or x == C - 1 or y == 0 or y == R - 1:
#             return t + 1
        
#         # maze 불 확장 
#         if t > last_t:
#             while q_fire:
#                 x_fire, y_fire, t_fire = q_fire.popleft()
#                 if t_fire == t:
#                     q_fire.appendleft((x_fire, y_fire, t_fire))
#                     break

#                 for i in range(4):
#                     nfx = x_fire + dx[i]
#                     nfy = y_fire + dy[i]
                
#                     if 0 <= nfx < C and 0 <= nfy < R:
#                         if not maze[nfy][nfx] == '#':
#                             maze[nfy][nfx] = 'F'
#                             q_fire.append((nfx, nfy, t_fire + 1))
                            


#         for i in range(4):
#             is_impossible = True
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < C and 0 <= ny < R:
#                 if maze[ny][nx] == '.':
#                     q.append((nx, ny, t+1))
#                     is_impossible = False

#             if is_impossible:
#                 return(-1)
            

# ans = bfs(jx, jy)
# if ans == -1:
#     print("IMPOSSIBLE")
# else:
#     print(ans)


"""
정답 풀이
"""
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

maze = [list(input().strip()) for _ in range(R)] # 문자열은 수정 불가능하므로 list로 받아야 함

dist_f = [[-1] * C for _ in range(R)]
dist_j = [[-1] * C for _ in range(R)]

q_f = deque()
q_j = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            q_f.append((i, j))
            dist_f[i][j] = 0
        elif maze[i][j] == 'J':
            q_j.append((i, j))
            dist_j[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while q_f:
    x, y = q_f.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] != '#' and dist_f[nx][ny] == -1:
                dist_f[nx][ny] = dist_f[x][y] + 1
                q_f.append((nx, ny))

while q_j:
    x, y = q_j.popleft()

    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        print(dist_j[x][y] + 1)
        sys.exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] != '#' and dist_j[nx][ny] == -1:
                if dist_f[nx][ny] == -1 or dist_f[nx][ny] > dist_j[x][y] + 1:
                    dist_j[nx][ny] = dist_j[x][y] + 1
                    q_j.append((nx, ny))

print("IMPOSSIBLE")