n = int(input())
queue = list(map(int, input().split()))
stack = []

count = 1
ans = True
while queue:
    person = queue.pop(0)
    if person == count:
        count += 1
    else:
        stack.append(person)
    
    while stack and stack[-1] == count:
        stack.pop()
        count += 1

while stack:
    if stack.pop() != count:
        ans = False
        break
    count += 1

if ans:
    print("Nice")
else:
    print("Sad")
        

    

    