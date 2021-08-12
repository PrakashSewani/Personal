#Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

A=[]
N=int(input("Enter length of Array A "))

for i in range(0,N):
    temp=int(input("Enter the Element "))
    A.append(temp)

S=int(input("Enter the required Sum"))

sum=A[0]
subA=[]
start=0

for i in range(1,N):
    sum+=A[i]
    if(sum> S):
        sum=sum-A[start]
        start+=1

    if(sum<S):
        subA.append(A[i])
    
    if(sum==S):
        print(subA)
    
    else:
        print("No such Combination found")