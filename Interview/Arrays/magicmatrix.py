s=[[4,9,2],[3,5,7],[8,1,5]]
effort=[]
vert=0
lst=[]
temp1,temp2,temp3,temp4=0,0,0,0
seconddiagonal=len(s)-1
for i in range(0,len(s)):
    
    for j in range(0,len(s)):
        temp1+=s[i][j]
    lst.append(temp1)
    # print(temp1)
    temp1=0    
        
    while(vert!=len(s)):
        temp2+=s[vert][i]
        vert+=1
    lst.append(temp2)
    # print(temp2)
    vert=0
    temp2=0

for i in range(0,len(s)):    
    for j in range(0,len(s)):
        if i==j:
            temp3+=s[i][j]
# print(temp3)
lst.append(temp3)       
    
for i in range(0,len(s)):    
    while(seconddiagonal>=0):
        temp4+=s[i][seconddiagonal]
        seconddiagonal-=1
lst.append(temp4)
print(temp4)
# for i in lst:
#     if i<15:
#         effort.append(15-i)