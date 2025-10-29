# a, b = map(int, input().split())

# if a < b:
#     a, b = b, a

# GCD = 0
# LCM = a * b

# while True:
#     if a % b == 0:
#         GCD = b
#         break
#     a, b = b, (a % b)

# LCM =  int(LCM / GCD)

# print(GCD)
# print(LCM)


# import sys
# input = sys.stdin.readline

# N = int(input())
# load = list(map(int, input().split()))
# gas = list(map(int, input().split()))

# now_gas = 1000000001 # 최대값 이상의 가스 가격

# sum = 0

# for i in range(len(gas) - 1):
#     if now_gas > gas[i]:
#         now_gas = gas[i]
#     sum += (now_gas * load[i])
    
# print(sum)


# def fac(n):
#     ans = 1
#     for i in range(2, n+1):
#         ans *= i
#     return ans



# n = int(input())
# ans = fac(n)
# ans = list(map(int, str(ans)))
# ans = ans[::-1]

# cnt = 0
# for i in ans:
#     if i == 0:
#         cnt+=1
#     else:
#         break3

# print(cnt)


# n = int(input())
# k = int(input())

# def func(n):
#     ans = 0
#     for i in range(1, n+1):
#         temp = n**2 // (k * i)
#         if temp > n:
#             temp = n
        
#         ans += temp
#     return ans

# left = 1
# right = n ** 2
# while left <= right:
#     mid = (left + right) // 2
#     temp = func(mid)
#     if temp < k:
#         left = mid + 1
#     elif temp >= k:
#         right = mid - 1

# print(right)



import heapq
def dijkstra(graph, start):
    distences = {node: float('inf') for node in graph}
    distences[start] = 0
    queue = [(0, start)]

    while queue:
        current_distence, current_node = heapq.heappop(queue)

        if current_distence > distences[current_node]:
            continue
      
        for neighbor, weight in graph[current_node]:
            distence = current_distence + weight

        if distence < distence[neighbor]:
            distence[neighbor] = distence
            heapq.heappush(queue, (distence, neighbor))

    return distences
        
