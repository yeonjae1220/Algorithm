input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


cnt = M
for i in range(N-1, -1, -1):
    if i == 0 and M > 0:
        print(B[i], end=" ")
        cnt -= 1

for c in C:
    if cnt > 0:
        print(c, end=" ")
        cnt -= 1