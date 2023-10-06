import sys

dict_a = {}

for _ in range(int(input())):
  key, value = map(str, sys.stdin.readline().split())
  
  if value == "enter":
    dict_a[key] = value
  else:
    del dict_a[key]

for key in dict(sorted(dict_a.items(), reverse = True)):
  print(key)