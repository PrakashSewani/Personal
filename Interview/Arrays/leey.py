s='aabdfasd'
n=1000000000000
slen=len(s)
rem=n%slen
temp1=s[0:rem]
idli=n//slen
temp2=s*idli
temp2=temp1+temp2

flag=0
for i in temp2:
    if i=='a':
        flag+=1
    
print(flag)