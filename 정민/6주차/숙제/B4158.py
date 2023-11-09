# 백준 4158번 CD (실버5)

import sys

def binary_search_iterative(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1  
        elif arr[mid] > target:
            end = mid - 1  
        else:
            start = mid + 1  

    return -1  

while True:
  n, m = map(int, input().split())

  if n == 0 and m == 0:
    exit(0)

  list1 = []
  list2 = []

  count = 0
  
  for _ in range(n):
    list1.append(int(sys.stdin.readline()))

  for _ in range(m):
    if binary_search_iterative(list1, int(sys.stdin.readline())) == 1:
      count += 1

  print(count)