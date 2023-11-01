import sys

list1 = list(input())
list1.sort(reverse=True)

for i in list1:
  print(i, end='')
