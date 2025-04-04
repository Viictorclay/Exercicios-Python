#                     ANALISE DE DADOS DE UM GRUPO


from datetime import datetime

pessoasDmair = qHomens = mulherMs20 = qMulheres = qPessoas = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while True:

    name = input(" Qual é seu nome ? ")
    sexo = input(" Homen ou Mulher ? (H/M) ").strip().lower()
    ano = int(input(" Ano de nasciento: "))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    idade = datetime.now().year - ano

    if sexo == "h":
        qPessoas += +1
        qHomens += +1

        if idade > 18:
            pessoasDmair += +1

    elif sexo == "m":
        qPessoas += +1
        qMulheres += +1
        
    if idade > 18:
            pessoasDmair += +1

    elif idade < 20:
            mulherMs20 += +1

    escolha = input(" Deseja continuar ? ").lower()

    if escolha == "sim":
        print("-----------------------------------------------------")

    elif escolha == "não" or escolha == "nao":
        print("-----------------------------------------------------")
        print(f" Acima de 18 anos: {pessoasDmair} ")
        print(f" Homens cadastrados: {qHomens} ")
        print(f" Mulheres cadastradas: {qMulheres} ")
        print(f" Mulheres com idade menor que 20 anos: {mulherMs20} ")
        print(f" Pessoas cadastradas: {qPessoas} ")
        print(" FINISH.")
        exit()