"""
ans 배열이랑 queue 하나 두고
공백 포함 문자열 큐로 쭉 받다가 < 나오면, 큐에 있는거 뒤집어서 ans에 추가
< 나오면 > 나올때 까지 큐로 쭉 받다가 그대로 ans에 추가


"""
import sys
from collections import deque
input = sys.stdin.readline

query = list(input().strip())

ans = []
q = deque()

i = 0
while i < len(query):
    if query[i] == '<':
        ans.extend(list(q)[::-1])
        q.clear()

        while query[i] != '>':
            ans.append(query[i])
            i += 1
        ans.append('>')
    
    elif query[i] == ' ':
        ans.extend(list(q)[::-1])
        ans.append(' ')
        q.clear()

    else:
        q.append(query[i])

    i += 1
        

if q:
    ans.extend(list(q)[::-1])

print(*ans, sep='')
        
        

