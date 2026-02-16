import heapq
def solution(scoville, K):
    enough = False
    cnt = 0
    not_enough = []
    heapq.heapify(not_enough)
    for s in scoville:
        if s < K:
            heapq.heappush(not_enough, s)
        else:
            enough = True
    
    
    while not_enough:
        if len(not_enough) < 2:
            if not enough:
                return -1
            else:
                cnt += 1
                break
        
        first = heapq.heappop(not_enough)
        second = heapq.heappop(not_enough)
        new = first + (second * 2)
        cnt += 1
        if new < K:
            heapq.heappush(not_enough, new)
        else:
            enough = True
        
    return(cnt)
    
    
    
        
    