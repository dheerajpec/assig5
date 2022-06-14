lowerrange1= input("Enter the lower range")
lowerrange=int(lowerrange1)
upperrange1= input("Enter the upper range")
upperrange=int(upperrange1)
n= int(input("enter the number"))
i= lowerrange+1#to keep the starting and end not included
while i<upperrange:
    if(i%n==0):
        print(i)
    i=i+1
