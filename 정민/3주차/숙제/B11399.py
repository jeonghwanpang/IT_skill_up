# 백준 11399번 ATM (실버4)

# idea
# 리스트 정렬하고 더하면 되는 거 아닌가

import sys

n = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
list1.sort()

result = 0
for i in range(n):
  select = list1[0:i+1]
  result += sum(select)

print(result)
