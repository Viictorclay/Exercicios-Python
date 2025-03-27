#                     VELOCIMETRO + MULTA


velocidade = int(input("VELOCIDADE DO CARRO: "))

if velocidade > 60 :
    print("VOCÊ FOI MULTADO")
    multa = 7.00 * ( velocidade - 60)
    print("")
    print(f"MULTA DE: R${multa:.2f}")
else:
    print("Parabéns, por respeitar os limites da rodovia.")