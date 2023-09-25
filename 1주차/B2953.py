list_a = []

for j in range(5):
  result = 0
  p = input().split(' ')

  for i in range(4):
    result += int(p[i])

  list_a.append(result)

m = max(list_a)
print(list_a.index(m) + 1, m)