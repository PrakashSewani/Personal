def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))