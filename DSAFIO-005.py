#                 CALCULAR A MEDIA DE UM ALUNO


print("-----------------------------------------------------")
print("                   NOTA DE CLAY                      ")
print("-----------------------------------------------------")
pn = float(input(" Primeira nota: "))
sn = float(input(" Segunda nota: "))
md = (pn + sn) / 2
print("-----------------------------------------------------")
print(f" MEDIA: {md}")
if md >= 6:
    print(" ALUNO APROVADO! ")
else:
    print(" ALUNO EM RECUPERÇÃO! ")