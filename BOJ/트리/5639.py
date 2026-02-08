# root node는 첫번째
# 이전 노드와 비교해서 작으면 left child로.  
# 이전 노드와 비교해서 크고 이전 노드의 부모노드 보다 작으면 해당 노드의 right child. 
# 이전 노드와 비교해서 크고, 이전 노드의 부모노드 보다도 크면 그 다음 노드의 right child.

import sys
sys.setrecursionlimit(10**6)
pre = []
while True:
    line = sys.stdin.readline().strip() 
    if not line: # 더 이상 읽을 줄이 없으면 멈춤
        break
    pre.append(int(line))


def postorder(start, end):
    if start > end:
        return
    
    mid = end + 1 # 아무것도 안걸리면 다음 재귀때 return되게

    for i in range(start + 1, end + 1):
        if pre[start] < pre[i]:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(pre[start])

postorder(0, len(pre) - 1)