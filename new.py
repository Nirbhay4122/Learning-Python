#this is global variable

x='Nirbhay singh'

#this is local variable

def myfun():
  x='Nitesh patel'
  print(x)

myfun()
print("my name is " + x)