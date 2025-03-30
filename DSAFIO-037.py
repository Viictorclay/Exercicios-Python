#                           NUMERO PRIMO ( sim or não )


n = int(input("DIGITE UM NUMERO: "))
for c in range(1, n +1):
    if n % c == 0:
        print("\033[32m", end=" ")
    else:
        print("\033[37m", end=" ")
    print(f"{c}", end=" ")