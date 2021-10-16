n=1258
arr=[]

for i in range(1,n):
    if(n%i==0):
        arr.append(i)
    else:
        continue

print(sum(arr))