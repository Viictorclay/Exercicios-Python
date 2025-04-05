#                       SIMULADOR DE CAIXA ELETRONICO


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("                 BANCO Cy                  ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
valor = int(input(" Que valor você quer sacar ? R$ "))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

notas_50 = notas_20 = notas_10 = notas_1 = 0

notas_50 = valor // 50
valor %= 50

notas_20 = valor // 20
valor %= 20

notas_10 = valor // 10
valor %= 10

notas_1 = valor // 1
valor %= 1

if notas_50 >= 1:
    print(f" Total de {notas_50} cédulas de R$50")
if notas_20 >= 1:   
    print(f" Total de {notas_20} cédulas de R$20")
if notas_10 >= 1:
    print(f" Total de {notas_10} cédulas de R$10")
if notas_1 >= 1:
    print(f" Total de {notas_1} cédulas de R$1")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Volte sempre ao BANCO Cy! Tenha um bom dia.")
print("")