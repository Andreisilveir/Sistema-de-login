import tkinter as tk
import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'high'
)

cursor = conexao.cursor()

def menu():
    janela = tk.Tk()
    janela.title('menu')

    t = tk.Label(janela, text='Menu', font=('Arial', 20))
    t.place(rely=0.15, relx=0.46)
    
    b_r = tk.Button(janela, text='Registro', height=2, width =15, border =3, borderwidth=3, )
    b_r.place(rely=0.45, relx=0.35)
    
    b_l = tk.Button(janela, text='Login', height=2, width=15, border=3, borderwidth=3, )
    b_l.place(rely=0.45, relx=0.45)
    
    b_i = tk.Button(janela, text='Informações', height=2, width=15, border=3, borderwidth=3, )
    b_i.place(rely =0.45, relx=0.55)
    
    b_s = tk.Button(janela, text='Sair', height=2, width=17, border=3, borderwidth=3, )
    b_s.place(rely=0.94, relx=0.9)

    janela.mainloop()

    
menu()