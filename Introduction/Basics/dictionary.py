thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(len(thisdict))

x = thisdict["model"]
print(x)

thisdict.update({"year": 2020})
print(thisdict)

for x in thisdict:
  print(thisdict[x])