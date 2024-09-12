


a = 5
b = 20
list = [5,6,7,8,9]

# membership operator

if a in list:
    print("A is present")
else:
    print("A is not present")

if b in list:
    print("B is present")
else:
    print("B is not present")


# Identity Operator in python

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)


