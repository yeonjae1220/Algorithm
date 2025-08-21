list = []
for _ in range(N):
    input = int(input())
    if (input < M):
        list.append(input)
    
print(*list)