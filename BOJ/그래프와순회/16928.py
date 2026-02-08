from collections import deque

N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]

board_move = {}

for s, e in ladder:
    board_move[s] = e

for s, e in snake:
    board_move[s] = e
    
board = [0] * 101

def bfs():
    queue = deque([(1, 0)])
    while queue:
        pos, cnt = queue.popleft()
        if pos == 100:
            return cnt
        for i in range(1, 7):
            next_pos = pos + i
            if next_pos in board_move:
                next_pos = board_move[next_pos]
            if next_pos <= 100 and board[next_pos] == 0:
                queue.append((next_pos, cnt + 1))
                board[next_pos] = 1
            

print(bfs())
            

