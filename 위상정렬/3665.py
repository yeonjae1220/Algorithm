import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    teams = list(map(int, sys.stdin.readline().split()))

    graph = {}
    for i in range(1, N + 1):
        graph[i] = []

    depth = [0 for _ in range(N + 1)]
    
    for i in range(N):
        for j in range(i + 1, N):
            graph[teams[i]].append(teams[j])
            depth[teams[j]] += 1
        
    
    m = int(sys.stdin.readline())



    for i in range(1, m + 1):
        a, b = map(int, sys.stdin.readline().split())
        rank_a = teams.index(a)
        rank_b = teams.index(b)

        # 만약 a가 더 순위가 높았다면 (인덱스가 작다면)
        if rank_a < rank_b:
            # 기존 간선 a -> b 를 b -> a 로 뒤집음
            graph[a].remove(b)
            graph[b].append(a)
            depth[b] -= 1
            depth[a] += 1
        else: # b가 더 순위가 높았다면
            # 기존 간선 b -> a 를 a -> b 로 뒤집음
            graph[b].remove(a)
            graph[a].append(b)
            depth[a] -= 1
            depth[b] += 1


    temp_arr = []
    is_ambiguous = False
    queue = deque()
    # 진입 차수가 0인 모든 노드를 큐에 추가
    for i in range(1, N + 1):
        if depth[i] == 0:
            queue.append(i)
            
    while queue:
        if len(queue) > 1:
            is_ambiguous = True
            break   
        temp = queue.popleft()
        temp_arr.append(temp)
        for j in graph[temp]:
            depth[j] -= 1
            if depth[j] == 0:
                queue.append(j)

      # 5. 최종 결과 판별
    if is_ambiguous:
        print("?")
    elif len(temp_arr) < N: # 모든 노드를 방문하기 전에 정렬이 끝났다면 사이클 존재
        print("IMPOSSIBLE")
    else:
        print(*temp_arr)

        
    


# 바뀐 것들 depth 측정해서 한번도 안바뀐 것들 자리 고정해두고 빈칸에 이전 위상정렬 줄 세우기 한것처럼?
# 기존 순위랑 같은데 변경 사항도 같으면 예외 처리