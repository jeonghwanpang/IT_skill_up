#백준 28455번 Union Maplestory (브론즈2)

import sys


n = int(input())

list1 = []
for _ in range(n):
  list1.append(int(sys.stdin.readline()))
list1.sort(reverse=True)

sum1 = 0
sum2 = 0

if n < 42:
  for i in range(n):
    sum1 += list1[i]

    if list1[i] >= 250:
      sum2 += 5
    elif list1[i] >= 200:
      sum2 += 4
    elif list1[i] >= 140:
      sum2 += 3
    elif list1[i] >= 100:
      sum2 += 2
    elif list1[i] >= 60:
      sum2 += 1
else:
  for i in range(42):
    sum1 += list1[i]

    if list1[i] >= 250:
      sum2 += 5
    elif list1[i] >= 200:
      sum2 += 4
    elif list1[i] >= 140:
      sum2 += 3
    elif list1[i] >= 100:
      sum2 += 2
    elif list1[i] >= 60:
      sum2 += 1

print(sum1, sum2)


