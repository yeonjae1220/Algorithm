n, m = map(int, input().split())
dict_num = {}
dict_name = {}
for i in range(n):
    name = input().strip()
    dict_num[name] = i + 1
    dict_name[i + 1] = name

for i in range(m):
    query = input().strip()
    if (query.isdigit()):
        print(dict_name[int(query)])
    else:
        print(dict_num[query])
        
# isalpha 썼었는데 안됬음

