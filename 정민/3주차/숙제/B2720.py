# 백준 2720번 세탁소 사장 동혁 (브론즈3)

# idea
# 버림나눗셈 후 출력
# 현재 돈 -= 몫 * 단위
# 다음 단위 연산 수행

import sys

rest = [25, 10, 5, 1]

t = int(input())

for i in range(t):
  money = int(sys.stdin.readline().strip())

  for item in rest:
    n = money // item
    print(n, end=' ')
    money -= n * item
  print()
