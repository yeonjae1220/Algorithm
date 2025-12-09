"""
벽 3개 짓는걸 어떻게 하지
백트레킹 -> n^3이라 아닌거 같은데 => 이게 맞는 방법이였네

입력 조건 보면 지도가 3<=N, M<=8 되어 있다. 근데 예제 입력 보니 8 * 8이 최대인듯?
64 * 63 * 62 .. 많긴 하네 

바이러스 위치를 다 큐에 넣고 싹 비우면서 bfs로 돌려가기
바이러스 다음 이동이 안전 영역 일 때 우선적으로 벽 사용?
아니면 만약 다음 칸이 벽일 때 해당 바이러스가 더 이상 진행하지 못한다면 더하기? -> 3개를 깔아야 하니 아닌거 같기도 하고
"""

import sys
input = sys.stdin.readline
from collections import deque
import copy

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = 0


# 이렇게 분리해서 할 생각은 하긴 했는데, 구현이 깔끔하게 안나왔었음
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0

def bfs():
    global ans
    lab_copy = copy.deepcopy(lab)

    q = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                q.append((j, i))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if lab_copy[ny][nx] == 0:
                    lab_copy[ny][nx] = 2
                    q.append((nx, ny))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 0:
                cnt += 1
    
    ans = max(ans, cnt)



make_wall(0)
print(ans)

        