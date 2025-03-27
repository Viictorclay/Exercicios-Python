#                    PRIMEIRO E ULTIMO NOME


nome_completo = input("NOME COMPALTO: ").strip()
name = nome_completo.title().split()
if len(name) >= 2:
    print(f"PRIMEIRO NOME: {name[0]}")
    print(f"SEGUNDO NOME: {name[-1]}")