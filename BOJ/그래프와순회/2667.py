import sys
from collections import deque

n = int(sys.stdin.readline())

houses = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]


def bfs(x, y, cnt):
    global n

    if visited[x][y] == -1:
        visited[x][y] = 0
        if houses[x][y] == 1:
            cnt += 1
            queue = deque([(x, y)])
            
            while(queue):
                temp = queue.popleft()
                if temp[0] + 1  < n and houses[temp[0] + 1][temp[1]] == 1 and visited[temp[0] + 1][temp[1]] == -1 :
                    visited[temp[0] + 1][temp[1]] = 0
                    queue.append([temp[0] + 1, temp[1]])
                    cnt+=1
                if temp[1] + 1 < n and houses[temp[0]][temp[1] + 1] == 1 and visited[temp[0]][temp[1] + 1] == -1:
                    visited[temp[0]][temp[1] + 1] = 0
                    queue.append([temp[0], temp[1] + 1])
                    cnt+=1
                if temp[0] - 1 >= 0 and houses[temp[0] - 1][temp[1]] == 1 and visited[temp[0] - 1][temp[1]] == -1:
                    visited[temp[0] - 1][temp[1]] = 0
                    queue.append([temp[0] - 1, temp[1]])
                    cnt+=1
                if temp[1] - 1 >= 0 and houses[temp[0]][temp[1] - 1] == 1 and visited[temp[0]][temp[1] - 1] == -1:
                    visited[temp[0]][temp[1] - 1] = 0
                    queue.append([temp[0], temp[1] - 1])
                    cnt+=1

        return cnt
    else:
        return
    

ans = []
                        
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1 and houses[i][j] == 1:
            ans.append(bfs(i, j, 0))

print(len(ans))

ans.sort()
for i in ans:
    print(i)







    
    

