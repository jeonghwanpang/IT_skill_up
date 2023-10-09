import sys

list1 = []

n = int(input())

for i in range(n):
  # a = int(input())
  a = int(sys.stdin.readline())
  
  if a != 0:
    list1.append(a)
  elif a == 0:
    list1.pop()

print(sum(list1))

# result = 0
# for i in range(len(list1)):
#   result += list1[i]
# print(result)