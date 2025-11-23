import sys
input = sys.stdin.readline

string = input().strip()
explosion = input().strip()
lenExplosion = len(explosion)

stack = []
for c in string:
    stack.append(c)
    if c == explosion[-1] and "".join(stack[-lenExplosion:]) == explosion:
        for _ in range(lenExplosion):
            stack.pop()



if not stack:
    print("FRULA")
else:
    print("".join(stack))




"""
# 시간초과

import sys
input = sys.stdin.readline

string = input().strip()
explosion = input().strip()

# 단순하게는 explosion string 길이만큼 윈도우? 잡고 쭉 돌려가면서 지우고, 이걸 안지워질때까지 반복

nString = len(string)
nExplosion = len(explosion)

if nString < nExplosion:
    print("string")
    exit()



while True:
    check = False
    for i in range(0, nString - nExplosion + 1):
        if explosion == string[i:i+nExplosion]:
            check = True
            string = string[0:i] + string[i+nExplosion:]
            nString -= nExplosion
            if nString < nExplosion:
                break
    if check == True:
        continue
    else:
        break

if nString == 0:
    print("FRULA")
else:
    print(string)

"""