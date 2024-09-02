

x = 2
y = 2
z = 6

def cats(x,y,z):
    distance1 = 0
    distance2 = 0

    distance1 = abs(x - z)
    distance2 = abs(y - z)

    if(distance1 == distance2):
        return "Mouse C"
    elif(distance1 < distance2):
        return "Cat A"
    else:
        return "Cat B"
print(cats(x,y,z))