import math
a=int(input("ENTER THE FIRST SIDE: "))# first side
b=int(input("ENTER THE second SIDE: "))# second side
c=int(input("ENTER THE third SIDE: "))# third side
if(a+b>c and b+c>a and c+a>b):
  s=(a+b+c)/2
  area= math.sqrt(s*(s-a)*(s-b)*(s-c))
  print('Area of the triangle: ',area)
else: 
  print('Triangle not possible with given dimentions')
  
