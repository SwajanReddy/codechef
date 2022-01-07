# cook your dish here
for i in range(int(input())):
    k=int(input())
    x=[int(x) for x in input().split()]
    y=[int(y) for y in input().split()]
    c=0
    if(x[0]>=y[0]):
        c+=1
    for i in range(1,len(x)):
        if(x[i]>=x[i-1]):
            z=x[i]-x[i-1]
            #print(z)
            if(z>=y[i]):
                c+=1
        elif(x[i]<x[i-1]):
            z=x[i-1]-x[i]
            #print(z)
            if(z>=y[i]):
                c+=1
    print(c)
