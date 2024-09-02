n = 5
height = 1

def treeHeight(n, height):
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height +=1
    return  height
print(treeHeight(n, height))
