while True:
    a = input()
    answer = 'Y'

    if a == '*':
        break 

    else:
        for i in range(97, 123):
            if a.find(chr(i)) == -1:
                answer ='N'
                break
    
        print(answer)