# 백준 24051번 알고리즘 수업 - 삽입 정렬1 (브론즈1)

# insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
#     for i <- 2 to N {
#         loc = i - 1;
#         newItem = A[i];

#         # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
#         while (1 <= loc and newItem < A[loc]) {
#             A[loc + 1] <- A[loc];
#             loc--;
#         }
#         if (loc + 1 != i) then A[loc + 1] = newItem;
#     }
# }

import sys

def insertion_sort(arr, n, k):
  count = 0

  for i in range(1, n):
    loc = i - 1
    newItem = arr[i]
        
    while 0 <= loc and newItem < arr[loc]:
      arr[loc + 1] = arr[loc]
      loc -= 1
      count += 1

      if count == k:
        return arr[loc + 1]
        
    if loc + 1 != i:
      arr[loc + 1] = newItem  
      count += 1

      if count == k:
        return arr[loc + 1]
      
  return -1


n, k = map(int, sys.stdin.readline().split())
print(insertion_sort(list(map(int, sys.stdin.readline().split())), n, k))

# n, k = map(int, input().split())
# print(insertion_sort(list(map(int, input().split())), n, k))