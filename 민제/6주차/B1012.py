# 백준 1012번 유기농 배추

# idea
# dfs를 통해 구현

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(arr, x, y):
    if x== -1 or y== -1 or x== len(arr[0]) or y== len(arr):
        return

    if arr[y][x] == 0 :
        return

    arr[y][x] = 0
    dfs(arr, x - 1, y)
    dfs(arr, x + 1, y)
    dfs(arr, x, y - 1)
    dfs(arr, x, y + 1)
    return


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    count = 0

    arr = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
                dfs(arr, j, i)

    print(count)
