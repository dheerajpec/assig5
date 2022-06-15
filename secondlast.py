a=[0,0,0,0,0,0,0,0,0,0]# initially taken zero for declaration purpose to fill the values afterward
k=0
while k<10:
    a[k]= int(input("Enter the number: "))
    k=k+1
print('The positive number out of the entered nos. are: ')
for i in a:
    if(i>0):
        print(i)
print('The negative number out the nos. are: ')
for i in a:
    if(i<0):
        print(i)
print('even no out of the entered nos: ')
for i in a:
    if(i%2==0):
        print(i)
print('odd no out of the entered nos: ')
for i in a:
    if(not(i%2==0)):# not because if the condition comes false means it is odd and we need to print it so to get into the if statement not used
        print(i)
print('Frequecy of respective nos are: ')
for i in a:
    if(type(i)==float):# so no repetition occurs
        continue
    n=0
    j=0
    while j<10:
        if(a[j]==i):
            n=n+1
            a[j]=1.1# an decimal no which would be used afterwards to distinguish it from other int values
        j=j+1
    print('Frequency of ',i,'is :',n)
            
            
