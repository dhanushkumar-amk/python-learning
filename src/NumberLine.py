
kangaroo1 = 0
distance1 = 1

kangaroo2 = 2
distance2 = 2

def kangaroo(kangaroo1, distance1, kangaroo2, distance2):

    # Base case
    if distance1 < distance2 :
        return "No"

    newKangaroo1Position = kangaroo1
    newKangaroo2Position = kangaroo2

    while newKangaroo1Position < newKangaroo2Position :

        newKangaroo1Position += distance1
        newKangaroo2Position += distance2

        if newKangaroo1Position == newKangaroo2Position:
            return "yes"

    return "No"

print(kangaroo(kangaroo1,distance1,kangaroo2,distance2))