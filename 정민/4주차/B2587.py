# 백준 2587번 대표값2 (브론즈2)

import sys

list1 = []
for _ in range(5):
  list1.append(int(sys.stdin.readline()))
list1.sort

print(list1)

print(int(sum(list1)/5))
print(list1[2])








