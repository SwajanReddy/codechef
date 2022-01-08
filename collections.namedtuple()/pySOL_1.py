from collections import namedtuple
n=int(input())
s=input()
#print("s,",s)
stu=namedtuple("Student",s)
l=[]
for i in range(n):
     x=input()
     x=x.split()
     #print("X",x)
     x=stu(x[0],x[1],x[2],x[3])
     l.append(x)
tm=0   
c=0 
for i in l:
    #print(i)
    tm=tm+int(i.MARKS)
    c=c+1
avg=tm/c
print("%.2f"%avg)
