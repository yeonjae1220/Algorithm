croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for c in croatia:
    word = word.replace(c, "e") # 아무 알파벳 중복 안되는걸로

print(len(word))
