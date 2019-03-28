#print("Enter your name:")
#x = input()
#print("Hello, " + x)

#thislist = ["apple", "banana", "cherry"]
#thislist[1] = "blackcurrant"
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#for x in thislist:
#  print(x)

#thislist = ["apple", "banana", "cherry"]
#print("Type fruit name")
#x=input()
#if x in thislist:
#  print("Yes, 'apple' is in the fruits list")
#else:
#    print("no its not in the list")

#thislist = ["apple", "banana", "cherry"]
#thislist.insert(0, "orange")
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#del thislist
#print(thislist)

#i = 1
#while i < 10:
#  print(i)
#  i += 1
#
"""adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)"""

"""def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

def my_function():
  print("Hello from a function")
  my_function()"""

"""def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")"""

"""def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")"""

"""import datetime

x = datetime.datetime.now()
print(x)"""

"""import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))"""

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


