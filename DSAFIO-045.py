#                  ESTATÍSTICAS EM PRODUTOS


total = 0
produtoM1000 = 0
menor_preço = None
nomeD_menor = ""

print("=-=-=-=-=--=--=--=-=---=-=-=-=-=-=-=-=-=-=-=-=")

while True:

    nomeD_produto = input("Produto: ")
    preço = float(input("Preço: "))
    
    total += + preço

    if preço > 1000:
        produtoM1000 += +1

    escolha = input("Tem mais algum produto ? (sim/não) ").strip().lower()

    if menor_preço is None or preço < menor_preço:
        menor_preço = preço
        nomeD_menor = nomeD_produto

    if escolha == "sim":
        print("----------------------------------------------")

    elif escolha in ["não", "nao", "n"]:
        print("=-=-=-=-=--=--=--=-=---=-=-=-=-=-=-=-=-=-=-=-=")
        print("                    RESUMO                  \n ")
        print(f"total: {total:.2f}")
        print(f"quantos produtos tem acima de 1000: {produtoM1000}")
        print(f"Produto mais barato: {nomeD_menor} R${menor_preço:.2f}")
        print("")
        print("                   FINISH                     ")
        print("=-=-=-=-=--=--=--=-=---=-=-=-=-=-=-=-=-=-=-=-=")
        exit()