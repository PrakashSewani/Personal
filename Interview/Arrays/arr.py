arr=[1,1,2,4,2]
l=len(arr)
flag=0
for i in range(0,l-1):
    newarr=[]
    maximum=0
    for j in (0,l-1):
        newarr=arr[i:j]
        maximum=max(newarr)
        if(i*j<=maximum):
            flag+=1
            continue
        else:
            continue
    
print(flag)
