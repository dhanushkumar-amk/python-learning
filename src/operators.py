from idlelib.pyparse import trans
from wsgiref.util import shift_path_info

#  assignment operator
#  assignment operator are used assign the value in the variables it represent in =

#  python is type_inferred language

age = 20
# int age = 20

# multiple assignment in a single line

name, Age = "dhanush", 20
print(name, age)

word = "hello"
print(word)
word = "world"  # we can also reassign the same variable with different values
print(word)


print('-----------------------')

# arithemetic operators
# + - * / %

a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print( a / b) # always print in floating point value
print(a // b) # floor division itis used to remove the floating point
print( a % b)

print(2 ** 3)  # it is used to identify the power of the numbers




# Bodmas rule
#(), **,  / , *, +, -

print(20-10/5*2)


# relational operators or comparison operator

a = 20
b = 5

# always give us the boolean as answer

print(a < b)
print(a > b)

c = 20
print( a >= c)

print( a == b)
print(a != b)


print("----------\t\t\t---------------------")
a = "Ram"
b = "ram"
print(a == b)  #  checking the both variable in an each characters
print( a < b)  # it will check based on the ascii value

# to identify the particular values ascii value using ascii value ord() function
print( "a =  " , ord('a'))
print("A =  " , ord('A'))


# argumented assignment operator (shorthand assignment operator)

a = 5
a += 2
print(a)

a *= 2   # a = a * 2
print(a)


# swap of two numbers

a = 5
b = 7

#  using temp variables
temp = a
a = b
b = temp
print(a, b)

a, b = b, a



#  membership operator  => it is used to check the value is present or not in a particular list or others

#  it will works only on sequence of the element

#  it is also return as boolean

# membership operator (in) | not in

list = [1,2,3,4,5]
print( 5 in list)

name = "visiovibe"
print('v' in name )
print('v' not in name)



print("----------------")

# logical operator

# it is also return boolean type

# and |  or  | not
a = 5
b = 20
statement1 = ( a==10)
statement2 = (b==20)

# or operator => either oant one will true it return true

print(statement1 or statement2)

#  and operator
#  if both the value is true ten it return true else return false

print(statement1 and statement2)


# not operator
# it convert true and false else fasle into true

# print(not(true))
# print(not(false))

print('---------------------------')

# bitwise operator

# bitwise and
# bitwise or
# bitwise not
# bitwise xor
# bitwise right shift
# bitwise left shift

a = 2
b = 3

# bitwise and
print(a & b)

# bitwise or
print(a | b)

#  bitwise xor => if the same number means false else return true
print(a ^ b)

print("=======================")
# right shift
print(a>>1)
print(a<<1)


# String replication

string = " hello world "
print( string * 10)  # string * number is called string replication

# string Concatenation
# it is used to add two strings

str1 = "hello"
str2 = "world"
print( str1 + str2)
