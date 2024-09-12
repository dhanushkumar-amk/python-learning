num = int(input("Enter the value : "))
sum = 0
temp = num

while temp > 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10

if sum == num:
    print("It is an armstrong number")
else:
    print(" It is a not an armstrong number")