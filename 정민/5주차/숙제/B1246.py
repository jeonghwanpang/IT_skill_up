# 백준 1246번 온라인 판매 (실버4)

# idea
# 현재 수익보다 현재 달걀로 판매하는 수익이 더 클 경우
# 수익과 책정 가격을 초기화한다.

import sys

n, m = map(int, sys.stdin.readline().split())

list1 = []
for _ in range(m):
  list1.append(int(input()))
list1.sort()

price = 0
profit = 0

for i in range(m):
  egg = min(m - i, n) # 달걀 수가 사람 수보다 작을 경우

  if profit < list1[i] * egg:
    profit = list1[i] * egg 
    price = list1[i] 
    

print(price, profit)