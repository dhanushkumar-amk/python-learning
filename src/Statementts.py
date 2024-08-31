
#  the statement is a set of instructions

# types of statement

# 1. simple statements
# 2. compund statement
# 3. Empty statement


# component statement
#  conditional statements
'''
a = 10
b = 100
if (a < b and b == 100):  # the brackets are optional in python
    print(True)
else:
    print(False)


# elif

a = 1000
b = 200
c = 30

if(a > b and a > c):
    print("A is greatest")
elif (b > c):
    print("B is greatest")
else:
    print("c is greatest")

num1 = int(input("Enter the number : "))

if num1 == 0:
    print("It is a zero" , num1)
elif num1 > 0:
    print("It is a positive number", num1)
else :
    print("It is a negative number", num1)



# nested if statement

age = 18
eat_pizza = True
exercise = True

if age > 15:
    if eat_pizza == True and exercise == True :
        print("Your are fit")
    else :
        print("your are nt fit ")
else:
    print("It is your wish")
'''

# ternary operator