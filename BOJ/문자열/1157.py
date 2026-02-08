a = input().upper()
alpha_list = list(set(a))
cnt = []
for i in alpha_list:
    cnt.append(a.count(i))

if(cnt.count(max(cnt)) >= 2):
    print('?')
else:
    print(alpha_list[cnt.index(max(cnt))])
    
