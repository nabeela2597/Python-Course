n = int(input('ENter the number whose sum you want to find: '))

s = 0

for i in range(1, n+1):
    s += i
    print('Sum = ', s)