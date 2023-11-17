# 백준 1912번 연속합 (실버2)

n = int(input())

list1 = list(map(int, input().split()))

result = [list1[0]]
for i in range(1, n):
  result.append(max((result[i-1] + list1[i]), list1[i]))

print(max(result))