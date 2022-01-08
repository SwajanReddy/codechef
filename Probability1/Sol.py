from itertools import permutations

n=int(input())

s=list(input().split())
s="".join(s)
k=int(input())

l=list(permutations(s,k))
tl=len(l)
p=0
for i in l:
    if "a" in i:
        p=p+1

print(p/tl)
