import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(list(set(nums)))

dic = {sorted_list[i] : i for i in range(len(sorted_list))}

for i in nums:
    print(dic[i], end=" ")


