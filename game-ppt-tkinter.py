import random
import tkinter as tk

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Função para jogar
def jogar():
    # Obter a escolha do jogador a partir da caixa de seleção
    jogador = escolha_jogador.get().lower()
    
    # Seleciona uma opção aleatória para o computador
    computador = random.choice(opcoes)
    
    # Verifica quem ganhou
    if jogador == computador:
        resultado.set("Empate!")
    elif jogador == "pedra":
        if computador == "papel":
            resultado.set("Você perdeu! O computador escolheu papel.")
        else:
            resultado.set("Você ganhou! O computador escolheu tesoura.")
    elif jogador == "papel":
        if computador == "tesoura":
            resultado.set("Você perdeu! O computador escolheu tesoura.")
        else:
            resultado.set("Você ganhou! O computador escolheu pedra.")
    elif jogador == "tesoura":
        if computador == "pedra":
            resultado.set("Você perdeu! O computador escolheu pedra.")
        else:
            resultado.set("Você ganhou! O computador escolheu papel.")
    
    # Atualiza o label com o resultado
    label_resultado.config(text=resultado.get())

# Cria a janela principal
janela = tk.Tk()
janela.title("Pedra, Papel, Tesoura")

# Cria um frame para as opções de escolha
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack()

# Cria uma caixa de seleção para as opções de escolha
escolha_jogador = tk.StringVar(value=opcoes[0])
opcoes_menu = tk.OptionMenu(frame_opcoes, escolha_jogador, *opcoes)
opcoes_menu.pack(side=tk.LEFT)

# Cria um botão para jogar
botao_jogar = tk.Button(frame_opcoes, text="Jogar", command=jogar)
botao_jogar.pack(side=tk.LEFT)

# Cria um label para exibir o resultado
resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado, font=("Arial", 16))
label_resultado.pack()

# Inicia o loop da janela
janela.mainloop()
