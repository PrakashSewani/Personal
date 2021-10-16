arr=[["Mohit",2,"14:23:33","17:23:33",5],["Omakr",2,"15:23:33","9:23:33",5],["AKDad",2,"16:23:33","10:23:33",5],["Adasd",2,"17:23:33","11:23:33",5],["adad",2,"18:23:33","12:23:33",5]]

name,jointime,leavetime=[],[],[]
for i in range(0,len(arr)):
    name.append(arr[i][0])
    jointime.append(arr[i][2])
    leavetime.append(arr[i][3])

print(jointime)

x=[]
temp=[]
for j in jointime:
    temp=j.split(":")
    for k in temp:
        if k.isdigit():
            x.append(int(k))

print(x)

print(leavetime)

y=[]
plc=[]
for l in leavetime:
    plc=l.split(":")
    for m in plc:
        if m.isdigit():
            y.append(int(m))

print(y)

attendance={}
timehr=None
timehr=None
p,q=0,0
for i in name:
    timehr=y[q]-x[q]
    timemin=y[q+1]-x[q+1]
    time=str(timehr)+":"+str(timemin)
    attendance[i]=time
    p+=1
    q+=3
print(attendance)