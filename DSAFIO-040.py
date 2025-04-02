#                              MASCULINO OU FEMINIO APENAS

sexo = 0
while sexo == "M" or "F":
    sexo = input("Digite seu Sexo (M/F): ").upper()
    if sexo == "M":
        print("Registrado. Seu sexo é Masculino.")
        break
    elif sexo == "F":
        print("Registrado. Seu sexo é Feminino.")
        break
    else:
        print("!ERRO! Digite ""M"" para Maculino ou ""F"" para Feminino. ")