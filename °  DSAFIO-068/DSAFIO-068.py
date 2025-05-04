#                    SISTEMA DE UMA BIBLIOTECA


import json
import os

biblioteca = []

def clear_system():
    os.system('cls' if os.name == 'nt' else 'clear')

def upload_biblioteca():
    global biblioteca
    if os.path.exists('biblioteca.json'):
        with open('biblioteca.json','r') as arquivo:
            biblioteca = json.load(arquivo)

def cadastrar_livro():
    print('     CADASTRAR LIVRO   ')

    while True:
        cod = int(input( ' Código do Livro: '))
        if any(livro["cod"] == cod for livro in biblioteca):
            print(' Código já cadastrado. tente outro.')
            return
        else:
            break

    title = input(' Nome do livro: ')
    autor = input(' Autor do livro: ')
    quant = int(input(' Quantos tem: '))
    preco = float(input(' Preço do livros: '))

    livro = {
        "cod": cod,
        "title": title,
        "autor": autor,
        "quant": quant,
        "preco": preco
    }

    biblioteca.append(livro)
    print(' Livro cadastrado com sucesso!')


def buscar_livro():
    cod = int(input(' Digite o código do livro: '))
    for livro in biblioteca:
        if livro["cod"] == cod:
            print(f' Livro encotrado: {livro}')
            return
    print(' ❌ Produto não encontrado.')


def listar_livros():
    if not biblioteca:
        print(' !!Biblioteca Vazia.!!')
    else:
        print('    Lista de Livros disponiveis')
        for liv in biblioteca:
            print(f' Código: {liv["cod"]} | title: {liv["title"]} | Autor: {liv["autor"]} | Preço: {liv["preco"]:.2f}')


def editar_quant():
    cod = int(input(' Digite o código do livro: '))
    for livro in biblioteca:
        if livro["cod"] == cod:
            nova_qtd = int(input(' Atualize quantidade: '))
            livro["quant"] = nova_qtd
            print(" Quantidade atualizada!")
            return
    print(' ❌ Produto não encontrado.')


def remover_livro():
    cod = int(input(' Digite o código do livro: '))
    for livro in biblioteca:
        if livro["cod"] == cod:
            biblioteca.remove(livro)
            return
    print(' ❌ Produto não encontrado.')


def salvar_e_sair():
    with open('biblioteca.json','w') as arquivo:
        json.dump(biblioteca, arquivo, indent=5)
        print(' Biblioteca salva com sucesso! Até a próxima.\n')
    

#programa pricipal
def menu():

    upload_biblioteca()
    while True:
        print('\n        MENU    ')
        print(' [1] Cadastrar livro')
        print(' [2] Buscar livro')
        print(' [3] Listar livros')
        print(' [4] Editar quantidade')
        print(' [5] Remover livro')
        print(' [6] Salvar e sair\n')

        perg = input(' Digite: ')
        clear_system()

        if perg in ['1']:
            cadastrar_livro()
        elif perg in ['2']:
            buscar_livro()
        elif perg in ['3']:
            listar_livros()
        elif perg in ['4']:
            editar_quant()
        elif perg in ['5']:
            remover_livro()
        elif perg in ['6']:
            salvar_e_sair()
            break
        else:
            print(' ERRO!  Opção invalida.')


#iniciar progrma

menu()