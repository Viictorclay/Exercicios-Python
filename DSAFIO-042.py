#                        CALCULADORA COM MENU

while True:

    while True:

        try:
            n1 = int(input("Primeiro Número: "))
            break
        except ValueError:
            print("!ERRO!")
            continue

    while True:
        try:
            n2 = int(input("Segundo Número:  "))
            break
        except ValueError:
            print("!ERRO!")
            continue


    print("")
    menu = int(input(" [1] Somar\n [2] multiplicar\n [3] Maior número\n [4] Novos números\n [0] Sair do programa\n \nDigte: "))

    if menu == 1:
        s = n1 + n2
        print(f"{n1} + {n2}")
        print(f"Resultado: {s}")
        
    elif menu == 2:
        m = n1 * n2
        print(f"Resultado: {m}")
        print(f"{n1} * {n2}")
        
    elif menu == 3:
        mn = max(n1, n2)
        if n1 == n2:
            print(f"{n1} e {n2}")
            print(f"Resultado: Não existe numero maior.")
        elif n1 != n2:
            print(f"{n1} e {n2}")
            print(f"Resultado: {mn}")
        
    elif menu == 4:
        print("OK. Digite os novos números.")

    elif menu == 0:
        print("Fechando programa... até proxima.")
        exit()

    else:
        print("!ERRO!")
