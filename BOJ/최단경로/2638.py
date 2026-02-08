"""
BOJ.최단경로.2638의 Docstring
먼저 내부 치즈 공간을 확인 한 후 체크 해두기 (공간 별로 다른 인덱스 vs 그냥 구분만 해놓기)
1시간 단위의 한 사이클이 돌 때
먼저 녹은 치즈 빼고
공기 추가하고
다음 녹을 치즈 추가 -> 하나 없어진다고 체크 되는게 아니고 주변 치즈 없어질 때마다 계속 확인 해줘야할듯

visited는 필요 없지 않나? 어차피 산소로 처리하니 괜찮을 듯
"""

"""
# 너무 불필요하게 복잡하게 구현함
# 결국 외부 공기 확장만 하면 되는거임

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 먼저 다음 사이클에 녹을 치즈와 치즈 내부 공기 구분하기
# 치즈 외부 공기는 [0][0]인 애 기준으로　탐색 돌리면서 뺴놓기 여기선 인덱스 2로 할 예정 (문제 조건이 가장자리에 치즈 없음)
# 치즈 외부 공기와 내부 공기가 만날 때는, 가장자리의 치즈가 외부 공기와 내부 공기를 함께 접하고 있을 때 

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def find_out_air():
    q = deque((0, 0))
    graph[0][0] = 2

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append((ny, nx))


next_melt_cheese = []

def find_first_melt_cheese():
    visited = [[False] * (M) for _ in range(N)] # 치즈만 바꿀 꺼긴 함
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if not visited[i][j]:
                    visited[i][j] = True
                    opt = is_melt(i, j)
                    # graph[i][j] = 2
                    if opt == 0:
                        continue
                    elif opt == 1:
                        next_melt_cheese.append((i, j, 0)) # y, x, opt (공기 안열림)
                    else:
                        next_melt_cheese.append((i, j, 1)) # y, x, opt (공기 열림)


def is_melt(x, y):
    check_in_air = False
    out_air_cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 2:
                out_air_cnt += 1
            elif graph[ny][nx] == 0:
                check_in_air = True
    
    if out_air_cnt < 2: # 다음 차레 녹지 않는 치즈
        return 0
    elif not check_in_air: # 다음 차례 녹지만, 내부 공기는 안열리는 치즈
        return 1
    else: # 다음 차례 녹고, 내부 공기까지 열리는 치즈
        return 2
    



find_out_air()
find_first_melt_cheese()


ans_cnt = 0
def temp(next_melt_cheese):
    if not next_melt_cheese: # 빈 리스트가 들어오면
        return ans_cnt

    while next_melt_cheese:
        y, x, opt = next_melt_cheese.pop()
        graph[y][x] = 2
        if opt == 1:
            q_air = [(y, x)]
            while q_air:
                b, a = q_air.pop()
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]

                    if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
                        graph[ny][nx] = 2
                        q_air.append((ny, nx))
            
    

    next_melt_cheese = []
    find_first_melt_cheese()
    ans_cnt += 1
    temp(next_melt_cheese)


print(temp(next_melt_cheese))
        

"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs_out_air():
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    graph[0][0] = 2  # 외부 공기

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and graph[ny][nx] != 1:
                    visited[ny][nx] = True
                    graph[ny][nx] = 2
                    q.append((ny, nx))

def melt():
    melt_list = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ni, nj = i + dy[k], j + dx[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if graph[ni][nj] == 2:
                            cnt += 1
                if cnt >= 2:
                    melt_list.append((i, j))

    for y, x in melt_list:
        graph[y][x] = 0

    return len(melt_list)

time = 0
while True:
    bfs_out_air()
    melted = melt()
    if melted == 0:
        break
    time += 1

print(time)