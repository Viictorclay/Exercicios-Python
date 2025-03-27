#                     ALUGUEL DE CARRO


dias = int(input("Quantos dias? "))
kms = float(input("Quantos kms rodou? "))
pagar = (dias * 60) + (kms * 0.15)
print(f"Falor final: {pagar:.2f}")