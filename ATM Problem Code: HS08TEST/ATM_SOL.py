# cook your dish here
amt,bal=map(eval,input().split())

if amt%5==0 and amt+0.50<=bal:
    bal=bal-amt-0.50
    print("%.2f"%(bal))
else:
    print("%.2f"%(bal))
