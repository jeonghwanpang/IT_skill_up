# 백준 23881번 알고리즘 수업 - 선택 정렬1 (브론즈1)

# selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
#     for last <- N downto 2 {
#         A[1..last]중 가장 큰 수 A[i]를 찾는다
#         if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
#     }
# }

import sys

def selection_sort(arr, n, k):
  count = 0

  for last in range(n-1, 0, -1):
    max_idx = 0
    for i in range(1, last + 1):
      if arr[i] > arr[max_idx]:
        max_idx = i
    if last != max_idx:
      arr[last], arr[max_idx] = arr[max_idx], arr[last]
      count += 1

    if count == k:
      print(arr[max_idx], arr[last])

  if count < k:
    print('-1')

  # print(count)


n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

selection_sort(arr, n, k)
# print(arr)


