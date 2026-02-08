import sys
n = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

input.sort()

cnt = 0
left = 0
right = n - 1

while left < right:
    if input[left] + input[right] == x:
        cnt += 1
        left += 1
        right -= 1
    elif input[left] + input[right] < x:
        left += 1
    else:
        right -= 1
    
print(cnt)