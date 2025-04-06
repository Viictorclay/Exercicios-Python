#                    CONTADOR DE PALAVRAS UNICAS


frase = input(" Digite uma frase: ").strip().lower()

fraseMOD = frase.replace(".", "").replace(",", "")
liste = (fraseMOD).split()
palavras_unicas = set(liste)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f" Frase: {frase.capitalize()}")
print(f" Palavras únicas: {len(palavras_unicas)}")
print(f" Palavras: {', '.join(palavras_unicas)}")