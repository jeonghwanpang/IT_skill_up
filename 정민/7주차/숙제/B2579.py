# 백준 11727번 2×n 타일링 2 (실버3)

n = int(input())

list1 = [1, 1]

for i in range(2, n+1):
  list1.append(list1[i-2] * 2 + list1[i-1])

print(list1[n] % 10007)
