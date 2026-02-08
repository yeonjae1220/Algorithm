"""
7568의 Docstring

"""
# import sys
# input = sys.stdin.readline

# N = int(input())

# query = []
# idx = 0
# for _ in range(N):
#     x, y = map(int, input().split())
#     query.append((x, y, idx))
#     idx += 1


# query.sort(reverse='True')
# ans = [1] * N

# rank = 1
# stack = 0
# for i in range(1, N):
#     if query[i][1] > query[i-1][1]:
#         ans[query[i][2]] = rank
#         stack += 1
    
#     else:
#         rank = rank + stack + 1
#         ans[query[i][2]] = rank
#         stack = 0

# print(ans)

import sys
input = sys.stdin.readline

N = int(input())

query = []

for _ in range(N):
    x, y = map(int, input().split())
    query.append((x, y))

for i in query:
    rank = 1
    for j in query:
        if i[0]  < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")