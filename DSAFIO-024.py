#                 CALCULAR PREÇO DA PASSAGEM POR KM


kms = int(input("Quantos kms vai ser sua viagem? "))

if kms <= 200:
    valor1 =  0.50 * kms
    print(f"O valor da sua passagem é: R${valor1:.2f}")
else:
    valor2 = 0.45 * kms
    print(f"O valor da sua passagem é: R${valor2:.2f}")