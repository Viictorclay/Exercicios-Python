#                      ÍMPARES MULTIPLOS DE 3 DE 0 A 500


for c in range(0, 500):
    if c % 2 == 0:
        c += 1
        if c % 3 == 0:
            print(c)