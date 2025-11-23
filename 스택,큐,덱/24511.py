import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


cnt = M
for i in range(N-1, -1, -1):
    if A[i] == 0 and cnt > 0:
        print(B[i], end=" ")
        cnt -= 1

for c in C:
    if cnt > 0:
        print(c, end=" ")
        cnt -= 1



"""
시간 초과
그냥 큐 안에 있는거 출력하고 남으면 입력값 순서대로 출력하는 거인 듯
출력 형식을 " " 이거말고 \n으로 해서 그런건가?
"""

# for c in C:
#     carry = c
#     for i in range(N):
#         if A[i] == 1:
#             continue
#         else:
#             B[i], carry = carry, B[i]
    
#     print(carry)



            
