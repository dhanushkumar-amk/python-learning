

n = 15
c = 3
m = 2

def chocalateFest(n,c,m):

    chocalate = n // c
    wrap = chocalate

    newChocalate = 0

    while wrap >= m:
        newChocalate = wrap // m
        chocalate += newChocalate
        wrap = (wrap % m) + newChocalate

    return chocalate

print(chocalateFest(n,c,m))