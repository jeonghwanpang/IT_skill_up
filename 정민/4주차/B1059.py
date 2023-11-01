# 백준 1059번 좋은 구간 (실버4)

import sys

L = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
n = int(input())

if n in list1:
  print(0)
else:
  list1.append(n)
  list1.sort()

  idx = list1.index(n)

  # 만약 n이 리스트의 첫 번째에 추가될 경우
  if idx == 0:  
    num = list1[idx+1] - n

    print(num * n - 1)

  else: 
    num1 = n - list1[idx-1]
    num2 = list1[idx+1] - n

    print(num1 * num2 - 1)


