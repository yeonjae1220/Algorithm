import heapq
import sys
n = int(sys.stdin.readline())
heap = list(map(int, sys.stdin.readline().split()))
heapq.heapify(heap)

for _ in range(n - 1):
    input_list = list(map(int, sys.stdin.readline().split()))
    for num in input_list:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])