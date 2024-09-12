
name = input("Enter the name :")

m1 = int(input("Enter the mark1 : "))
m2 = int(input("Enter the mark2 : "))
m3 = int(input("Enter the mark3 : "))

total = m1 + m2 + m3
average = total // 3

if m1 < 35 or m2 < 35 or m3 < 35:
    result = "fail"
else:
    result = "pass"


print("Name : ", name)
print("marks : ", m1, m2, m3)
print("total :", total, "out of 300")
print("average :", average)
print("result :", total)

