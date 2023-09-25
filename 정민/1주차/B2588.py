a = input()
b = input()

list_a = []

for i in reversed(range(3)):
  n = int(b[i]) * int(a)
  print(n)
  list_a.append(n)

result = list_a[2] * 100 + list_a[1] * 10 + list_a[0]
print(result)
  

# result1 = int(b[2]) * int(a[0]) * 100 + int(b[2]) * int(a[1]) * 10 + int(b[2]) * int(a[2])
# print(result1)

# result2 = int(b[1]) * int(a[0]) * 100 + int(b[1]) * int(a[1]) * 10 + int(b[1]) * int(a[2])
# print(result2)

# result3 = int(b[0]) * int(a[0]) * 100 + int(b[0]) * int(a[1]) * 10 + int(b[0]) * int(a[2])
# print(result3)

# result4 = result1 + result2 * 10 + result3 * 100
# print(result4)


