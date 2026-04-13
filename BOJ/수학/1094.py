import sys
input = sys.stdin.readline

tmp = 64
goal = int(input())
cnt = 0

while goal:
    if goal < tmp:
        tmp /= 2
    
    else:
        goal -= tmp
        cnt += 1

print(cnt)