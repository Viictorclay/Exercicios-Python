#                               NUMEROS POR EXENTENSO


tuplas = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")

print("=-=-=-=-=-=-=----=-=--=-=-=-=-=-=-=-=-==-==-=-=-=-=-")
while True:
    
    try:
        
        numero = int(input(" Digite um numero de 0 a 10: "))

        print("-----------------------------------------------")
        if 0 <= numero <= 10: 
            print(f" Você digitou o numero: {tuplas[numero]}")
            print("=-=-=-=-=-=-=----=-=--=-=-=-=-=-=-=-=-==-==-=-=-=-=-")
            
        else:
            print(" !!ERRO!! ", end="")
            continue

    except ValueError:
        print("-----------------------------------------------")
        print(" !!ERRO!! ", end="")
        continue
    
    continuar = input(" Quer continuar ? (sim/não) ").strip().lower()

    if continuar in ["não","n","nao"]:
        print("Até aproxima..")
        break