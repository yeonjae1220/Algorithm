"""
20055의 Docstring

N 내리는 위치
K 내구도 0 최대 개수

먼저 벨트 위 로봇 이동 시키기, 내구도 감소
올리는 칸에 로봇 추가
내구도 개수 검사

반복

그냥 구현? 진짜 깡 구현인가

로봇 위치 True False 배열 하나 두고
내구도 배열 따로 빼서 계산
내구도 0 늘 때마다 카운트 + 1

"""
# 답
from sys import stdin
from collections import deque

def solution(N, K, A):
    answer = 0
    belt = deque([False] * N)

    while True:
        answer += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        A.rotate(1)
        belt.rotate(1)

        # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        belt[N-1] = False

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(N-2, -1, -1):
            # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if belt[i] and not belt[i+1] and A[i+1] > 0:
                belt[i], belt[i+1] = False, True
                A[i+1] -= 1
        
        # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        belt[N-1] = False
        
        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if A[0] > 0:
            belt[0] = True
            A[0] -= 1
        
        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
        if A.count(0) >= K:
            break

    return answer

# input
N, K = map(int,stdin.readline().split())
A = deque(list(map(int,stdin.readline().split())))

# response
response = solution(N, K, A)
print(response)


# 이것도 구현 제대로 안됨
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# line = list(map(int, input().split()))
# robot = [False] * N

# cnt = 0
# ans = 0
# zero_idx = 0
# while cnt < K:
#     robot[N - 1] = False
#     for i in range(N - 1):
#         if robot[i]:
#             if not robot[i+1]:
#                 robot[i] = False
#                 robot[i+1] = True

    
#     zero_idx = ((2*N) - (zero_idx - 1)) % (2*N)

#     if line[zero_idx] != 0 and not robot[zero_idx]:
#         robot[zero_idx] = True
#         line[zero_idx] -= 1
#         if line[zero_idx] == 0:
#             cnt += 1

# print(ans)
    
    


# 문제 이해를 잘못함
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# line = list(map(int, input().split()))
# robot = [False] * (2 * N)

# cnt = 0
# ans = 0
# while cnt < K:
#     ans += 1
#     for i in range(2*N):
#         if robot[i]:
#             if line[(i+1) % (2 * N)] != 0 and not robot[(i+1) % (2 * N)]:
#                 robot[i] = False
#                 robot[(i+1) % (2 * N)] = True
#                 line[(i+1) % (2 * N)] -= 1
#                 if line[(i+1) % (2 * N)] == 0:
#                     cnt += 1
    
#     if line[0] != 0 and not robot[0]:
#         robot[0] = True
#         line[0] -= 1
#         if line[0] == 0:
#             cnt += 1

# print(ans)