"""
9375의 Docstring


"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    categories_set = set()
    cal_temp = {}

    if n == 0:
        print(0)
        continue

    for _ in range(n):
        name, category = input().split()

        if category in categories_set:
            cal_temp[category] += 1
        else:
            cal_temp[category] = 1
            categories_set.add(category)

    ans = 1
    for c in categories_set:
        ans *= (cal_temp[c] + 1)
    
    print(ans - 1)
        



    
    






