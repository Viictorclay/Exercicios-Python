#                    SISTEMA DE UMA BIBLIOTECA


import json
import os

biblioteca = []

def clear_sytem():
    os.system('cls' if os.name == 'nt' else 'clear')

def upload_biblioteca():
    global biblioteca
    if os.path.exists('biblioteca.json'):
        with open('biblioteca.json','r') as arquivo:
            biblioteca = json.load(arquivo)

def cadastrar_livro():
    print('     CADASTRAR LIVRO   ')
    cod = int(input( ' Código do Livro: '))
    title = input(' Nome do livro: ')
    autor = input(' Autor do livro: ')
    quant = int(input(' Quantos tem: '))
    preco = float(input(' Preço do livros'))

    livro = {
        "cod": cod,
        "title": title,
        "autor": autor,
        "quant": quant,
        "preco": preco
    }

    biblioteca.append(livro)
    print(' Livro cadastrado com sucesso!')




#programa pricipal

def menu():

    upload_biblioteca()
    while True:
        print('\n        MENU    ')
        print(' [1] Cadastrar livro')
        print(' [2] Buscar livro')
        print(' [3] listar livros')
        print(' [4] Editar livro')
        print(' [5] Remover livro')
        print(' [6] Salvar e sair\n')

        perg = input(' Digite: ')

        if perg in ['1']:
            print(cadastrar_livro())
        elif perg in ['2']:
            print(buscar_livro())
        elif perg in ['3']:
            print(listar_livros())
        elif perg in ['4']:
            print(editar_livro())
        elif perg in ['5']:
            print(remover_livro())
        elif perg in ['6']:
            print(salvar_e_sair())
            break
        else:
            print(' ERRO!  Opção invalida.')


#inicar progrma

menu()