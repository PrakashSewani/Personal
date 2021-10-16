n=153
number=n
flag=0
temp=[]

while(n!=0):
    temp.append(n%10)
    flag+=1
    n=n//10

sum=0
for i in temp:
    sum+=pow(i,flag)

if(sum==number):
    print("Armstrong")