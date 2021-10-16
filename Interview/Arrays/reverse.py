n=int(input("Number: "))

reverse=""
while(n!=0):
    temp=(n%10)
    reverse+=str(temp)
    n=n//10

print(int(reverse))


