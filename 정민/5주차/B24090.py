# 백준 24090번 알고리즘 수업 - 퀵 정렬 1 (실버5)

# idea

# quick_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- partition(A, p, r);  # 분할
#         quick_sort(A, p, q - 1);  # 왼쪽 부분 배열 정렬
#         quick_sort(A, q + 1, r);  # 오른쪽 부분 배열 정렬
#     }
# }

# partition(A[], p, r) {
#     x <- A[r];    # 기준원소
#     i <- p - 1;   # i는 x보다 작거나 작은 원소들의 끝지점
#     for j <- p to r - 1  # j는 아직 정해지지 않은 원소들의 시작 지점
#         if (A[j] ≤ x) then A[++i] <-> A[j]; # i값 증가 후 A[i] <-> A[j] 교환
#     if (i + 1 != r) then A[i + 1] <-> A[r]; # i + 1과 r이 서로 다르면 A[i + 1]과 A[r]을 교환
#     return i + 1;
# }

import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# count = 0

def partition(A, p, r):
  global k
  x = A[r]  # 기준원소
  i = p - 1 # i는 x보다 작거나 작은 원소들의 끝지점
  for j in range(p, r): # j는 아직 정해지지 않은 원소들의 시작 지점
    if A[j] <= x:
      i += 1 # i값 증가 후
      A[i], A[j] = A[j], A[i] # A[i] <-> A[j] 교환

      k -= 1

      if k == 0:
        print(A[i], A[j])
        exit(0)

      # count += 1
      # if n == count:
      #   print(A[i], A[j])
      #   exit()

  if i + 1 != r: # i + 1과 r이 서로 다르면
    A[i + 1], A[r] = A[r], A[i + 1] # A[i + 1]과 A[r]을 교환

    k -= 1

    if k == 0:
      print(A[i+1], A[r])
      exit(0)
    
    # count += 1
    # if n == count:
    #   print(A[i], A[j])
    #   exit()

  return i + 1

def quick_sort(A, p, r):
  if p < r:
    q = partition(A, p, r)   # 분할
    quick_sort(A, p, q - 1)  # 오른쪽 부분 배열 정렬
    quick_sort(A, q + 1, r)  # 오른쪽 부분 배열 정렬


n, k = map(int, input().split())

# list1 = list(map(int, input().split()))
quick_sort(list(map(int, input().split())), 0, n - 1)

# if count < k:
#   print(-1)

if k > 0:
  print(-1)
