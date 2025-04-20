def negativeinput():
  a = int(input("Enter a number: "))
  if a > 0:
    print('Positive')
    negativeinput()
  else:
    print('Negative')
    return
negativeinput()
