# 백준 2579번 계단 오르기 (실버3)


n = int(input())
list1 = []
for _ in range(n):
  list1.append(int(input()))

# result = [list1[0], (list1[0]+list1[1]), (max(list1[0], list1[1]) + list1[2])]

# for i in range(3, min(n+1, len(list1))):
#   result.append(max(list1[i-2], list1[i-1]) + list1[i])

# print(result[1] + result[n-1])

result = []
if len(list1) <= 2: 
    print(sum(list1))
else: 
  result = [list1[0], list1[0]+list1[1], (max(list1[0], list1[1]) + list1[2])]

  for i in range(3, n):
    result.append(max(result[i-3] + list1[i-1] + list1[i], result[i-2] + list1[i]))
    # 2계단 연속 뛰기 vs 1계단 건너 뛰기

  print(result[-1])
