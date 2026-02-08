import sys
input = sys.stdin.readline

puzzle = []
zeros = []
for i in range(9):
    row = list(map(int, input().strip()))
    puzzle.append(row)
    for j in range(9):
        if row[j] == 0:
            zeros.append((i, j)) # (행, 열) 좌표 저장


def check_c_r_s(x, y, n):
    for i in range(9):
        if puzzle[y][i] == n:
            return False
    
    for i in range(9):
        if puzzle[i][x] == n:
            return False
    
    temp_x = x // 3
    temp_y = y // 3

    for i in range(temp_y * 3, (temp_y + 1) * 3):
        for j in range(temp_x * 3, (temp_x + 1) * 3):
            if puzzle[i][j] == n:
                return False
    

    return True
        

def backtracking(idx):
    if idx == len(zeros):
        for i in range(9):
            print("".join(map(str, puzzle[i])))
        sys.exit()

    i, j = zeros[idx]

    for n in range(1, 10):
        if check_c_r_s(j, i, n):
            puzzle[i][j] = n
            backtracking(idx + 1)
            puzzle[i][j] = 0
            
                    
backtracking(0)













# import sys
# input = sys.stdin.readline

# puzzle = []
# for _ in range(9):
#     temp = list(map(int, input().strip()))
#     puzzle.append(temp)


# def check_c_r_s(x, y, n):
#     for i in range(9):
#         if puzzle[y][i] == n:
#             return False
    
#     for i in range(9):
#         if puzzle[i][x] == n:
#             return False
    
#     temp_x = x // 3
#     temp_y = y // 3

#     for i in range(temp_y * 3, (temp_y + 1) * 3):
#         for j in range(temp_x * 3, (temp_x + 1) * 3):
#             if puzzle[i][j] == n:
#                 return False
    

#     return True
        

# def backtracking(i, j):
#     if j == 9:
#         i += 1
#         j = 0

#     if i == 9:
#         for i in range(9):
#             print()
#             for j in range(9):
#                 print(puzzle[i][j], end="")
#         sys.exit()
    
#     if puzzle[i][j] != 0:
#         backtracking(i, j + 1)
#         return

#     if puzzle[i][j] == 0:
#         for n in range(1, 10):
#             if check_c_r_s(j, i, n):
#                 puzzle[i][j] = n
#                 backtracking(i, j+1)
#                 puzzle[i][j] = 0
            
                    
# backtracking(0, 0)