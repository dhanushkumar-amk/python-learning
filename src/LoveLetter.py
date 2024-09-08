
s = 'abcd'

def letter(s):
    count = 0
    i = 0
    j = len(s)-1

    while i > j:
        char1 = s.index(i)
        char2 =  s.index(j)

        if char1 > char2:
            temp = char1 - char2
        else:
            temp = char2 - char1

        count = count + temp

        i = i + 1
        j = j - 1
    return count
print(letter(s))



