import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class BrainBuster:
    def __init__(self): 
        
        self.janela = tk.Tk()
        self.janela.title('menu')
        self.janela.state('zoomed')
        
        t = tk.Label(self.janela, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)
    
        b_r = tk.Button(self.janela, text='Quiz', height=2, width =15, border =3, borderwidth=3,)
        b_r.place(rely=0.45, relx=0.35)
    
        b_l = tk.Button(self.janela, text='Perguntas', height=2, width=15, border=3, borderwidth=3,)
        b_l.place(rely=0.45, relx=0.45)
    
        b_i = tk.Button(self.janela, text='Lista', height=2, width=15, border=3, borderwidth=3, )
        b_i.place(rely =0.45, relx=0.55)
        
        b_r = tk.Button(self.janela, text='Retornar', height=2, width=17, border=3, borderwidth=3, command= self.retornar)
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(self.janela, text='Sair', height=2, width=17, border=3, borderwidth=3, command=self.sair)
        b_s.place(rely=0.94, relx=0.9)
        
        self.janela.mainloop()

        
    def sair(self, janela_atual):
        r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
        if r.lower() == 'yes':
            janela_atual.destroy()
                
    def retornar(self, janela_atual):
    
        r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
        if r.lower() == 'yes':
            janela_atual.destroy()
            BrainBuster()
        
BrainBuster()