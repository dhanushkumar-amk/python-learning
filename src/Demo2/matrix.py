
a = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

b = [
    [1, 2, 3],
    [1, 2, 3],
    [1,2, 3]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(a)):
            result[i][j] += a[i][k] * b[k][j]


for row in result:
    print(row)
