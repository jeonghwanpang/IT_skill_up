import sys

input = sys.stdin.readline

n, m = map(int, input().split())
list1 = [int(input()) for _ in range(m)]
list1.sort(reverse=True)

price = -1
profit = -1
loop = m if n > m else n
for i in range(loop):
    temp = list1[i] * (i + 1)

    if profit <= temp:
        profit = temp
        price = list1[i]

print(price, profit)
