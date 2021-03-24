x = 6 #global variable
y = "alex"

print(x)
print(y)

print(type(x))
print(type(y))

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = "awesome"

def myfunc():
  x = "fantastic" #local variable, can use global keyword to make it global
  print("Python is " + x)

myfunc()

print("Python is " + x)