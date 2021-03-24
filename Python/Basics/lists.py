thislist = ["apple", "banana", "cherry"]

print(thislist)

print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

print(list1)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #if not specified pop() removes the last entry

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)