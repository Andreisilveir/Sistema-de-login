from tkinter import messagebox
import tkinter as tk
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('db_host')
db_user = os.getenv('db_user')
db_password = os.getenv('db_password')
db_name = os.getenv('db_name')


conexao = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
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
        n_t.place(rely=0.3, relx=0.4)
    
        self.n_es = tk.Entry(self.janela3, font=20, border=3, borderwidth=3)
        self.n_es.place(rely=0.305, relx=0.44)
    
        s_t = tk.Label(self.janela3, text='senha', font=('Arial', 16))
        s_t.place(rely=0.35, relx=0.395)
    
        self.s_es = tk.Entry(self.janela3,font=20, border=3, borderwidth=3, show='*')
        self.s_es.place(rely=0.353, relx=0.44)
    
        tt = tk.Button(self.janela3, text='mostra', border=3, borderwidth=3, command=self.alternar_visibilidade)
        tt.place(rely=0.353, relx=0.59)
    
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
        n_t.place(rely=0.3, relx=0.4)
    
        self.n_e = tk.Entry(self.janela2, font=20, border=3, borderwidth=3)
        self.n_e.place(rely=0.305, relx=0.44)
    
        e_t = tk.Label(self.janela2, text='Email', font=('Arial', 16))
        e_t.place(rely=0.35, relx=0.4)
    
        self.e_e = tk.Entry(self.janela2,font=20, border=3, borderwidth=3)
        self.e_e.place(rely=0.353, relx=0.44)
    
        s_t = tk.Label(self.janela2, text='Senha', font=('Arial', 16))
        s_t.place(rely=0.4, relx=0.395)
    
        self.s_e = tk.Entry(self.janela2, font=20 ,border=3, borderwidth=3, show='*')
        self.s_e.place(rely=0.405, relx=0.44)
    
        b_m = tk.Button(self.janela2, text='Mostrar', border=3, borderwidth=3, command=self.alternar)
        b_m.place(rely=0.405, relx=0.59)
    
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
                    QuizBuster()
                
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
            
