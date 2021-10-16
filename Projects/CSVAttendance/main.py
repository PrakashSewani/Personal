import csv

filename='D:\Python\Projects\CSVAttendance\Original.csv'

rows=[]

with open(filename,'r') as csvfile:
    datareader=csv.reader(csvfile)
    for row in datareader:
        rows.append(row)

name=[]
joiningtime=[]
leavingtime=[]
for i in range(1,len(rows)):
    name.append(rows[i][0])
    joiningtime.append(rows[i][2])
    leavingtime.append(rows[i][3])

print(name)
#-----------------------joining time----------------------------------------------------------
x=[]
temp=[]
for j in joiningtime:
    temp.append(j.split(" "))

for k in range(0,len(temp)):
    x.append(temp[k][1])

finaljoin=[]
for l in range(0,len(x)):
    join=x[l].split(":")
    for pq in join:
        if pq.isdigit():
            finaljoin.append(int(pq))
#------------------------leaving time-----------------------------------------------------------
y=[]
perm=[]
for j in leavingtime:
    perm.append(j.split(" "))

for k in range(0,len(perm)):
    y.append(perm[k][1])

finalleave=[]
for l in range(0,len(y)):
    leave=y[l].split(":")
    for pq in leave:
        if pq.isdigit():
            finalleave.append(int(pq))
#--------------------------logic code-------------------------------------------------------------

difference=[]
timehr=None
timehr=None
timesec=None
p,q=0,0
for i in name:
    timehr=finalleave[q]-finaljoin[q]
    timemin=finalleave[q+1]-finaljoin[q+1]
    timesec=finalleave[q+2]-finaljoin[q+2]
    time=str(timehr)+":"+str(timemin)+":"+str(timesec)
    difference.append(time)
    q+=3

print(difference)