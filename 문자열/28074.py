import sys
input = sys.stdin.readline

# MOBIS = set()

input_string = input()

ans = True

if 'M' not in input_string:
    ans = False

elif 'O' not in input_string:
    ans = False

elif 'B' not in input_string:
    ans = False

elif 'I' not in input_string:
    ans = False

elif 'S' not in input_string:
    ans = False



if ans:
    print('YES')
else:
    print('NO')

