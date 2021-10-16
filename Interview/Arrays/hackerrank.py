ar=[1,3,2,6,1,2]
k=3
flag=0
for i in ar:
    for j in ar:
        sum=i+j
        if(sum%k==0):
            flag+=1
        sum=0
        
print (flag)