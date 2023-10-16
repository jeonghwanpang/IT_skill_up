# 백준 10814번 나이순 정렬 (실버5)

# idea
# 2차원 배열으로 나이, 이름을 입력 받고
# 나이 순으로만 정렬한다. (이름은 정렬 안 되게)

import sys

list1 = []

for i in range(int(input())):
  age, name = map(str, sys.stdin.readline().split())
  list1.append([age, name])

list1.sort(key=lambda x: int(x[0]))

for age, name in list1:
  print(age, name)

# print(list1)