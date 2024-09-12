mark1 = int(input("Enter the mark1 : "))
mark2 = int(input("Enter the mark2 : "))
mark3 = int(input("Enter the mark3 : "))

if mark1 > 30 and mark2 > 30 and mark3 > 30:
    total = mark1 + mark2 + mark3
    avg = total // 3
    print(total)
    print(avg)
else:
    print("Your mark is not eligible to calculate")
