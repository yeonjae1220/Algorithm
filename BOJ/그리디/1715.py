"""
1715의 Docstring

크기 순 정렬해서 작은것들끼리 먼저 합치는 방식으로 그리디

가 아니고 차이가 적은것 끼리 비교인가?
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

ans = 0
while len(cards) > 1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    sum = n1 + n2
    ans += sum
    heapq.heappush(cards, sum)

print(ans)


