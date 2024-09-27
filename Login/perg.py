import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class BrainBuster:
    def __init__(self):
        janela = tk.Tk()
        janela.title('menu')
        janela.state('zoomed')
        
        t = tk.Label(janela, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)
    
        b_r = tk.Button(janela, text='Quiz', height=2, width =15, border =3, borderwidth=3,)
        b_r.place(rely=0.45, relx=0.35)
    
        b_l = tk.Button(janela, text='Perguntas', height=2, width=15, border=3, borderwidth=3,)
        b_l.place(rely=0.45, relx=0.45)
    
        b_i = tk.Button(janela, text='Lista', height=2, width=15, border=3, borderwidth=3, )
        b_i.place(rely =0.45, relx=0.55)
        
        b_r = tk.Button(janela, text='Retornar', height=2, width=17, border=3, borderwidth=3, command= lambda:(retornar(janela)))
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(janela, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (sair(janela)))
        b_s.place(rely=0.94, relx=0.9)
        
        def sair(janela_atual):
            r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
            if r.lower() == 'yes':
                janela_atual.destroy()
                
        def retornar(janela_atual):
    
            r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
            if r.lower() == 'yes':
                janela_atual.destroy()
                BrainBuster()
        
        def Quiz():
            print()


        janela.mainloop()
        
BrainBuster()