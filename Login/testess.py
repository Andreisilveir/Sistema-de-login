import tkinter as tk

def opcao_selecionada(opcao):
    print(f"Você selecionou: {opcao}")

master = tk.Tk()
master.title("Menu Suspenso com OptionMenu")

# Variável para armazenar a seleção
variavel_opcao = tk.StringVar(master)
variavel_opcao.set("Escolha uma opção")  # Opção padrão

# Lista de opções
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5"]

# Criando o OptionMenu
menu = tk.OptionMenu(master, variavel_opcao, *opcoes, command=opcao_selecionada)
menu.pack(pady=10)

master.mainloop()