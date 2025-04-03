#                             ÍMPA / PAR  -  GAMER


from random import randint

win = impa = par = soma = 0

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while True:
    
    numero_PC = randint(0,10)

    lado = input(" ÍMPA OU PAR ? ").lower()
    meu_nuemero = int(input(" Qual vai ser seu número? "))
    print(f" Número do PC: {numero_PC}")

    soma = meu_nuemero + numero_PC
    
    if lado == "impa" or lado == "ímpa":
        if soma % 3 == 0:
            win += +1
            print("----------------------------------------------------")
            print(f" Resultado: {soma}")
            print(f" Numero do PC: {soma}")
            print(" Win! Mais uma!")

        else:
            print("----------------------------------------------------")
            print(f" Resultado: {soma}")
            print(" Lose.")
            print(f" Você teve {win} Wins consecutivas.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            break
    
    elif lado == "par":
        if soma % 2 == 0:
            win += +1
            print("----------------------------------------------------")
            print(f" Resultado: {soma}")
            print(" Win! Mais uma!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        else:
            print("----------------------------------------------------")
            print(f" Resultado: {soma}")
            print(" Lose.")
            print(f" Você teve {win} Wins consecutivas.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            break