a= ['dheeraj','dheeraj','vaibhav','gursimar','amisha','vaibhav','kundu','kundu']
for i in a:
    g=0
    n=0
    if(i=='----'):
        continue

    for j in a:
        if(i==j):
            n=n+1
            a[g]='----'
        g=g+1
    print(i," occured ",n," times")
    
            
