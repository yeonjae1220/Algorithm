import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
FRIEND_LIMIT = 200001

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return size[a]

    if a < b:
        parent[b] = a
        size[a] += size[b]
        return size[a]
    else:
        parent[a] = b
        size[b] += size[a]
        return size[b]



T = int(input())
for _ in range(T):
    F = int(input())

    relation_cnt = 0
    friend_dict = {}
    fri_cnt = 0

    parent = [0] * FRIEND_LIMIT
    for i in range(FRIEND_LIMIT): # 배열 초기화 잊지 않기
        parent[i] = i

    size = [1] * FRIEND_LIMIT

    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in friend_dict:
            friend_dict[f1] = fri_cnt
            fri_cnt += 1
        
        if f2 not in friend_dict:
            friend_dict[f2] = fri_cnt
            fri_cnt += 1

        a = find_parent(friend_dict[f1])
        b = find_parent(friend_dict[f2])

        
        relation_cnt = union_parent(a, b)
        # temp = parent[0] # 첫번째 & 두번째 친구의 parent값은 동일 > 이거 말고 다른 방법 찾아야 함
        # relation_cnt = parent.count(temp)

        
        print(relation_cnt)
    




    

    



# 처음 입력받은 두 친구 와 모두 친구인 관계를 찾아야 함
# 둘의 parent[x]와 같은 애들 수를 입력 받을 때마다 count 해주면 될 듯 하긴 함
# 오름차순 숫자가 아닌 이름이 들어왔을 때의 처리?
# 딕셔너리 만들어서 value 값을 cnt로 카운트 하면 숫자로 처리 가능할 듯 <- 이거 아님. 제일 상위 부모는 맞지만, 나머지는 자신의 바로 위 부모를 반환함
# parnet 배열의 크기는 문제 조건의 친구 관계 수 100000을 넘지 않음. 최대 200000 

# find_parent 찾으면서 그 안에 최상위 부모 가 있으면 (같은 그래프 이면) 합산.