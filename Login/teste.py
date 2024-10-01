import tkinter as tk
from random import *

class sla:
    
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('menu')
        self.janela.state('zoomed')
        
        self.panel = tk.Label(self.janela, text='BrainBuster', font=('Georgia', 23))
        self.panel.place(rely=0.3, relx=0.44)
        
        self.panel.pack_forget()
    
        b_r = tk.Entry(self.janela, width =15, font=('Georgia', 13))
        b_r.place(rely=0.45, relx=0.445)
        
        self.mo = tk.Button(self.janela, text='Enviar', border=3, borderwidth=3, width=6)
        self.mo.place(rely=0.45, relx=0.55)
        
        self.pe = tk.Button(self.janela, text='Pular pergunta', border=3, borderwidth=3)
        self.pe.place(rely=0.5, relx=0.465)
        
        variavel_opcao = tk.StringVar(self.janela)
        variavel_opcao.set("Tipos de Perguntas")  # Opção padrão 

        # Lista de opções
        opcoes = ["Progamação", "Historia", "Anime", "Mangá", "computação"]

        # Criando o OptionMenu
        menu = tk.OptionMenu(self.janela, variavel_opcao, *opcoes,)
        menu.place(rely=0.001, relx=0.03)
        
        b_r = tk.Button(self.janela, text='Retornar', height=2, width=17, border=3, borderwidth=3,)
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(self.janela, text='Sair', height=2, width=17, border=3, borderwidth=3,)
        b_s.place(rely=0.94, relx=0.9)
        
        self.janela.mainloop()
        
    def mostrar(self):
        self.panel.place(relx=0.3, rely=0.44)
        
sla()