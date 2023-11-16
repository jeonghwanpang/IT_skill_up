# 백준 1012번 유기농 배추 (실버2)

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(arr, x, y):
    if x <= -1 or y <= -1 or x >= len(arr[0]) or y >= len(arr):
        return
    
    if arr[y][x] == 0:
        return

    arr[y][x] = 0
    dfs(arr, x - 1, y)
    dfs(arr, x + 1, y)
    dfs(arr, x, y - 1)
    dfs(arr, x, y + 1)
    return


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    count = 0

    for a in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for a in range(len(arr)):
        for b in range(len(arr[a])):
            if arr[a][b] == 1:
                count += 1
                dfs(arr, b, a)
                
    print(count)

