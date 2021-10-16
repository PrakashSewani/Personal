arr=[[11,2,4],[4,5,6],[10,8,-12]]

suma=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if(i==j):
            suma+=arr[i][j]

kbz=[]
k=2
for i in range(0,3):
    kbz.append(arr[i][k])
    k-=1

ans=abs(suma-sum(kbz))
    
print(ans)