n=int(input())
l=[]

k=n
s=1
m=n-1
for i in range(n):
    x=[]
    for j in range(s,k+1):
        x.append(j)
    l.append(x)
    s=k+1
    k=k+m
    m=m-1
last=(s-1)*2
l2=s+1

c=0
dn=n
for i in range(len(l)):
    y=[]
    c=last-dn
    for j in range(c+1,last+1):
        y.append(j)
    l[i]=l[i]+y
    last=last-dn
    dn=dn-1

c=0
for i in l:
    i=[str(j) for j in i]
    i="*".join(i)
    space=" "*c
    i=space+i
    print(i)
    c=c+2
