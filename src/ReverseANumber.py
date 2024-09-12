num = 123

def reverse(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10  # Use integer division to update num
    return rev

reversed_num = reverse(num)
print(reversed_num)
