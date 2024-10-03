import tkinter as tk
from tkinter import messagebox

class BrainBuster:
    def __init__(self): 
        self.janela_principal()

    def janela_principal(self):
        self.janela = tk.Tk()
        self.janela.title('menu')
        self.janela.state('zoomed')

        t = tk.Label(self.janela, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)

        b_r = tk.Button(self.janela, text='Quiz', height=2, width=15, border=3, borderwidth=3, command=self.quiz)
        b_r.place(rely=0.45, relx=0.35)

        b_l = tk.Button(self.janela, text='Perguntas', height=2, width=15, border=3, borderwidth=3)
        b_l.place(rely=0.45, relx=0.45)

        b_i = tk.Button(self.janela, text='Informações', height=2, width=15, border=3, borderwidth=3)
        b_i.place(rely=0.45, relx=0.55)

        b_r = tk.Button(self.janela, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: self.retornar(self.janela))
        b_r.place(rely=0.94, relx=0.02)

        b_s = tk.Button(self.janela, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: self.sair(self.janela))
        b_s.place(rely=0.94, relx=0.9)

        self.janela.mainloop()

    def quiz(self):
        self.janela.destroy()
        self.janela1 = tk.Tk()
        self.janela1.title('Quiz')
        self.janela1.state('zoomed')

        self.panel = tk.Label(self.janela1, text='BrainBuster', font=('Georgia', 23))
        self.panel.place(rely=0.3, relx=0.44)

        b_r = tk.Entry(self.janela1, width=15, font=('Georgia', 13))
        b_r.place(rely=0.45, relx=0.445)

        self.mo = tk.Button(self.janela1, text='Enviar', border=3, borderwidth=3, width=6)
        self.mo.place(rely=0.45, relx=0.55)

        self.pe = tk.Button(self.janela1, text='Pular pergunta', border=3, borderwidth=3)
        self.pe.place(rely=0.5, relx=0.465)

        variavel_opcao = tk.StringVar(self.janela1)
        variavel_opcao.set("Tipos de Perguntas")  # Opção padrão 

        # Lista de opções
        opcoes = ["Programação", "História", "Anime", "Mangá", "Computação"]

        # Criando o OptionMenu
        menu = tk.OptionMenu(self.janela1, variavel_opcao, *opcoes)
        menu.place(rely=0.001, relx=0.03)

        b_r = tk.Button(self.janela1, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: self.retornar(self.janela1))
        b_r.place(rely=0.94, relx=0.02)

        b_s = tk.Button(self.janela1, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: self.sair(self.janela1))
        b_s.place(rely=0.94, relx=0.9)

        self.janela1.mainloop()
        
    def Perguntas(self):
        print('')

    def mostrar(self):
        self.panel.place(relx=0.3, rely=0.44)

    def sair(self, janela_atual):
        r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
        if r.lower() == 'yes':
            janela_atual.destroy()

    def retornar(self, janela_atual):
        r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
        if r.lower() == 'yes':
            janela_atual.destroy()
            self.janela_principal()  # Chama o método para reiniciar a janela principal

BrainBuster()