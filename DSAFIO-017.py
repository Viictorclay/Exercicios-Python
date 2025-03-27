#                     LER NUMERO DE 0 A 9999

while True:
    numero = input("DIGITE UM NUMERO DE 0 A 9999: ").strip()
    print("")

    if len(numero) == 4:
        print(f"unidade: {numero[3]}")
        print(f"dezena: {numero[2]}")
        print(f"centena: {numero[1]}")
        print(f"milhar: {numero[0]}")
        break
    elif len(numero) == 3:
        print(f"unidade: {numero[2]}")
        print(f"dezena: {numero[1]}")
        print(f"centena: {numero[0]}")
        break
    elif len(numero) == 2:
        print(f"unidade: {numero[1]}")
        print(f"dezena: {numero[0]}")
        break
    elif len(numero) == 1:
        print(f"unidade: {numero[0]}")
        break
    else:
        print("N/0")