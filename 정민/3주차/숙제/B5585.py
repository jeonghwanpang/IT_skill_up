# 백준 5585번 거스름돈 (브론즈2)

# idea
# 1000 - 지불할돈
# 버림나눗셈 후 개수 더하기
# 현재 돈 -= 몫 * 단위
# 다음 단위 연산 수행

import sys

rest = [500, 100, 50, 10, 5, 1]

money = 1000 - int(sys.stdin.readline())

count = 0

for item in rest:
  n = money // item
  count += n
  money -= n * item

print(count)