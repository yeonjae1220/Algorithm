# 우선 바꿔야 하는거 다 바꿔서 k 크기 체스판 시작하는 곳에다가 몇개 바꿔야 하는지 체크
# 그리고 그 중에 최소값 출력
# 체스판 시작 부분이 W일경우와 B일 경우 둘다 확인 해야함

# 검사해야 하는건 0 ~ n-k, 0 ~ m-k 까지
# B 일경우 
# [0][1] 은 W일 경우 + [1+K][0 ~ K] 검사
# [1][0] 은 W일 경우 + [0 ~ K][1+K] 검사
# [1][1] 은 B일 경우 + [1+K][1 ~ 1+K], [1 ~ 1+K][1+K] 검사 
# or [0][1] 이랑 [1][0] 결과값에 [1+k][1+k] 검사
# 이걸 W일 경우도 고려해서 똑같이 검사

#######

# 아니면 전체 체스판 다 바꿔놓고 k*k 크기만큼 잘라서 비교
# 0,0 이 W일 경우랑 B일 경우랑 비교해서 최소값 출력

### 

# 아 아이디어가

import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 'W'로 시작하는 패턴 기준의 누적 합 배열 하나만 생성
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        # (i+j)의 짝홀 여부로 기대 색상 판단
        if (i + j) % 2 == 0:
            expected_color = 'W'
        else:
            expected_color = 'B'
        
        # 기대 색상과 다르면 비용(cost)은 1
        cost = 1 if board[i][j] != expected_color else 0
        
        # 누적 합 계산
        prefix_sum[i + 1][j + 1] = cost + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]

min_repaint = float('inf')

# 모든 K x K 영역을 순회
for r in range(1, n - k + 2):
    for c in range(1, m - k + 2):
        r2, c2 = r + k - 1, c + k - 1
        
        # 'W' 패턴 기준 비용 계산
        cost_W = prefix_sum[r2][c2] - prefix_sum[r-1][c2] - prefix_sum[r2][c-1] + prefix_sum[r-1][c-1]
        
        # 'B' 패턴 기준 비용은 (전체 칸 수) - (W 패턴 비용)
        cost_B = k * k - cost_W
        
        # 두 비용 중 더 작은 값으로 전체 최솟값 갱신
        min_repaint = min(min_repaint, cost_W, cost_B)

print(min_repaint)