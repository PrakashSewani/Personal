# a=input()
# b=a.split(" ")
# arr=[]
# for i in range(0,len(b)-1):
#     c=b[i]
#     d=b[i+1]
#     temp1=c[len(c)-1]
#     temp2=d[0]
#     if temp1==temp2:
#         arr.append(1)
#     else:
#         arr.append(0)
# if 0 in arr:
#     print("False")
# else:
#     print("True")

def SmoothFunction(a):
    b=a.split()
    print(b)
    arr=[]
    print(len(b))
    if len(b)<=1:
        return False
    for i in range(0,len(b)-1):
        c=b[i]
        d=b[i+1]
        temp1=c[len(c)-1]
        temp2=d[0]
        if temp1==temp2:
            arr.append(1)
        else:
            arr.append(0)
    if 0 in arr:
        return False
    elif 1 in arr:
        return True

a=input()
print(SmoothFunction(a))
    
