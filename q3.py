a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n= int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(0,i):
        print(a[j], end='')
    print()
    a=a[i:]
