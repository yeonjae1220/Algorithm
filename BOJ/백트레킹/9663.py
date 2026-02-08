# 대각선 선별 방법을 이렇게 하네
# 근데 시간초과 뜸
# pypy3으로 제출해서 통과하긴 했는데, 패스하려면 visited 배열이나 비트 마스킹으로 관리해주는게 좋을듯
n = int(input())
# arr = [[0] * n for _ in range(n)]
arr = [0] * n
cnt = 0

def is_safe(q):
    for i in range(q):
        if arr[i] == arr[q] or abs(arr[q] - arr[i]) == abs(q - i):
            return False
    return True

def backtracking(q):
    global cnt

    if q == n:
        cnt += 1
        return
    else:
        for i in range(n):
            arr[q] = i
            if is_safe(q):
                backtracking(q + 1)
        
backtracking(0)
print(cnt)







        




# 한 행씩 비교하면 되는데 체스판 전체를 순회함 -> 매우 비효율 적
# def backtracking(q):        
#     global cnt

#     if q == 0:
#         cnt += 1
#         return
    
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 0:

#                 for k in range(n):
#                     if arr[k][j] == 0: 
#                         arr[k][j] = i + 1
#                     if arr[i][k] == 0:
#                         arr[i][k] = i + 1

#                     if (i + k < n and j + k < n and arr[i + k][j + k] == 0):
#                         arr[i + k][j + k] = i + 1
#                     if (i + k < n and j - k >= 0 and arr[i + k][j - k] == 0 ):
#                         arr[i + k][j - k] = i + 1
#                     if (i - k >= 0 and j + k < n and arr[i - k][j + k] == 0):
#                         arr[i - k][j + k] = i + 1     
#                     if (i - k >= 0 and j - k >= 0 and arr[i - k][j - k] == 0 ):
#                         arr[i - k][j - k] = i + 1
#                 backtracking(q - 1)
#                 for x in range(n):
#                     for y in range(n):
#                         if arr[x][y] == i + 1:
#                             arr[x][y] = 0
                

# backtracking(n)
# print(cnt)
                    
            
    