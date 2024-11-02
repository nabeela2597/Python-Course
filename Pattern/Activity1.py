print('Half pyramid patterns of stars ')

r = int(input('enter the no of rows:'))

for i in range(r):
  for j in range(i+1):
    print('*', end=' ')
  print()