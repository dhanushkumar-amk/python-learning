
# Iterative statement is nothing but loops

# it divided into two types

# 1.entry controlled loop
# 2.exit controlled loop => python does not have this

# 1. for loop

# entry controlled loop

num = 5

# syntax

for i in range(num):   # range - default starting zero and end with num - 1
    num *=  2
    # print(num)
print(num)

#  define a  range
num1 = 5
for i in range(3,5):
    num1 += 2
print(num1)


print("===============")

# step value is passed as third argument in range keyword
# range(start, end, increment)



for i in range(0,200,2):
    print(i)
