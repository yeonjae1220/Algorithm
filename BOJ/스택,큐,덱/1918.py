"""
1918의 Docstring
분할정복으로?
사칙연산 바꿔주는 함수 만들기
먼저 * 부터 처리
나머지 + 들 처리
후 완성된 후위 표기식 반환

이걸 전체 query에서 () 안에 있는 것들 각각 처리하고 
마지막으로 한번더 함수 돌려주기
"""


"""
뭔가 구현도 잘못된 방법이고 문법적인 오류도 있다.
특히 중첩 괄호를 처리 못함
"""

# import sys
# input = sys.stdin.readline

# query = input().strip()

# def cal(q):
#     stack_ans = []
#     stack_cal = []

#     for c in q:
#         if c.isalpha():
#             stack_ans.append(c)
#         else:
#             if c == "+" or c == "-":
#                 stack_cal.append(c)
#             else:
#                 stack_ans.append(c).extend(stack_cal[::-1])
#                 stack_cal = []
#     return stack_ans
    
# for i in range(len(query)):
#     left, right = 0, 0
#     if query[i] == "(":
#         left = i
    
#     if query[i] == ")":
#         right = i
#         query = query[:left].extend(cal(query[left:right])).extend(query[right:])


# print(query)



import sys
input = sys.stdin.readline

query = input().strip()

def cal(q):
    stack_ans = []
    stack_cal = []

    for c in q:
        if c.isalpha():
            stack_ans.append(c)
        else:
            if c == "+" or c == "-":
                stack_cal.append(c)
            else:
                stack_ans.append(c).extend(stack_cal[::-1])
                stack_cal = []
    return stack_ans
    
for i in range(len(query)):
    left, right = 0, 0
    if query[i] == "(":
        left = i
    
    if query[i] == ")":
        right = i
        query = query[:left].extend(cal(query[left:right])).extend(query[right:])


print(query)



import sys
input = sys.stdin.readline

query = input().strip()
print(cal(query))


            


            
