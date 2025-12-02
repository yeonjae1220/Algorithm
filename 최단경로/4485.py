import sys
import heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# def bfs(N):
#     q = deque()
#     q.append(cave[0][0])
#     visited[0][0] = True


def dijkstra(i, j):
    q = []
    d = [[float('inf')] * (N) for _ in range(N)]
    heapq.heappush(q, (cave[i][j], i, j))
    d[i][j] = cave[i][j]

    while q:
        cost, x, y = heapq.heappop(q)

        if d[x][y] < cost:
            continue

        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < N:
                n_cost = cost + cave[n_x][n_y]
                
                if d[n_x][n_y] > n_cost:
                    d[n_x][n_y] = n_cost
                    heapq.heappush(q, (n_cost, n_x, n_y))
        

    return d[N-1][N-1]

    




prob = 0
while True:
    N = int(input())
    if N == 0:
        break

    prob += 1

    cave = []
    for i in range(N):
        cave.append(list(map(int, input().split())))
    
    # visited = [[False] * N for _ in range(N)]

    ans = dijkstra(0, 0)

    print(f"Problem {prob}: {ans}")



    


