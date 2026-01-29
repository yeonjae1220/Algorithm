"""
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

key_note = {}

for _ in range(N):
    site, pw = input().split()
    key_note[site] = pw


for _ in range(M):
    find = input().strip()
    print(key_note[find])