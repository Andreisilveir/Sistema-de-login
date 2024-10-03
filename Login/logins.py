from tkinter import messagebox
import tkinter as tk
import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'high'
)

class BrainBuster:
    
    def __init__(self):
        
        self.nome = ''
        self.email = ''
        self.senha = ''
        self.menu()
    
    def menu(self):
    
        self.janela = tk.Tk()
        self.janela.title('BrainBuster')
        self.janela.state('zoomed')

        t = tk.Label(self.janela, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)
    
        b_r = tk.Button(self.janela, text='Registro', height=2, width =15, border =3, borderwidth=3, command=self.registrar)
        b_r.place(rely=0.45, relx=0.35)
    
        b_l = tk.Button(self.janela, text='Login', height=2, width=15, border=3, borderwidth=3, command=self.login)
        b_l.place(rely=0.45, relx=0.45)
    
        b_i = tk.Button(self.janela, text='Informações', height=2, width=15, border=3, borderwidth=3, )
        b_i.place(rely =0.45, relx=0.55)
    
        b_s = tk.Button(self.janela, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (self.sair(self.janela)))
        b_s.place(rely=0.94, relx=0.9)

        self.janela.mainloop()
        
    def login(self):
    
        self.janela.destroy()
    
        self.janela3 = tk.Tk()
        self.janela3.title('Entrar')
        self.janela3.state('zoomed')
    
        e = tk.Label(self.janela3, text='Login', font=('Arial', 20))
        e.place(rely=0.15, relx=0.46)
    
        n_t = tk.Label(self.janela3, text='Nome', font=('Arial', 16))
        n_t.place(rely=0.3, relx=0.43)
    
        self.n_es = tk.Entry(self.janela3, font=20, border=3, borderwidth=3)
        self.n_es.place(rely=0.305, relx=0.47)
    
        s_t = tk.Label(self.janela3, text='senha', font=('Arial', 16))
        s_t.place(rely=0.35, relx=0.43)
    
        self.s_es = tk.Entry(self.janela3,font=20, border=3, borderwidth=3, show='*')
        self.s_es.place(rely=0.353, relx=0.47)
    
        tt = tk.Button(self.janela3, text='mostra', border=3, borderwidth=3, command=self.alternar_visibilidade)
        tt.place(rely=0.353, relx=0.6)
    
        b = tk.Button(self.janela3, text='login', height=1, width=8, border=3, borderwidth=3, command=self.entrar)
        b.place(rely=0.4, relx=0.5)
    
        b_r = tk.Button(self.janela3, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: (self.retornar(self.janela3)))
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(self.janela3, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (self.sair(self.janela3)))
        b_s.place(rely=0.94, relx=0.9)

        self.janela3.mainloop()
        
    def registrar(self):
    
        self.janela.destroy()
    
        self.janela2 = tk.Tk()
        self.janela2.title('Registro')
        self.janela2.state('zoomed')
    
        e = tk.Label(self.janela2, text='Registro', font=('Arial', 20))
        e.place(rely=0.15, relx=0.46)
    
        n_t = tk.Label(self.janela2, text='Nome', font=('Arial', 16))
        n_t.place(rely=0.3, relx=0.43)
    
        self.n_e = tk.Entry(self.janela2, font=20, border=3, borderwidth=3)
        self.n_e.place(rely=0.305, relx=0.47)
    
        e_t = tk.Label(self.janela2, text='Email', font=('Arial', 16))
        e_t.place(rely=0.35, relx=0.43)
    
        self.e_e = tk.Entry(self.janela2,font=20, border=3, borderwidth=3)
        self.e_e.place(rely=0.353, relx=0.47)
    
        s_t = tk.Label(self.janela2, text='Senha', font=('Arial', 16))
        s_t.place(rely=0.4, relx=0.425)
    
        self.s_e = tk.Entry(self.janela2, font=20 ,border=3, borderwidth=3, show='*')
        self.s_e.place(rely=0.405, relx=0.47)
    
        b_m = tk.Button(self.janela2, text='Mostrar', border=3, borderwidth=3, command=self.alternar)
        b_m.place(rely=0.4, relx=0.6)
    
        b = tk.Button(self.janela2, text='Registrar', height=1, width=8, border=3, borderwidth=3, command=self.registro)
        b.place(rely=0.45, relx=0.485)
    
        b_r = tk.Button(self.janela2, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: (self.retornar(self.janela2)))
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(self.janela2, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: (self.sair(self.janela2)))
        b_s.place(rely=0.94, relx=0.9)
    
        self.janela2.mainloop()
    
    def alternar_visibilidade(self):
    
        if self.s_es.cget('show') == '*':
            self.s_es.config(show='')  # Mostra a senha
            self.s_es.config(text='Esconder')  # Muda o texto do botão
        
        else:
            self.s_es.config(show='*')  # Esconde a senha
            botao.config(text='Mostrar')  # Muda o texto do botão
        
    def alternar(self):
    
        if self.s_e.cget('show') == '*':
           self.s_e.config(show='')
           self.s_e.config(text='Esconder')
        
        else:
            self.s_e.config(show='*')  # Esconde a senha
            botao.config(text='Mostrar')  # Muda o texto do botão

    def retornar(self,janela_atual):
    
        r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
        if r.lower() == 'yes':
            janela_atual.destroy()
            self.menu()

    def sair(self,janela_atual):
        r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
        if r.lower() == 'yes':
            janela_atual.destroy()
        
    def entrar(self):
    
        self.nomes = self.n_es.get()
        self.senha = self.s_es.get()
        
        try:
        
            with conexao.cursor() as cursor:
           
                sql = 'select * from registro WHERE nome = %s AND senha = %s'
                cursor.execute(sql, (self.nomes, self.senha))
                w = cursor.fetchone()
            
                if w == None:
                    messagebox.showinfo('Acesso Negado!', 'Acesso negado, verifique as informações inseridas ou se registre!')

                else:
                    messagebox.showinfo('Acesso aceito!', f'Seja bem-vindo(a) {self.nomes}')
                    self.janela3.destroy()
                    self.BrainBuster(titulo=tk.Tk())
                
        except pymysql.Error as error:
            conexao.rollback()
            messagebox.showerror('Erro', f'{error}')
        
    def registro(self):
    
        self.nome = self.n_e.get()
        self.email = self.e_e.get()
        self.senha = self.s_e.get()
    
        try:
            with conexao.cursor() as cursor:
                sql = "INSERT INTO registro(nome, email, senha) VALUES(%s, %s, %s)"
                cursor.execute(sql, (self.nome, self.email, self.senha))
                s = cursor.fetchall()
                conexao.commit()
                
                if s == None:
                    messagebox.showinfo('Usuario negado', 'Acesso negado, repita as informações!')
                    
                else:
                    r = messagebox.showinfo('Usuario aceito', 'Usuário registrado com sucesso, agora façã login!')
                
        except pymysql.Error as error:
            
            conexao.rollback()
            messagebox.showerror('Erro', f'{error}')
    
QuizBuster()