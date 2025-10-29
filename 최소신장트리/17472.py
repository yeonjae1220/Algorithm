# 다리는 직선
# 다리는 바다만
# 다리 길이는 2 이상

# 놓을 수 있는 다리의 경우의 수 찾기
# 이걸 크루스칼로 찾기?
# 노드는 섬 자체로 (섬들 분류 해야함) -> 섬 찾는데는 bfs나 dfs로?

# 섬 사이의 거리들 (가중치) 는 어떻게 찾지?
# 섬 테두리 바다 부분 이 출발 좌표라 생각하고, 각각 이으면? 
# 모든 다리 시작 부분에서 x, y 방향의 직선을 두고 (섬 만나면 끝) 싹?

# 아 다리는 가로방향이면 양 끝에 섬이 있어야 하고 세로도 마찬가지
# 이러면 다리 찾을 만 하다 

### 정리
# 섬 분류하기
# 각 섬마다 다리 놓으면서 가중치와 함께 다리 경우의 수 싹 찾기
# 크루스칼로 최솟값 구하기

# 섬 찾을 때 2차원 배열 또 만들지 말고 (섬번호, x, y, 다리방향) 으로 리스트에 튜플로 집어 넣기?
# 다리방향은 다시 검사하자 

# 받은 map을 이용해서 0 이 아니면 섬, 섬마다 번호 붙이기로 바꾸자


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
start_bridge = []
bridges = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def check_island(x, y, island_num):
    queue = deque([(x, y)])
    while queue:
        a, b = queue.popleft()
        start_bridge.append((island_num, a, b))
        visited[a][b] = True
        for i in range(4):
            next_x = a + dx[i]
            next_y = b + dy[i]
            if (0 <= next_x < N) and (0 <= next_y < M) and not visited[next_x][next_y]: #
                if map[next_x][next_y] == 1:
                    map[next_x][next_y] = island_num
                    queue.append((next_x, next_y))

# 섬 숫자는 2부터 시작함
island_num = 1

for i in range(N):
    for j in range(M):
        if map[i][j] == 0 or visited[i][j]:
            continue
        else:
            island_num += 1
            map[i][j] = island_num # 시작섬 번호 할당
            check_island(i, j, island_num)


# 얻은 섬 정보를 통해 다리 정보 찾아야 함
for island, x, y in start_bridge:
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 맵을 벗어났는지 확인
        if not (0 <= next_x < N and 0 <= next_y < M):
            continue
        # 땅인지 확인
        if map[next_x][next_y] != 0:
            continue

        else:
            bridge_length = 0

            if i == 0:
                while next_x < N:
                    if map[next_x][next_y] == 0:
                        bridge_length += 1
                        next_x += 1
                        continue
                    else:
                        arrived_island = map[next_x][next_y]
                        if bridge_length >= 2 and island != arrived_island:
                            bridges.append((bridge_length, island, arrived_island)) # 다른 섬 번호 알아야함
                        break
            
            elif i == 1:
                while next_y >= 0:
                    if map[next_x][next_y] == 0:
                        bridge_length += 1
                        next_y -= 1
                        continue
                    else:
                        arrived_island = map[next_x][next_y]
                        if bridge_length >= 2 and island != arrived_island:
                            bridges.append((bridge_length, island, arrived_island))
                        break
            
            elif i == 2:
                while next_x >= 0:
                    if map[next_x][next_y] == 0:
                        bridge_length += 1
                        next_x -= 1
                        continue
                    else:
                        arrived_island = map[next_x][next_y]
                        if bridge_length >= 2 and island != arrived_island:
                            bridges.append((bridge_length, island, arrived_island))
                        break

            else:
                while next_y < M:
                    if map[next_x][next_y] == 0:
                        bridge_length += 1
                        next_y += 1
                        continue
                    else:
                        arrived_island = map[next_x][next_y]
                        if bridge_length >= 2 and island != arrived_island:
                            bridges.append((bridge_length, island, arrived_island))
                        break


                        
                            
bridges.sort()


# 이제 크루스칼로 최소 거리 찾기
# 섬 위치가 2부터 시작함 
parent = [0] * (island_num + 3)

for i in range(2, island_num + 3):
    parent[i] = i

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]
    
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
for length, a, b in bridges:
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        continue
    else:
        ans += length
        union_parent(a, b)
    


root = find_parent(2) # 2번 섬을 기준으로
all_connected = True
for i in range(3, island_num + 1):
    if find_parent(i) != root:
        all_connected = False
        break

if all_connected and ans > 0: # ans가 0이어도 안됨 (섬이 하나거나, 다리가 없는 경우)
    print(ans)
elif island_num == 2 and ans == 0: # 섬이 하나인데 다리가 없는 경우
    print(0)
elif not all_connected:
    print(-1)
else: # 섬은 여러개인데 연결 다리가 하나도 없는 경우
    print(-1)

    



# 항상 범위 검사를 먼저 하고 다음 조건 검사 하기 (list index out of range error 예방)
