string="prakash"

temp=""
for i in string:
    if i not in temp:
        temp+=i
    
print(temp)