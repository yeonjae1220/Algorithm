N, M = map(int, input().split())
list = list(map(int, input().split()))

for i in range(N):
    if (list[i] < M):
        print(list[i], end=' ')



# N = int(input())
# M = int(input())

# list = []
# for _ in range(N):
#     input = int(input())
#     if (input < M):
#         list.append(input)
    
# print(*list)