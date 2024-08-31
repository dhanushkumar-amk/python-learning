#  the variables are used to store the data it act as a container


# variables

  #  Datatypes
  # two types
  # simple and complex

  # 1 . simple
  #  integer - numbers
  # String  - words
  # boolean - True or False T and F are Caps
  # Float - Decimal numbers

  #  python does not support char data structure it is also considers as String

  # 2. Complex
  #   List
  #   Tuple
  #   Dictionary
  #   set



# name='dhanush'
# print(name)

name = "Dhanushkumar"
age  = 20
mark = 45.5
cat = False

print(name , age, mark, cat , sep=" | ")

# the variable name is also called Identifiers

# quiz
# name = "ram"
# crop = "rice"
# yield = 50   # yield has special meaning in python
# print(yield)


#  rules of naming the identifier
# 1. A keyword can't be used as an identifier

#  keywords in python
import  keyword
print(keyword.kwlist)


# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield'


# 2.All identifiers are case sensitive
Name = "dhanush"
name = "ram"
print(Name , name)

#  it also allows A-z , 1 - 9, and underscores  but it does not allowed white space and special characters
has_credit_card = False  # here the underscore is also called snake Case
print(has_credit_card)

# 3 first characters  always starts with letters
# 1name
_name = 'siva'
print(_name)

# in python the underscore is also consider as the letter

#  to see what the data type in variable using type function
word = "something"
print(type(word))
# <class 'str'>

has = True
print(type(has))


# Dynamic typing
name = "dhanush"  # string
name = 2004 # integer

print(type(name), name)  # it will print 2004

#  python allows us to change the value in dynamically


string = "Dhanush"
print(string[0])  # indexing                     it always starts with  0
# D

# mutability
#  to reassign the value in the variable

# string[0] = "s"
# print(string)
# we can't change the value in an item not in individual element


