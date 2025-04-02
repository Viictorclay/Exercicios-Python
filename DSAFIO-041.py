#               TENTNADO ADIVINHAR O NUMERO DO PC (DSAFIO-042 N 2)


import random
numero_PC = random.randint(0, 10)
meu_numero = 0
palpites = 1
while numero_PC != meu_numero:
    meu_numero = int(input("MEU NUMERO: "))
    print("-------------------------------------")
    if numero_PC == meu_numero:
        print(f"NUMERO ESCOLHIDO PELO PC: {numero_PC}")
        print(f"NUMERO QUE ESCOLHI: {meu_numero}")
        print("ACERTOU!")
        print(f"Você precisou de {palpites} palpite para adivinhar.")
        break
    elif numero_PC != meu_numero:
        palpites += + 1