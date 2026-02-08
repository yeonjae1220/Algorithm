

def code1(n):
    global cnt1
    
    if (n == 1 or n == 2):
        cnt1 += 1
        return 1
    else:
        return code1(n - 1) + code1(n - 2)
    
def code2(n):
    global cnt2
    global f
    for i in range(3, n + 1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


n = int(input())

f = [0] * (n + 1)
f[1] = 1
f[2] = 1

cnt1 = 0
cnt2 = 0

code1(n)
code2(n)
print(cnt1, cnt2)


    
    


