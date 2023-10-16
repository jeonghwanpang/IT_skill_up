# 백준 1758번 알바생 강호 (실버4)

# idea
# 팁이 큰 순서대로 정렬한다.
# 팁 계산식 : 팁 - i (i는 0부터 시작하니까)
# 만약 계산한 팁이 0보다 작으면 pass

import sys

n = int(input())
list1 = []

for _ in range(n):
  list1.append(int(sys.stdin.readline().strip()))
list1.sort(reverse=True)

sum = 0
for i in range(n):
  money = list1[i] - i

  if money >= 0:
    sum += money 

print(sum)

