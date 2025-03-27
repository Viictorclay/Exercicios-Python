#                        QUEM GANHA EU OU O PC ?


import random
numero_PC = random.randint(0, 5)

meu_numero = int(input("MEU NUMERO: "))
print("")

if numero_PC == meu_numero:
    print(f"NUMERO ESCOLHIDO PELO PC: {numero_PC}")
    print(f"NUMERO QUE ESCOLHI: {meu_numero}")
    print("EMPATE")
elif numero_PC >= meu_numero:
    print(f"NUMERO ESCOLHIDO PELO PC: {numero_PC}")
    print(f"NUMERO QUE ESCOLHI: {meu_numero}")
    print("EU PERDIR T-T.")
else:
    print(f"NUMERO ESCOLHIDO PELO PC: {numero_PC}")
    print(f"NUMERO QUE ESCOLHI: {meu_numero}")
    print("EU GANHEI! CHORA MAQUINA!")