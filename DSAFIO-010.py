#             LOJA AQUI TUDO TEM DE 5% DESCONTO !!


print("-----------------------------------------------------")
valor = float(input("Qual é o valor do produto? "))
vdescontado = valor -  (valor * 5/100)
sodesconto = vdescontado - valor
print("-----------------------------------------------------")
print(f"VALOR SEM DESCONTO: R$ {valor}")
print(f"VALOR COM DESCONTO: R$ {vdescontado:.2f}")
print(f"DESCONTO DE: R$ {sodesconto}")
print("-----------------------------------------------------")