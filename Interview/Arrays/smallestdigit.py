def calculate(c):
    temp=[]
    ans=1
    varr=0
    while c!=0:
        d=c%10
        temp.append(d)
        c=c//10
    return temp

a=int(input())
for i in range(1,1000):
    temp=calculate(i)
    temp.reverse()
    idli=1
    for i in range(0,len(temp)):
        idli*=temp[i]*(10**i)
    if idli==a:
        print("TRUE")