class QuizBuster:
    
    def __init__(self): 
        self.qa_list = []
        self.janela_principal()

    def janela_principal(self):
        self.janela = tk.Tk()
        self.janela.title('Menu')
        self.janela.state('zoomed')

        t = tk.Label(self.janela, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)

        b_r = tk.Button(self.janela, text='Quiz', height=2, width=15, border=3, borderwidth=3, command=self.quiz)
        b_r.place(rely=0.45, relx=0.35)

        b_l = tk.Button(self.janela, text='Perguntas', height=2, width=15, border=3, borderwidth=3, command=self.lista)
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

        self.selecionar_pergunta()  # Obtém uma nova pergunta

        if self.f: 
            self.p_t = tk.Label(self.janela1, text=self.f, font=('georgia', 20))
            self.p_t.place(relx=0.5, rely=0.2, anchor='center')
        else:
            messagebox.showinfo('Sem perguntas', 'Não tem pergunta registrada!')
            self.janela1.destroy()
            return

        self.r_e = tk.Entry(self.janela1, font=2, border=3, borderwidth=3, width=15)
        self.r_e.place(relx=0.5, rely=0.45, anchor='center')

        b_e = tk.Button(self.janela1, text='Enviar', border=3, borderwidth=3, width=5, command=self.revisar_resposta)
        b_e.place(relx=0.58, rely=0.45, anchor='center')

        b_p = tk.Button(self.janela1, text='Pular pergunta', border=3, borderwidth=3, width=10, command=self.atualizar_pergunta)
        b_p.place(relx=0.5, rely=0.5, anchor='center')

        b_r = tk.Button(self.janela1, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: self.retornar(self.janela1))
        b_r.place(rely=0.94, relx=0.02)

        b_s = tk.Button(self.janela1, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: self.sair(self.janela1))
        b_s.place(rely=0.94, relx=0.9)

        self.janela1.mainloop()

    def atualizar_pergunta(self):
        
        messagebox.showinfo('Pulando pergunta', "Atualizando pergunta...")  # Mensagem de depuração
        self.selecionar_pergunta()  # Seleciona uma nova pergunta

        if self.f:
            
            self.p_t.config(text=self.f)  # Atualiza o texto do label
        else:
            messagebox.showinfo('Sem perguntas', 'Não há mais perguntas registradas!')

    def revisar_resposta(self):
        resposta_usuario = self.r_e.get()  # Obtém o texto da entrada
        
        if resposta_usuario.strip().lower() == self.g.lower():  # Comparação sem diferenciar maiúsculas
            messagebox.showinfo('Certa resposta', 'Você acertou a resposta!')
        else:
            messagebox.showinfo('Resposta errada', 'Você errou a resposta.')

    def selecionar_pergunta(self):
        
        with conexao.cursor() as cursor:
        
            sql = 'SELECT Perguntas, Respostas FROM estudos ORDER BY RAND() LIMIT 1'  # Aleatório para novas perguntas
            cursor.execute(sql)
            resultado = cursor.fetchone()

        if resultado:
            
            self.f = resultado[0].strip()  # Acessa a pergunta
            self.g = resultado[1].strip()  # Acessa a resposta
        
        else:
            
            self.f = None  
            self.g = None

    def lista(self):
        self.janela.destroy()
        self.janela2 = tk.Tk()
        self.janela2.title('Registro de Perguntas e Respostas')
        self.janela2.state('zoomed')

        tk.Label(self.janela2, text='Registro de Perguntas e Respostas', font=('Arial', 16)).pack(pady=10)

        pe = tk.Label(self.janela2, text='Digite sua pergunta:')
        pe.pack(pady=5)

        self.p_e = tk.Entry(self.janela2, width=40)
        self.p_e.pack(pady=5)

        tk.Label(self.janela2, text='Digite sua resposta:').pack(pady=5)
        self.answer_entry = tk.Entry(self.janela2, width=40)
        self.answer_entry.pack(pady=5)

        tk.Button(self.janela2, text='Registrar Pergunta e Resposta', command=self.registra_pergunta).pack(pady=10)

        self.listbox = tk.Listbox(self.janela2, width=50, height=10)
        self.listbox.pack(pady=10)

        tk.Button(self.janela2, text='Apagar Seleção', command=self.deletar).pack(pady=5)

        b_r = tk.Button(self.janela2, text='Retornar', height=2, width=17, border=3, borderwidth=3, command=lambda: self.retornar(self.janela2))
        b_r.place(rely=0.94, relx=0.02)

        b_s = tk.Button(self.janela2, text='Sair', height=2, width=17, border=3, borderwidth=3, command=lambda: self.sair(self.janela2))
        b_s.place(rely=0.94, relx=0.9)

        self.carregar_perguntas() 
        
    def deletar(self):
        try:
            selected_index = self.listbox.curselection()  
            if selected_index:  # Verifica se há algo selecionado
                selected_index = selected_index[0]  
                selected_item = self.listbox.get(selected_index)
                item_id = int(selected_item.split('|')[0].split(': ')[1])  

                with conexao.cursor() as cursor:
                    sql = 'DELETE FROM estudos WHERE id = %s'
                    cursor.execute(sql, (item_id,))
                    conexao.commit()

                self.listbox.delete(selected_index)
                messagebox.showinfo('Sucesso', 'Pergunta e resposta apagadas com sucesso!')
            else:
                messagebox.showwarning('Aviso', 'Por favor, selecione uma pergunta e resposta para apagar.')
        
        except pymysql.Error as error:
            messagebox.showerror('Erro', f'Ocorreu um erro ao apagar a pergunta: {error}')
        
    def registra_pergunta(self):
        self.question = self.p_e.get()
        self.answer = self.answer_entry.get()
    
        try:
            with conexao.cursor() as cursor:
                if not self.question or not self.answer:
                    messagebox.showwarning('Aviso', 'Por favor, preencha tanto a pergunta quanto a resposta.')
                    return
                
                sql = 'INSERT INTO estudos(Perguntas, Respostas) VALUES(%s, %s)'
                cursor.execute(sql, (self.question, self.answer))
                conexao.commit()
                self.listbox.insert(tk.END, f'Pergunta: {self.question} | Resposta: {self.answer}')
                self.p_e.delete(0, tk.END)
                self.answer_entry.delete(0, tk.END)
                messagebox.showinfo('Sucesso', 'Pergunta e resposta registradas com sucesso!')
    
        except pymysql.Error as error:
            conexao.rollback()
            messagebox.showerror('Erro', f'Ocorreu um erro ao registrar a pergunta: {error}')
        
    def carregar_perguntas(self):
        try:
            with conexao.cursor() as cursor:
                sql = 'SELECT id, Perguntas, Respostas FROM estudos'
                cursor.execute(sql)
                resultado = cursor.fetchall()
            
                self.listbox.delete(0, tk.END)
                for id, pergunta, resposta in resultado:
                    self.listbox.insert(tk.END, f'ID: {id} | Pergunta: {pergunta} | Resposta: {resposta}')
                
        except pymysql.Error as error:
            messagebox.showerror('Erro', f'Ocorreu um erro ao carregar as perguntas: {error}')

    def sair(self, janela_atual):
        r = messagebox.askquestion('Fechar a janela', 'Você realmente deseja fechar a janela?')
        if r.lower() == 'yes':
            janela_atual.destroy()

    def retornar(self, janela_atual):
        r = messagebox.askquestion('Retornar janela', 'Você realmente deseja retornar ao menu?')
        if r.lower() == 'yes':
            janela_atual.destroy()
            self.janela_principal()
    
BrainBuster()