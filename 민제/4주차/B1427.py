#백준 1427 소트인사이드

#idea
# 문자열을 리스트로 입력받아 sort내장함수로 정렬해준다.

print(''.join(map(str,sorted(list(map(int,input())),reverse=True))))