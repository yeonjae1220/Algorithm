# 가로줄 기준으로 분리?
# 2차원배열에 넣어서?

# 이렇게 쉬운걸 왤케 못풀었지


import sys
N = int(sys.stdin.readline())

def recursive(n):
    if n == 3:
        return ['***', '* *', '***']
    
    sub = recursive(n // 3)

    ans = []

    for i in sub:
        ans.append(i * 3)

    for i in sub:
        blank = ' ' * (n // 3)
        ans.append(i + blank + i)

    for i in sub:
        ans.append(i * 3)

    return ans

star = recursive(N)
for i in star:
    print(i)
    


# x1, x2, y1, y2를 매개변수로 9등분 해서 처리할렸는데,, 
# 3**8 * 3**8 2차원 배열은 너무 큰거 같기도 해





## 아주 복잡한 중첩 리스트 반환하는걸로 했는데, 이걸 원하는데로 출력하긴 어렵다고 함
# ans = [[]]

# def recursive (n):
#     if n == 0:
#         return 1
    
#     a = recursive(n-1)

#     return [[a, a, a],
#             [a, [([0] * (n))  * (n)], a],
#             [a, a, a]]
    
# print(*recursive(N))


