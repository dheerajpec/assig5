for i in range(1,6):# this will print the first half
    for j in range(0,i):
        print('*', end='')
    print()# this will change the line
for i in range(0,5):# this will print the second half
    j=4-i
    while(j>0):
        print('*', end='')
        j=j-1
    print()
