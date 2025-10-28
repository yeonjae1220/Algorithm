# 1
# 23
# 4567

# 425 1 637 inorder
# 452 673 1 postorder

# postorder 마지막이 root node
# root node 중심으로 왼쪽, 오른쪽이 서브트리들. 
# postorder[-2] 가 오른쪽 sub tree의 root node? 근데 오른쪽 서브트리가 없을 수 도 있잖아

# postorder에서 노드들의 순서가 inorder left subtree, right subtree, rootnode로 나옴
# postorder에서 나눠진 리스트의 가장 오른쪽이 그부분 subtree의 root node

# 숫자 알 필요 없이 그냥 길이만 알면 루트 노드 알 수 있음
# [0 ~ mid_idx - 1], mid_idx, [mid_idx + 1:len(list) - 1]
# mid_idx - 1 이랑 (mid_idx - 1) * 2 이게 left, right의 루트

# 이제 이거 재귀 돌려야함

# postorder[-1] 루트로 출력
# inorder에서 저 루트값의 idx 찾기
# 왼쪽 오른쪽 길이 구하기
# postorder에서 왼쪽 끝, 오른쪽 끝 루트노드 확인하고 각각 자르기
# import sys
# sys.setrecursionlimit(10**6)

# n = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))

# # 향후 루트 인덱스를 찾게되므로 미리 맵핑해둠
# in_order_index = {value: index for index, value in enumerate(inorder)}

# ans = []


# def preorder_x(postorder_list):
#     if not postorder_list:
#         return
#     root_node = postorder_list[-1]
#     mid_idx = inorder.index(root_node)

#     ans.append(root_node)
#     if len(postorder_list) > 1:
#         preorder(postorder_list[0:mid_idx])
#         preorder(postorder_list[mid_idx:-1])


# def preorder(start, end):
#     if start > end:
#         return
#     root_node = postorder[end]
#     mid_idx = inorder.index(root_node)

#     ans.append(root_node)
#     if end - start > 0:
#         preorder(start, mid_idx - 1)
#         preorder(mid_idx, end - 1)


# preorder(0, len(postorder) - 1)
# print(*ans)



### 참고
# 비효율적인 리스트 슬라이싱:
# preorder(postorder_list[0:mid_idx]) 와 같이 재귀 호출 시마다 리스트를 잘라 
# 새로운 리스트를 만드는 것은 매우 비효율적입니다. 
# 매번 새로운 메모리를 할당하고 값을 복사하는 과정에서 많은 시간이 소요됩니다.

# 애초에 문자열 슬라이싱으로 하니 메모리 초과 뜨네





import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline # 빠른 입력을 위해 추가

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 1. inorder의 값별 인덱스를 미리 저장하여 O(1) 조회가 가능하게 합니다. (시간 초과 해결)
position = [0] * (n + 1)
for i in range(n):
    position[inorder[i]] = i

# 2. inorder와 postorder의 범위를 모두 인자로 넘겨 올바른 재귀 로직을 구현합니다.
def get_preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건
    if in_start > in_end or post_start > post_end:
        return

    # postorder의 마지막 노드가 현재 서브트리의 루트입니다.
    root = postorder[post_end]
    print(root, end=' ')

    # inorder에서 루트의 위치를 O(1)로 찾습니다.
    root_idx_inorder = position[root]
    
    # inorder에서 찾은 루트 위치를 기준으로 왼쪽 서브트리의 크기를 계산합니다.
    # 이것이 이 문제의 핵심입니다!
    left_subtree_size = root_idx_inorder - in_start

    # 왼쪽 서브트리 탐색
    get_preorder(
        in_start,                         # inorder 시작
        root_idx_inorder - 1,             # inorder 끝
        post_start,                       # postorder 시작
        post_start + left_subtree_size - 1  # postorder 끝
    )
    
    # 오른쪽 서브트리 탐색
    get_preorder(
        root_idx_inorder + 1,             # inorder 시작
        in_end,                           # inorder 끝
        post_start + left_subtree_size,   # postorder 시작
        post_end - 1                      # postorder 끝
    )

# 전체 범위를 대상으로 첫 재귀 함수를 호출합니다.
get_preorder(0, n - 1, 0, n - 1)