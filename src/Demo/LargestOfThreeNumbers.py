a = int(input(" Enter the a value : "))
b = int(input(" Enter the b value : "))
c= int(input(" Enter the c value : "))


if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else:
    largest = c

print("The largest value is : ", largest)