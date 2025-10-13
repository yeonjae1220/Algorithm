import heapq

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    heap = []
    heapq.heappush(heap, a)
    heapq.heappush(heap, b)
    heapq.heappush(heap, c)

    if (heapq.heappop(heap)**2 + heapq.heappop(heap)**2) == heapq.heappop(heap)**2:
        print("right")
    else:
        print("wrong")

    
