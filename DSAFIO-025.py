#                   APROVA OU NÃO O FINANCIAMENTO ?


cores = {"vermelho": "\033[31m",
         "verde": "\033[32m",
         "branco": "\033[37m]",
         "reset": "\033[0m]"
         }

salario = float(input("Quanto você recebe por mês? "))
valor_casa = float(input("Qual é o valor da casa? "))
anos = int(input("Em quantos anos vocês deseja pagar? "))
mensal = (valor_casa / anos) / 12
tps = (salario * 30) / 100
print("")
if  mensal > tps:
    print(f"VALOR MENSAL: R${mensal:.2f}")
    print(f"SEU SALARIO: R${salario}"
          )
    print("Infelizmente o financiamento foi negado.\n O valor a pagar está 30%"" acima da sua renda mensal.")
elif mensal == tps:
    print(f"VALOR MENSAL: R${mensal:.2f}")
    print(f"SEU SALARIO: R${salario:.2f}"
          )
    print("Seu financiamento está liberado. Porém a um risco de acumulo de dividas, pois o valor a pagar está equivalente a sua renda mensal."
          )
    print("Aconselhamos não fazer o financiamento no momento e tentar novamento em outra oportunidade."
          )
else:
    print(f"VALOR MENSAL: R${mensal:.2f}")
    print(f"SALARIO: {salario:.2f}"
          )
    print("Opa! Boas noticias. Vocês está apto a financiar está casa!")