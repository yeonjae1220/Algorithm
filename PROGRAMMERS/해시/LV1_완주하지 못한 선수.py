"""
PROGRAMMERS.LV1_완주하지 못한 선수의 Docstring

간단 정답
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


"""

def solution(participant, completion):
    dict = {}
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    answer = ''
    
    for c in completion:
        dict[c] -= 1
    
    
    for key in dict:
        if dict[key] != 0:
            answer += key
            
    return answer
