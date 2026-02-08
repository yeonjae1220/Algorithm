import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

"""
n = 2**N # 한변의 길이
last_num = n ** 2 - 1이 마지막 수


temp = ((last_num + 1) / 4)
0 ~ temp - 1
temp ~ temp * 2 - 1
temp * 2 ~ temp * 3 - 1
temp * 3 ~ temp * 4 - 1 (last_num)

시작 수 랑 한 변의 길이 넘기면서 좌표 내에 있는 사각형만 재귀 호출 해서 찾으면 될듯

"""

def div_con(start, n):
    global r, c

    if n == 2:
        if r == 0 and c == 0:
            return start
        elif r == 0 and c == 1:
            return start + 1
        elif r == 1 and c == 0:
            return start + 2
        else:
            return start + 3
        

    last_num = (n ** 2) - 1
    temp = ((last_num + 1) // 4)

    if c < n//2 and r < n//2:
        return(div_con(start, n//2))
    elif c >= n//2 and r < n//2:
        c -= n//2
        return(div_con(start + temp, n//2))
    elif c < n//2 and r >= n//2:
        r -= n//2
        return(div_con(start + temp*2, n//2))
    else:
        c -= n//2
        r -= n//2
        return(div_con(start + temp*3, n//2))


# print(div_con(0, 2 ** N))
print(div_con(0, 2 ** N))



"""
dp 처럼 풀어도 될꺼 같긴 한데..
"""