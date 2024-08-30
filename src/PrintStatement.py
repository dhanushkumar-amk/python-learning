# print statement
print("hello world")
print('hello world') # we can use both double and single quotes

# it has two arguments

# 1. end  - it defines what we can do after print statement at the end default => go to the new line end='\n';
print("python is a shit", end='')
print(" python is holy shit****")
#   if we don't any new line just use end=" " with empty arguments

# quiz 1
print("2 + 3", end=' = ')
print(2 + 3)
#  we can also add String with in the end=" " arguments

# 2. separation arguments
#  separation  arguments is used to separate the many sentence in an arguments
#  it wll works as replace of comma(,)

# default separation is space

print("laptop" ," powerBank", " mouse" ," pen" ," pencil", " eraser", " mobile phone")

# separation using print statement
print("laptop", " powerBank", " mouse", " pen" ," pencil", " eraser", " mobile phone" ,sep=' + ')


#  it will work on the mathematical expression
print(40 + 60)
print(76 * 4 + 5 -2)

# quiz 2
print("Hi", "Hi",  sep='...', end="...")
print("Hi")


