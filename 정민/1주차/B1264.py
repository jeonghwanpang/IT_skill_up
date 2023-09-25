list_a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
  count = 0

  text = input()

  if text in ["#"]:
    break

  for i in text:
    if i in list_a:
      count += 1
  print(count)
