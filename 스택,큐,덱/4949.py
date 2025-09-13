import sys
while True:
    s = sys.stdin.readline().rstrip()
    stack = []

    if s == ".":
        break
    
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')' or s[i] == ']':
            if len(stack) == 0:
                stack.append(s[i])
                break
            elif(s[i] == ')'):
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif(s[i] == ']'):
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
    
    if(len(stack) == 0):
        print("yes")
    else:
        print("no")
