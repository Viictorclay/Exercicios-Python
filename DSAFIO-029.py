#                CLASIFICAÇÃO DE ATLETA DE NATAÇÃO


nome = input("NOME DO ATLETA: ")
ano = int(input("ANO DE NASCIMENTO: "))
categoria = 2025 - ano

if categoria <= 9:
    print("O ATLETA ESTÁ NA CATEGORIA: Mirim")
    print("CATEGORIA: 0 a 9 anos.")
elif categoria <= 14:
    print("O ATLETA ESTÁ NA CATEGORIA: Infantil")
    print("CATEGORIA: 10 a 14 anos.")
elif categoria <= 19:
    print("O ATLETA ESTÁ NA CATEGORIA: Junior")    
    print("CATEGORIA: 15 a 19 anos.")
elif categoria <= 22:
    print("O ATLETA ESTÁ NA CATEGORIA: Sênior")
    print("CATEGORIA: 20 a 22 anos.")
else:
    print("O ATLETA ESTÁ NA CATEGORIA: Master")
    print("CATEGORIA: Acima de 22 anos.")