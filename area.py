import math
a=int(input("ENTER THE FIRST SIDE: "))
b=int(input("ENTER THE second SIDE: "))
c=int(input("ENTER THE third SIDE: "))
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle: ',area)
