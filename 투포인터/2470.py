import sys
input = sys.stdin.readline
N = int(input())
liquides = list(map(int, input().split()))

liquides.sort()
right = len(liquides) - 1
left = 0

ans_right = right
ans_left = left

close_to_zero = float('inf')
while left < right:
    temp = liquides[left] + liquides[right]
    if abs(temp) < abs(close_to_zero):
        ans_right = right
        ans_left = left
        close_to_zero = temp

    
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    
    else:
        break

print(liquides[ans_left], liquides[ans_right], sep = " ")
    
    
        