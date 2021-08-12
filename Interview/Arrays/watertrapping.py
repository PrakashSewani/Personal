arr=[3,0,0,2,0,4]
n=6

arrnew=arr

arr.sort()

h1=arr[n-1]
print(h1)
h2=arr[n-2]
print(h2)

water=h2*(n-2)

for i in range(1,n-2):
    water-=arrnew[i]

print(water)