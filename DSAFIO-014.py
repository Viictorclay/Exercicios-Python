#                         CALCULADORA


import math

num = float(input("Digite um numero: "))
arredondarCIMA = math.ceil(num)
arredondarBAIXO = math.floor(num)
partINTERIA = math.trunc(num)
potencia = math.pow(num)
raizQ = math.sqrt(num)

print(f"ARREDONDANDO PARA CIMA: {arredondarCIMA}")
print(f"ARREDONDANDO PARA BAIXO: {arredondarBAIXO}")
print(f"PARTE INTEIRA: {partINTERIA}")
print(f"POTENCIA: {potencia}")
print(f"RAIZ QUADRADA: {raizQ:.2f}")
