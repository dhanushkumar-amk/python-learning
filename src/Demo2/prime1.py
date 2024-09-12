num = int(input("enter the number :"))

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
            return  True

    else:
        return False


if isPrime(num):
    print(f"{num} is a prime number ")
else:
    print(f"{num} is a not prime number")

