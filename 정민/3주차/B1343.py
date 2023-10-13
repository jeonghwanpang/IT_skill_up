# 백준 1343번 폴리오미노 (실버5)

# idea
# XXXX를 찾아서 AAAA로 바꿔주고
# XX를 찾아서 BB로 바꿔준다.
# 만약 문자열에 X가 남아있으면 -1을 출력한다.

n = input()
n = n.replace('XXXX', 'AAAA')
n = n.replace('XX', 'BB')

if 'X' in n:
  print(-1)
else:
  print(n)



