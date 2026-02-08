import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
query = list(map(int, input().split()))
query.sort()

i = 0
j = len(query) - 1
cnt = 0

while i < j:
    if query[i] + query[j] == M:
        cnt += 1
        i += 1
        j -= 1
    
    elif query[i] + query[j] < M:
        i += 1
    else:
        j -= 1


print(cnt)