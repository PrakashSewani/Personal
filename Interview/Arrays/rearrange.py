arr=[10,20,30,40,50,60,70,80,90,100,110]
arr.sort()

flaghigh=len(arr)
flagmin=0

arrnew=[]
for i in range(0,len(arr)):
    if(i%2==0):
        if(flaghigh!=flagmin):
            arrnew.append(arr[flaghigh-1])
            flaghigh-=1
            print("Flaghigh= ",flaghigh)
            continue
        else:
            break
    else:
        if(flagmin!=flaghigh):
            arrnew.append(arr[flagmin])
            flagmin+=1
            print("Flagmin",flagmin)
            continue
        else:
            break

print(arrnew)