"""
주어진 자료구조를 그래프로 바꿀 필요 없이 dx dy 를 2차원 배열에서 돌리면서 단계적으로 진행하기
연합은 여러개 일 수 있음
불리언 타입의 체크 변수를 활용해서 2차원 배열을 전부 탐색 했음에도 연합이 생기지 않을 때 
따로 만든 인구 이동 횟수 변수를 리턴

일단 2차원 배열을 dx dy로 bfs든 dfs든 돌리면서 큐에 집어 넣고, 연합을 제외한 부분을 반복적으로 확인 하여 인구이동을 전부 시켜줌
인구이동이 안일어 나는건 연합 인구 총 수 변수 가지고 판단?

이걸 무한 루프 돌려버리기
"""

# visited 관련 해서 체크하는 위치나 이런것 때문에 문제가 있었음


import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def move_ppl():
    visited = [[False] * N for _ in range(N)]
    is_moved = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                q = deque()
                visited[i][j] = True
                q.append((i, j))
                temp_sum = arr[i][j]
                temp_country = [(i, j)]
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                            if L <= abs(arr[y][x] - arr[ny][nx]) <= R:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                                temp_sum += arr[ny][nx]
                                temp_country.append((ny, nx))

                
                if len(temp_country) > 1:
                    is_moved = True
                    new_ppl = temp_sum // len(temp_country)
                    
                    for y, x in temp_country:
                        arr[y][x] = new_ppl
                        
    return is_moved
                
ans = 0
while True:
    if move_ppl():
        ans += 1
    else:
        break

print(ans)