# 백준 20115번 에너지 드링크 (실버3)

# idea
# 역순으로 정렬
# 2개 합친 드링크량이 다음 드링크량 보다 많으면, 드링크의 반을 버림
# 적으면, 합친 드링크의 반을 버림
# 출력 시, 정수이면 정수로 출력하기

import sys

n = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
list1.sort(reverse=True)

energy = list1[0]

for i in range(1, n):
  if energy > list1[i]:
    energy += list1[i] / 2
  else:
    energy = energy / 2 + list1[i]


if energy.is_integer():
  print(int(energy))
else:
  print(energy)

