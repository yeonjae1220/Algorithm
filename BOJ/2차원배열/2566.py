table = []
for i in range(9):
    row = list(map(int, input().split()))
    table.append(row)

max = -1
col, cal = -1, -1
for i in range(9):
    for j in range(9):
        if table[i][j] > max:
            max = table[i][j]
            col, cal = i, j

print(max)
print(col + 1, cal + 1)

        