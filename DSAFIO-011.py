#                      REAJUSTE SALARIAL


salario = float(input("Quanto o fucionariol ganha? "))
salarioCR = salario + (salario * 8.40/100)
reajuste = salarioCR -  salario
print(f"O salario do funcionario ficou R${salarioCR}")
print(f"O reajuste foi de R${reajuste}")