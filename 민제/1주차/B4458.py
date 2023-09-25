#백준 4458번 첫 글자를 대문자로

#idea
#문자열의 첫번째 문자를 아스키코드로 변환후 -32해주고 다시 문자로 변환

for i in range(int(input())):
    str=input()
    if str[0]>='a' and str[0]<='z':
        print(str.replace(str[0],chr(ord(str[0])-32),1))
    else:
        print(str)