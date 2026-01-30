"""
11723의 Docstring
Set 연산으로 푸니 계속 메모리 초과 난다
"""


# import sys
# input = sys.stdin.readline

# def add(n):
#     Set.add(n)

# def remove(n):
#     Set.discard(n)
    
# def check(n):
#     if n in Set:
#         ans.append(1)
#     else:
#         ans.append(0)

# def toggle(n):
#     if n in Set:
#         Set.discard(n)
#     else:
#         Set.add(n)

# def all():
#     global Set
#     Set = set([i for i in range(1, 21)])

# def empty():
#     global Set
#     Set = set()


# Set = set()
# T = int(input())
# ans = []
# for _ in range(T):
#     query = input().strip().split()

#     if len(query) == 1:
#         if query[0] == "all":
#             all()
#         else:
#             empty()
    
#     else:
#         q = query[0]
#         n = int(query[1])

#         if q == "add":
#             add(n)
#         elif q == "remove":
#             remove(n)
#         elif q == "check":
#             check(n)
#         elif q == "toggle":
#             toggle(n)
#         else:
#             print("query not exist")


# for i in ans:
#     print(i)

"""
비트 마스킹으로 풀기
"""
import sys
input = sys.stdin.readline

arr = bytearray(21)
ans = []

T = int(input())

for _ in range(T):
    cmd = input().strip().split()

    if cmd[0] == "add":
        arr[int(cmd[1])] = 1
    elif cmd[0] == "remove":
        arr[int(cmd[1])] = 0
    elif cmd[0] == "check":
        # ans.append(arr[int(cmd[1])])
        print(arr[int(cmd[1])])
    elif cmd[0] == "toggle":
        x = int(cmd[1])
        arr[x] ^= 1
    elif cmd[0] == "all":
        for i in range(1, 21):
            arr[i] = 1

    elif cmd[0] == "empty":
        for i in range(1, 21):
            arr[i] = 0

# print("\n".join(map(str, ans)))