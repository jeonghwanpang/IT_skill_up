# 백준 4796번 캠핑 (브론즈1)

# idea
# (V // P) * L + V % P
# L, P, V가 모두 0일 때 종료

# else 부분 예시
# V일짜리 휴가, P일 중 L일동안만
# 11일짜리 휴가, 7일 중 2일 동안만 (입력: 2 7 11)

n = 1

while True:
  L, P, V = map(int, input().split())

  if L == 0 and P == 0 and V == 0:
    break

  if V % P <= L:
    print('Case {}: {}'.format(n, (V // P) * L + V % P))
  else:
    print('Case {}: {}'.format(n, (V // P) * L + L))
  n += 1