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


"""
개선할 점


네, 물론이죠. `i == 0`부터 `i == 3`까지의 코드는 로직이 99% 동일하고 방향만 다르기 때문에, \*\*방향 벡터(`dx`, `dy`)\*\*를 사용해 하나의 `while` 루프로 완벽하게 합칠 수 있습니다.

-----

## \#\# 1. 최적화 원리: `while` 루프 합치기

핵심은 `if i == 0:` (아래쪽)일 때는 `next_x += 1`을, `i == 3:` (오른쪽)일 때는 `next_y += 1`을 반복하는 것입니다.

이 "반복적인 이동"을 `dx[i]`와 `dy[i]`가 대신하도록 만들면 됩니다.

  * `i=0` (아래): `dx[0]=1`, `dy[0]=0`. `(next_x + 1, next_y + 0)`을 반복합니다.
  * `i=1` (왼쪽): `dx[1]=0`, `dy[1]=-1`. `(next_x + 0, next_y - 1)`을 반복합니다.
  * ...

`if-elif` 문 4개를 지우고, `for i in range(4):` 루프 안에 `while` 루프 하나만 남기면 됩니다.

-----

## \#\# 2. 수정된 다리 탐색 코드

`start_bridge`를 순회하는 부분을 다음과 같이 수정할 수 있습니다.

```python
# ... (이전 코드) ...

# 얻은 섬 정보를 통해 다리 정보 찾아야 함
for island, x, y in start_bridge:
    for i in range(4):
        # 1. 해당 방향의 "이동 값"을 가져옴
        dir_x = dx[i]
        dir_y = dy[i]

        # 2. 첫 번째 칸 이동
        next_x = x + dir_x
        next_y = y + dir_y
        
        bridge_length = 0

        # 3. 경계 검사 + 다리 건설을 하나의 while 루프로 처리
        while 0 <= next_x < N and 0 <= next_y < M:
            
            # Case 1: 바다(0)를 만난 경우
            if map[next_x][next_y] == 0:
                bridge_length += 1
                next_x += dir_x # 같은 방향으로 계속 이동
                next_y += dir_y
                
            # Case 2: 다른 섬을 만난 경우
            elif map[next_x][next_y] != island:
                arrived_island = map[next_x][next_y]
                if bridge_length >= 2:
                    # 튜플로 append (이전 코드 버그 수정)
                    bridges.append((bridge_length, island, arrived_island))
                # 다리 건설 중단
                break

            # Case 3: 원래 섬을 다시 만난 경우
            else:
                # 다리 건설 중단
                break
```

-----

## \#\# 3. (추가) 더 근본적인 최적화

위 코드는 `if-elif` 중복은 해결했지만, 여전히 **알고리즘적인 중복**이 남아있습니다.

`start_bridge` 리스트는 섬의 *모든* 땅 좌표를 포함합니다. 이로 인해 같은 다리(예: 2번 섬과 3번 섬 사이)가 **수십 번씩 중복되어** `bridges` 리스트에 추가됩니다.

가장 좋은 최적화는 `start_bridge` 리스트를 아예 사용하지 않고, **`map` 전체를 딱 한 번만 스캔**하는 것입니다.

```python
# 'start_bridge' 리스트와 관련 로직 모두 삭제

bridges = set() # 1. 중복을 자동 제거하기 위해 set 사용

for i in range(N):
    for j in range(M):
        # 현재 위치가 섬이 아니면(바다) 건너뜀
        if map[i][j] == 0:
            continue
            
        start_island = map[i][j]

        # 2. 모든 방향이 아닌 "오른쪽"과 "아래쪽" 2방향만 탐색
        # (위쪽과 왼쪽은 다른 칸에서 이미 탐색했으므로 중복됨)
        # dx = [1(아래), 0, -1, 0(오른쪽)]
        # dy = [0, -1, 0, 1]
        for i_dir in [0, 3]: # 0: 아래쪽, 3: 오른쪽
            dir_x = dx[i_dir]
            dir_y = dy[i_dir]
            
            nx = i + dir_x
            ny = j + dir_y
            length = 0

            while 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == 0:
                    length += 1
                    nx += dir_x
                    ny += dir_y
                elif map[nx][ny] != start_island:
                    end_island = map[nx][ny]
                    if length >= 2:
                        # 3. set에 (길이, 작은섬번호, 큰섬번호)로 저장
                        bridges.add((length, min(start_island, end_island), max(start_island, end_island)))
                    break
                else: # 같은 섬 만나면 중단
                    break

# 4. set를 리스트로 변환 후 정렬
bridges = sorted(list(bridges))
```

이 방식이 중복 탐색을 원천적으로 차단하여 훨씬 빠르고 효율적입니다.


"""