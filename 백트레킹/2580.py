import sys
arr = []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 결국 답 보고 품

def solve(i, j, k):
    for x in range(9):
        if arr[i][x] == k:
            return False
    for y in range(9):
        if arr[y][j] == k:
            return False
    box_x = (i // 3) * 3
    box_y = (j // 3) * 3
    for a in range(box_x, box_x + 3):
        for b in range(box_y, box_y + 3):
            if arr[a][b] == k:
                return False
    return True

def backtracking():
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for k in range(1, 10):
                    if solve(i, j, k):
                        arr[i][j] = k
                        if backtracking():
                            return True
                        else:
                            arr[i][j] = 0
                return False
    return True
            
backtracking()
for x in range(9):
    print(" ".join(map(str, arr[x])))
sys.exit(0)






# 실패
# def backtracking():
#     for i in range(9):
#         for j in range(9):
#             if arr[i][j] == 0:
#                 for k in range(1, 10):
#                     if k not in arr[i]:
#                         if k not in [arr[x][j] for x in range(9)]:
#                             box_x = (i // 3) * 3
#                             box_y = (j // 3) * 3
#                             check = True
#                             for a in range(box_x, box_x + 3):
#                                 for b in range(box_y, box_y + 3):
#                                     if arr[a][b] == k:
#                                         check = False
#                             if check:
#                                 arr[i][j] = k
#                                 backtracking()
#                                 arr[i][j] = 0
            
#             elif i == 8 and j == 8:
#                 for x in range(9):
#                     print(" ".join(map(str, arr[x])))
#                 sys.exit(0)
#                 return

            
# backtracking()
