
num = int(input("Enter the value of Num : "))

if(num < 2):
    print("It is not prime")

if(num % 2 != 0 and num % num != 0):
    print("It is a prime number")
else:
    print("It is a not prime ")