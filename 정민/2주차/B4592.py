# 중복을 없애자

# 입력
# 5 1 22 22 22 3
# 4 98 76 20 76
# 6 19 19 35 86 86 86
# 1 7
# 0

# 출력
# 1 22 3 $
# 98 76 20 76 $
# 19 35 86 $
# 7 $

while True:
  a = list(map(int, input().strip().split()))

  if a[0] == 0:
    break

  for i in range(1, len(a)):
    if i == 1:
      print(a[i], end = " ")
    elif a[i] != a[i-1]:
      print(a[i], end = " ")
  print("$")