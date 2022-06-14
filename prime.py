lowerrange1= input("Enter the lower range")
lowerrange=int(lowerrange1)
upperrange1= input("Enter the upper range")
upperrange=int(upperrange1)
for i in range(lowerrange,upperrange):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)
        
