#                               IMC


peso = float(input("DIGITE SEU PESO: "))
altura = float(input("DIGITE SUA ALTURA: "))
imc = peso / (altura ** 2)
obesidade = (0 if imc <18.5 else
             1 if imc < 29.9 else
             2 if imc < 39.9 else
             3)

if imc <18.5:
    print(f"IMC: {imc:.2f}")
    print("Você está abaixo do peso ideal.")
    print("CLASSIFICAÇÃO: Magreza")
    print(f"OBESIDADE(grau): {obesidade}")
elif 18.5 <= imc <= 24.9:
    print(f"IMC: {imc:.2f}")
    print("Voce está no peso ideal.")
    print("CLASSIFICAÇÃO: Normal")
    print(f"OBESIDADE(grau): {obesidade}")
elif 25.0 <= imc <29.9:
    print(f"IMC: {imc:.2f}")
    print("Você está acima do peso.")
    print("CLASSIFICAÇÃO: Sobrepeso")
    print(f"OBESIDADE(grau): {obesidade}")
elif 30.0 <= imc <39.9:
    print(f"IMC: {imc}")
    print("Você está obeso.")
    print("CLASSIFICAÇÃO: Obesidade")
    print(f"OBESIDADE(grau): {obesidade}")
else:
    print(f"IMC: {imc}")
    print("Você está obeso.")
    print("CLASSIFICAÇÃO: Obesidade Grave")
    print(f"OBESIDADE(grau):")