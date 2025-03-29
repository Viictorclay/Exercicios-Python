#               PEDRA, PAPEL E TISORA


import random

lista = ["Pedra", "Papel", "Tisora"]

while True:
    m_escolha = input("Pedra, Papel ou Tisora? ").strip().lower()
    escolha_do_pc = random.choice(lista)
    if escolha_do_pc.lower() == "pedra":
        if m_escolha.lower() == "pedra":
             print(f"ESCOLHA DA MAQUINA: {escolha_do_pc.capitalize()}")
             print("EMPATE!")  
        elif m_escolha.lower() == "papel":
            print(f"ESCOLHA DA MáQUINA: {escolha_do_pc.capitalize()}")
            print("Você Venceu!")
            comando = input("Deseja mais uma rodada? ")
            if comando.lower() in ["não", "nao"]:
                print("Certo, Até aproxima.")
                break
        elif m_escolha.lower() == "tisora":
             print(f"ESCOLHA DA MAQUINA: {escolha_do_pc.capitalize()}")
             print("Você Perdeu!")
             comando = input("Deseja mais uma rodada? ")
             if comando.lower() in ["não", "nao"]:
                print("Certo, Até aproxima.")
                break
                
    elif escolha_do_pc.lower() == "papel":
        if m_escolha.lower() == "pedra":
            print(f"ESCOLHA DA MÁQUINA: {escolha_do_pc.capitalize()}")
            print("Você Perdeu!")
            comando = input("Deseja mais uma rodada? ")
            if comando.lower() in ["não", "nao"]:
                print("Certo. Até aproxima.")
                break
            
        elif m_escolha.lower() == "papel":
            print(f"ESCOLHA DA MAQUINA: {escolha_do_pc.capitalize()}")
            print("EMPATE!")

        elif m_escolha.lower() == "tisora":
            print(f"ESCOLHA DA MÁQUINA: {escolha_do_pc.capitalize()}")
            print("Você Venceu!")
            comando = input("Deseja mais uma rodada? ")
            if comando.lower() in ["não", "nao"]:
                print("Certo. Até aproxima.")
                break
            
    elif escolha_do_pc.lower() == "tisora":
        if m_escolha.lower() == "pedra":
            print(f"ESCOLHA DA MÁQUINA: {escolha_do_pc.capitalize()}")
            print("Você Venceu!")
            comando = input("Deseja mais uma rodada? ")
            if comando.lower() in ["não", "nao"]:
                print("Certo. Até aproxima.")
                break
            
        elif m_escolha.lower() == "papel":
            print(f"ESCOLHA DA MAQUINA: {escolha_do_pc.capitalize()}")
            print("Você Perdeu!")
            comando = input("Deseja mais uma rodada? ")
            if comando.lower() in ["não", "nao"]:
                print("Certo. Até aproxima.")
                break 
            
        elif m_escolha.lower() == "tisora":
            print(f"ESCOLHA DA MÁQUINA: {escolha_do_pc.capitalize()}")
            print("EMPATE!")