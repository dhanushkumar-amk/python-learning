num = int(input("Enter the number: "))

sum = 0
temp = num

while temp > 0:
    remainder = temp % 10
    sum = sum + remainder ** 3
    temp = temp//10

if sum == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} not a armstrong number")