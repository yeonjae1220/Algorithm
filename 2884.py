a, b = map(int, input().split())

if (b - 45) >= 0:
    print(f"{a} {b-45}")
else:
    if a == 0:
        print(f"23 {60 - (45 - b)}")
    else:
        print(f"{a-1} {60 - (45 - b)}")