
n = 5
def viral(n):

    liked = 0
    shared = 5
    totalLiked = 0

    for i in range(n):
        liked = shared // 2
        totalLiked += liked
        shared = liked * 3

    return totalLiked
print(viral(n))