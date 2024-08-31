
# function are mainly used to reusability of a same code





# function declaration or definition

def hello():                    # def is used to create the function
    for i in range(5):
        print("hello")

# function calling
hello()


# reusability
def add():
     a = int(input("a"))
     b = int(input("b"))
     c = a + b
     print(c)
add()


# types of function

# 1. void function
# 2 . non - void function

# does not return any value is called void function
# return any value is called non - void function

def sub():
    a = int(input("a"))  # example for non void function
    b = int(input("b"))
    return a - b

sub1 = sub()
print(sub1)

a = int(input("A"))
b = int(input("B"))

def add1(a,b):     # pass parameters
    return  a + b

sum1 = add1(a,b)  # pass arguments
print(sum1)


# parameterized function
# default function



# types of arguments

'''
keyword Arguments
default  Arguments
position Arguments
'''

# position arguments is used the order the same function declaration order

