num = int(input("Enter the number : "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i
print(f"the factorial number of {num} is", fact)