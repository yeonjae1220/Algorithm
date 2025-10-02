import sys
import heapq
T = int(sys.stdin.readline())

for _ in range(T):
    M = int(sys.stdin.readline())
    min_hq = []
    max_hq = []
    median = []
    temp = M
    input_arr = []
    while temp > 0:
        input_arr += (list(map(int, sys.stdin.readline().split())))
        temp -= 10
    for i, j in enumerate(input_arr):
        if len(min_hq) == len(max_hq):
            heapq.heappush(max_hq, -j)
        else:
            heapq.heappush(min_hq, j)

        if min_hq and -max_hq[0] > min_hq[0]:
            max_v = -heapq.heappop(max_hq)
            min_v = heapq.heappop(min_hq)
            heapq.heappush(max_hq, -min_v)
            heapq.heappush(min_hq, max_v)
        
        if (i + 1) % 2 == 1:
            median.append(-max_hq[0])            
        


    print(len(median))
    for i, n in enumerate(median):
        if (i + 1) % 10 == 0:
            print(median[i], end='\n')
        else:
            print(median[i], end=' ')


    
        