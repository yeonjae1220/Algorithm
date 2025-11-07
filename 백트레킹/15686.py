# 존재하는 치킨 집 중에서 M 이하를 고를 때
# 최소 거리들.. 
# 일단 집들 좌표 싹 넣어두고
# 치킨집들 좌표 싹 정리해서

# dp 처럼 각각 치킨 집들 좌표 별 거리들 정리?
# 아니면 backtracking으로 하나씩 뻈다 넣었다 하면서 각각 비교?
# 두개 합치는게 좋겠는데

# [N][M] 짜리 dp 배열 만들고, 각각의 거리 계산해서 넣어두기 (메모제이션?)
# 백트래킹으로 치킨집 넣고 빼면서 최솟값 업데이트?


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

town_map = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0] * (13) for _ in range(N * 2)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if town_map[i][j] == 0:
            continue
        elif town_map[i][j] == 1:
            home.append((j, i))
        else:
            chicken.append((j, i))


len_home = len(home)
len_chicken = len(chicken)

dp = [[0] * len_chicken for _ in range(len_home)]

for i in range(len_home):
    for j in range(len_chicken):
        dp[i][j] = abs(home[i][0] - chicken[j][0]) + abs(home[i][1] - chicken[j][1])

    
# 치킨집 기준으로 넣었을 때 안넣었을 때.. 
# 각각 계속 최솟값 찾기 해야하나

bt = []
ans = sys.maxsize
def backtracking(idx):
    global ans

    if len(bt) == M:
        temp = 0
        for i in range(len_home):
            temp_min = sys.maxsize
            for j in bt:
                temp_min = min(temp_min, dp[i][j])
            temp += temp_min

        ans = min(ans, temp)
        return
    
    for i in range(idx, len_chicken):
        bt.append(i)
        backtracking(i + 1)
        bt.pop()

        
backtracking(0)
print(ans)

