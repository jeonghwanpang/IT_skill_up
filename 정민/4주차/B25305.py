#백준 25305번 커트라인 (브론즈2)

import sys
input = sys.stdin.readline

list1 = []

n, k = map(int, input().split())

list1 = list(map(int, input().split()))
list1.sort(reverse=True)

print(list1[k-1])


