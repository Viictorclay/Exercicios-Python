#                    TUPLAS COM TIME DE FUTEBOL


teans = ("Corinthians", "Ceará", "Fortaleza", "Juventude", "Cruzeiro", "Grêmio", "Vasco da Gama", "Bragantino", "Flamengo", "Internacional", "Bahia", "São Paulo", "Sport", "Botafogo", "Palmeiras", "Atlético-MG", "Santos", "Mirassol", "Fluminense", "Vitória")

print("=============================================================")
print(f"Os 5 primerios colocados: \n{teans[0:6]}")
print("=============================================================")
print(f"Os últimos 4 colocados: \n {teans[16:]}")
print("=============================================================")
print(f"Times em orgem alfabetica: \n {sorted(teans)}")
print("=============================================================")
print(f"O São Paulo está na {teans.index("São Paulo") + 1}ª posição.")
