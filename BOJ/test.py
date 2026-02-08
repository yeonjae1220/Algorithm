import sys
input = sys.stdin.readline

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



# import heapq
# def dijkstra(graph, start):
#     distences = {node: float('inf') for node in graph}
#     distences[start] = 0
#     queue = [(0, start)]

#     while queue:
#         current_distence, current_node = heapq.heappop(queue)

#         if current_distence > distences[current_node]:
#             continue
      
#         for neighbor, weight in graph[current_node]:
#             distence = current_distence + weight

#         if distence < distence[neighbor]:
#             distence[neighbor] = distence
#             heapq.heappush(queue, (distence, neighbor))

#     return distences
        


# import sys
# input = sys.stdin.readline

# n = int(input())

# if 620 <= n <= 780:
#     print("Red")
# elif 590 <= n < 620:
#     print("Orange")
# elif 570 <= n < 590:
#     print("Yellow")
# elif 495 <= n < 570:
#     print("Green")
# elif 450 <= n < 495:
#     print("Blue")
# elif 425 <= n < 450:
#     print("Indigo")
# elif 380 <= n < 425:
#     print("Violet")

# else:
#     print("Out of Range")



# import sys
# input = sys.stdin.readline

# W, P = map(int, input().split())

# partition = list(map(int, input().split()))
# partition.append(0)
# partition.append(W)
# partition.sort(reverse=True)
# ans = set()

# n = len(partition)

# for i in range(0,n - 1):
#     for j in range(i + 1, n):
#         ans.add(partition[i] - partition[j])

# result = sorted(list(ans))
# print(*result)



"""
9084 dp 문제
"""

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     coin = list(map(int, input().split()))
#     M = int(input())

#     dp = [0] * (M + 1)
#     dp[0] = 1

#     for c in coin:
#         for i in range(1, M + 1):
#             if i - c >= 0:
#                 dp[i] += dp[i - c]
    
#     print(dp[M])


"""
1535 dp문제
"""
# N = int(input())
# demage = [0] + list(map(int, input().split()))
# happy = [0] + list(map(int, input().split()))

# dp = [[0] * 100 for _ in range(N + 1)]

# for i in range(1, N + 1):
#     for j in range(1, 100):
#         if demage[i] <= j:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-demage[i]] + happy[i])
#         else:
#             dp[i][j] = dp[i-1][j]
    
# print(dp[N][99])


