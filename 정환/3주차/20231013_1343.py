#왼쪽부터! xxxx 를 'AAAA'로 바꾸고 XX 를 BB로 바꾼다.
# 바꿨는데 x가 남아있다면? 이건 안되는거다.. -1 출력해라
board = input()
board.replace('XXXX','AAAA')
board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)