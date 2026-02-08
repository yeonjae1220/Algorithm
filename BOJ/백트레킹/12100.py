"""
12100의 Docstring

상하좌우 움직임 (한쪽 끝으로 정렬)
만약 같은 수가 붙어있다면 합쳐짐

그냥 이동 방향의 축 기준으로 각 숫자의 나열을 보고 축 기준으로 하나씩 순회하며 같은게 있으면 합치기
최대값 따로 분리해놓고 숫자 합쳐질 때 마다 검사 후 갱신
이렇게 상하좌우 각각 분기를 만들어서 백트레킹? 

보드의 크기는 1 ~ 20
최대 5번 이동
0은 빈칸

2^8 개의 경우의 수... 
시간 제한 1초에 메모리 제한 512MB면 그냥 다 찾아보는게 맞을 듯 함
"""

import sys
input = sys.stdin.readline


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

ans = max(map(max, graph)) # 초기 최대값

direction = [1, 2, 3, 4] # 상 하 좌 우

def move_graph(d, now_graph, largest):
    new_graph = [[0] * N for _ in range(N)]
    
    # i는 y축 j는 x축
    if d == 1:
        for j in range(N):
            idx = 0
            merged = False
            for i in range(N):
                if now_graph[i][j] != 0:
                    if now_graph[i][j] == new_graph[idx][j] and not merged:
                        new_graph[idx][j] *= 2
                        largest = max(largest, new_graph[idx][j]) # 최대값 갱신
                        merged = True
                    else:
                        if new_graph[idx][j] != 0:
                            idx += 1

                        new_graph[idx][j] = now_graph[i][j]
                        merged = False
                            
                
    
    elif d == 2:
        for j in range(N):
            idx = N - 1
            merged = False
            for i in range(N - 1, -1, -1):
                if now_graph[i][j] == 0:
                    continue
                if new_graph[idx][j] == now_graph[i][j] and not merged:
                    new_graph[idx][j] *= 2
                    largest = max(largest, new_graph[idx][j])
                    merged = True
                else:
                    if new_graph[idx][j] != 0:
                        idx -= 1
                    new_graph[idx][j] = now_graph[i][j]
                    merged = False

    elif d == 3:
        for i in range(N):
            idx = 0
            merged = False
            for j in range(N):
                if now_graph[i][j] == 0:
                    continue
                if new_graph[i][idx] == now_graph[i][j] and not merged:
                    new_graph[i][idx] *= 2
                    largest = max(largest, new_graph[i][idx])
                    merged = True
                else:
                    if new_graph[i][idx] != 0:
                        idx += 1
                    new_graph[i][idx] = now_graph[i][j]
                    merged = False

    else:
        for i in range(N):
            idx = N - 1
            merged = False
            for j in range(N - 1, -1, -1):
                if now_graph[i][j] == 0:
                    continue
                if new_graph[i][idx] == now_graph[i][j] and not merged:
                    new_graph[i][idx] *= 2
                    largest = max(largest, new_graph[i][idx])
                    merged = True
                else:
                    if new_graph[i][idx] != 0:
                        idx -= 1
                    new_graph[i][idx] = now_graph[i][j]
                    merged = False
            

    return new_graph, largest



ans_list = []

def backtraking(g, depth, largest):
    if depth == 5:
        # 최대값 리턴
        ans_list.append(largest)
        return
    
    for i in range(4):
        new_graph, temp_largest = move_graph(direction[i], g, largest)
        backtraking(new_graph, depth + 1, temp_largest)


backtraking(graph, 0, ans)

print(max(ans_list))



"""
현재 idx 위치에서 합쳐졌는지 안 합쳐 졌는지 merged로 체크 필요
"""