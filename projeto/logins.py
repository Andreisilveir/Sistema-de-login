from tkinter import messagebox
import tkinter as tk
import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'high'
)

nome = ''
email = ''
senha = ''

def retornar(janela_atual):
    
    r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
    if r.lower() == 'yes':
        janela_atual.destroy()
        menu()

def sair(janela_atual):
    r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
    if r.lower() == 'yes':
        janela_atual.destroy()

def registro():
    global n_e, e_e, s_e, nome, email, senha
    
    nome = n_e.get()
    email = e_e.get()
    senha = s_e.get()
    
    try:
        with conexao.cursor() as cursor:
            sql = "INSERT INTO registro(nome, email, senha) VALUES(%s, %s, %s)"
            cursor.execute(sql, (nome, email, senha))
            s = cursor.fetchall()
            conexao.commit()
            if s == None:
                messagebox.showinfo('Usuario negado', 'Acesso negado, repita as informações!')
            else:
                messagebox.showinfo('Usuario aceito', 'Usuário registrado com sucesso, agora façã login!')
                
    except pymysql.Error as error:
        conexao.rollback()
        messagebox.showerror('Erro', f'{error}')
        
            
def pergunta():
    global janela3
    
    janela4 = tk.Tk()
    janela4.title('Pergunta e resposta')
    
    t = tk.Label(janela4, text='Perguntas', font=('Georgia', 20))
    t.place(rely=0.1, relx=0.38)
    
    t1 = tk.Label(janela4, text='E', font=('Georgia', 18))
    t1.place(rely=0.135, relx=0.45)
    
    t2 = tk.Label(janela4, text='Respostas', font=('georgia', 20))
    t2.place(rely=0.165, relx=0.465)
    
    b_c = tk.Button(janela4, text='Criar Perguntas', height=2, width =15, border =3, borderwidth=3,)
    b_c.place(rely=0.45, relx=0.35)
    
    b_r = tk.Button(janela4, text='Respostas', height=2, width=15, border=3, borderwidth=3,)
    b_r.place(rely=0.45, relx=0.45)
    
    b_p = tk.Button(janela4, text='Perguntas', height=2, width=15, border=3, borderwidth=3, )
    b_p.place(rely =0.45, relx=0.55)
    
    b_r = tk.Button(janela4, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: (retornar(janela2)))
    b_r.place(rely=0.94, relx=0.02)
    
    b_s = tk.Button(janela4, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (sair(janela)))
    b_s.place(rely=0.94, relx=0.9)
    
    janela4.mainloop()
        
def login():
    
    global janela3, janela
    
    janela.destroy()
    
    janela3 = tk.Tk()
    janela3.title('Entrar')
    
    e = tk.Label(janela3, text='Login', font=('Arial', 20))
    e.place(rely=0.15, relx=0.46)
    
    n_t = tk.Label(janela3, text='Nome', font=('Arial', 16))
    n_t.place(rely=0.3, relx=0.43)
    
    n_e = tk.Entry(janela3, font=20, border=3, borderwidth=3)
    n_e.place(rely=0.305, relx=0.47)
    
    s_t = tk.Label(janela3, text='senha', font=('Arial', 16))
    s_t.place(rely=0.35, relx=0.43)
    
    s_e = tk.Entry(janela3,font=20, border=3, borderwidth=3, show='*')
    s_e.place(rely=0.353, relx=0.47)
    
    b = tk.Button(janela3, text='login', height=1, width=8, border=3, borderwidth=3, )
    b.place(rely=0.4, relx=0.485)
    
    b_r = tk.Button(janela3, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: (retornar(janela3)))
    b_r.place(rely=0.94, relx=0.02)
    
    b_s = tk.Button(janela3, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (sair(janela3)))
    b_s.place(rely=0.94, relx=0.9)

    janela3.mainloop()

def registrar():
    global janela, n_e, e_e, s_e
    
    janela.destroy()
    
    janela2 = tk.Tk()
    janela2.title('Registro')
    
    e = tk.Label(janela2, text='Registro', font=('Arial', 20))
    e.place(rely=0.15, relx=0.46)
    
    n_t = tk.Label(janela2, text='Nome', font=('Arial', 16))
    n_t.place(rely=0.3, relx=0.43)
    
    n_e = tk.Entry(janela2, font=20, border=3, borderwidth=3)
    n_e.place(rely=0.305, relx=0.47)
    
    e_t = tk.Label(janela2, text='Email', font=('Arial', 16))
    e_t.place(rely=0.35, relx=0.43)
    
    e_e = tk.Entry(janela2,font=20, border=3, borderwidth=3)
    e_e.place(rely=0.353, relx=0.47)
    
    s_t = tk.Label(janela2, text='Senha', font=('Arial', 16))
    s_t.place(rely=0.4, relx=0.425)
    
    s_e = tk.Entry(janela2, font=20 ,border=3, borderwidth=3, show='*')
    s_e.place(rely=0.405, relx=0.47)
    
    b = tk.Button(janela2, text='Registrar', height=1, width=8, border=3, borderwidth=3, command=registro)
    b.place(rely=0.45, relx=0.485)
    
    b_r = tk.Button(janela2, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: (retornar(janela2)))
    b_r.place(rely=0.94, relx=0.02)
    
    b_s = tk.Button(janela2, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (sair(janela2)))
    b_s.place(rely=0.94, relx=0.9)
    
    janela2.mainloop()

def menu():
    global janela
    
    janela = tk.Tk()
    janela.title('menu')

    t = tk.Label(janela, text='Menu', font=('Arial', 20))
    t.place(rely=0.15, relx=0.46)
    
    b_r = tk.Button(janela, text='Registro', height=2, width =15, border =3, borderwidth=3, command=registrar)
    b_r.place(rely=0.45, relx=0.35)
    
    b_l = tk.Button(janela, text='Login', height=2, width=15, border=3, borderwidth=3, command=login)
    b_l.place(rely=0.45, relx=0.45)
    
    b_i = tk.Button(janela, text='Informações', height=2, width=15, border=3, borderwidth=3, )
    b_i.place(rely =0.45, relx=0.55)
    
    b_s = tk.Button(janela, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (sair(janela)))
    b_s.place(rely=0.94, relx=0.9)

    janela.mainloop()
    
menu()