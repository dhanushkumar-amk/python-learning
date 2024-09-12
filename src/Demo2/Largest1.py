

a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
c = int(input("Enter the value c: "))

if a > b and b > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

print(f"Largest of three number {a}, {b} and {c} is =  ", largest)