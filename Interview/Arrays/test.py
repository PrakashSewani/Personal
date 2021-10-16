import math

n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

itr=[]
ans=[]
for i in arr:
    itr.append(i)
    itr.sort()
    if len(itr)%2!=0:
        mid=math.floor(len(itr)/2)
        ans.append(float(itr[mid]))
       
    else:
        mid1=int(len(itr)/2)
        median=((itr[mid1-1]+itr[mid1])/2)
        ans.append(median)
        
print(ans)