with open(r'D:\Python\text.txt','rb') as f:
    lines=f.readlines()

txt=str(lines).split(",",1)[1]

dark=txt.split("\\n")

harsh=[]
for i in dark:
    temp=str(i).replace("\\","")
    harsh.append(temp)

while("" in harsh) :
    harsh.remove("")

harsh=harsh[:-1]

search=input()
k=search.split()
dhokla=""
for i in range(0, len(harsh)):
    if set(k).issubset(set(harsh[i].split())):
        print("success")
        print(i)
        for j in range(i,i+15):
            print("success")
            dhokla+=harsh[j+1]

print(dhokla)

# print('1.4.1 Gravitational Force'=='Gravitational Force')
# dd="1.4.1 Gravitational Force"
# ss=dd.split()
# print(ss)
# ds='Gravitational Force'
# sd=ds.split()
# print(sd)
# print(set(sd).issubset(set(ss)))