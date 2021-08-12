a=[7, 3, 2, 4, 9, 12, 56]
a.sort()

n=3
minimum=0
for i in a:
    while(n<len(a)):
        print('mayur ',n)
        if(minimum==0):
            minimum=abs(a[i]-a[n])
            n+=1
            break
        elif(abs(a[i]-a[n])<minimum):
            minimum=abs(a[i]-a[n])
            print (minimum)
            n+=1
            break
