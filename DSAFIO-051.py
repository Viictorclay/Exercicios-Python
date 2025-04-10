#                     ADD VALORES UNICOS EM UMA LISTA


valores = []
while True:
    
    num = int(input(" Adicione um número: "))

    if num in valores:
        print(" Número já foi adicionado.")
    else:
        valores.append(num)
        print(" Número adicionado com sucesso!")

    opção = input(" Deseja continuar? (Sim/não): ").lower()

    if opção in ["não","n","nao","nn"]:
        print(f"{"=-=" * 30}")
        break

print(f" Nuemros adcionados {sorted(valores)}")
