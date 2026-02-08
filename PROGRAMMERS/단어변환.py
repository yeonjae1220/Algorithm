"""
단어변환의 Docstring

target의 단어로 하나씩 바꾸는 게 아닌
기존 단어에서 하나씩 바꾸는 words에 있는 걸 큐에 넣어가기

덜 품

"""



from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

word_len = len(begin)

visited = set()

def bfs():
    q = deque()
    q.append((begin, 0))
    visited.add(begin)

    while q:
        now, depth = q.popleft()
        if now == target:
            return depth
        for i in range(word_len):
            temp = list(now)
            temp[i] = target[i]
            temp = ''.join(temp)
            if temp not in visited and temp in words:
                q.append((temp, depth + 1))
                visited.add(temp)
        
    return 0

print(bfs())

          



    