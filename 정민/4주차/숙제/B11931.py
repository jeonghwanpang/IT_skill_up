# 백준 11931번 수 정렬하기 4 (실버5)

import sys

list1 = []

for _ in range(int(input())):
  list1.append(int(sys.stdin.readline()))

list1.sort(reverse=True)

for i in list1:
  print(i)