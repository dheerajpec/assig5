a1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=a1
n= int(input("enter the number: "))
for i in range(1,n+1):
    if len(a)<n:
        a=a+a1# in case the string exhuasts so it will again start from A and so on
    for j in range(0,i):
        print(a[j], end='')
    print()
    a=a[i:]
