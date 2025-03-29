#               NOTA DE UM ALUNO (APROVADO OU REPROVADO)


n1 = float(input("PRIMEIRA NOTA: "))
n2 = float(input("SEGUNDA NOTA: "))
n3 = float(input("TERCEIRA NOTA: "))
media = (n1 + n2 + n3) / 3

print("")
if media < 5.0:
    print(f"MEDIA: {media:.1f}")
    print("ALUNO REPOVADO.")
elif 5.0 <= media <= 6.9:
    print(f"MEDIA: {media:.1f}")
    print("ALUNO EM RECUPERAÇÃO.")
else:
    print(f"MEDIA: {media:.1f}")
    print("ALUNO APROVADO.")