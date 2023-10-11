# 백준 1439번 뒤집기 (실버5)

# idea
# 현재 문자가 이전 문자와 다르면 새로운 덩어리가 시작된 거
# -> 해당하는 카운터 증가
# 더 적은 덩어리의 개수를 출력

import sys

n = sys.stdin.readline().strip()

zero = one = 0
prev = ''

for i in n:
  if i != prev:
    if i == '0':
      zero += 1
    else:
      one += 1
  prev = i

print(min(zero, one))

  
