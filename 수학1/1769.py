import sys
input = sys.stdin.readline

n = input().strip()


cnt = 0

while len(n) > 1:
    sum = 0
    for i in n:
        sum += int(i)

    n = str(sum)
    cnt += 1
        

print(cnt)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")
    

