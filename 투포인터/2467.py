"""
2467의 Docstring

그냥 정렬 먼저 하고 (되어 있음)
left right인덱스 가지고 0에 가까줘 질 때 까지 l r 쪽 가감하다가 l == r 아니면 결과값 0이 나오면 return

"""


import sys
input = sys.stdin.readline

N = int(input())
query = list(map(int, input().split()))

left = 0
right = len(query) - 1
temp = abs(query[left] + query[right])

l = 0
r = len(query) - 1

while l < r:
    t = query[l] + query[r]

    if abs(t) < temp:
        left = l
        right = r
        temp = abs(t)
 
    
    if t < 0:
        l += 1
    else:
        r -= 1


print(query[left], query[right])
    
