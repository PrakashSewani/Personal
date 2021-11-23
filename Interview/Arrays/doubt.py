def printtriangle(A):
    if len(A)<1:
        return
    temp=[0]*(len(A)-1)
    for i in range(0,len(A)-1):
        x=A[i]+A[i+1]
        temp[i]=x
    printtriangle(temp)
    # if((len(temp)+1)==1):
    #     print(A[0])
    print(A)
A=list(map(int,input().split()))
printtriangle(A)