#                        TEMPO DE ALISTAMENTO


nascimento = int(input("Qual foi o ano que você nasceu? "))
idade = 2025 - nascimento
tempo = 18 - idade
tempo2 = idade - 18
ano = nascimento + 18

if idade <18:
    print("Ainda não chegou no prediodo do seu alistamento.")
    print(f"Espere mais {tempo} anos.")
    print(f"Ano do seu alistamento: {ano}")
elif idade == 18:
    print("Você já esta no ano do seu alistamento! Aliste-se")
else:
    print("Já passou o seu periodo de alistamento.")
    print(f"Está {tempo2} atrasado. ")
    print(f"Ano do seu alistemanto foi em: {ano}")

print("")

print(f"{idade} \n {tempo2} \n {tempo} \n {ano} ")