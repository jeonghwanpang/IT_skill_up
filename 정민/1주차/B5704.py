while True:
  count = 0

  text = input()

  if text in ["*"]:
    break

  small = 97
  for j in range(26):
    n = text.find(chr(small))

    if n==-1:
      break
    count+=1
    small += 1

  if count == 26:
    print("Y")
  else:
    print("N")

    
      
