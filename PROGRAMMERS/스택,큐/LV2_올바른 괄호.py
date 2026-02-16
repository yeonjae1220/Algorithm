def solution(s):
    q = []
    for c in s:
        if c == '(':
            q.append('(')
        else:
            if not q:
                return False
            else:
                q.pop()
        
    
    if q:
        return False
    else:
        return True
    