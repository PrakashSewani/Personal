n=10
arr=[]
while(n>0):
    arr.append(n%2)
    n=n//2
# arr.reverse()
# print(arr)
flag=0
for i in arr:
    if i==1:
        flag+=1

for i in range(0,len(arr)):
    if arr[i]==1:
        msbindex=i

arr.reverse()
for i in range(0,len(arr)):
    if arr[i]==1:
        lsbindex=len(arr)-1-i

print(flag,"#",lsbindex,"#",msbindex)