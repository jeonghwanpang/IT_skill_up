n = int(input())

for i in range(n):
  text = input()
  change = text.capitalize()
  text = text.replace(text[0], change[0], 1)
  
  print(text)