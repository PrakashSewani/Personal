arr=[900, 940, 950, 1100, 1500, 1800]
dep=[910, 1200, 1120, 1130, 1900, 2000]

lenarr=len(arr)
lendep=len(dep)

platform=1
for i in range(0,lenarr-2):
    if i!=lenarr-2:#penultimate
        if(arr[i+1]>dep[i]):
            continue
        else:
            print(platform)
            platform+=1
    

for j in range(0,lendep-1):
    if(arr[lenarr-1]>dep[j]):
        break
                
print(platform)