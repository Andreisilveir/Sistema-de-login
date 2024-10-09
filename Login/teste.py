import tkinter as tk
from tkinter import messagebox
import pymysql 

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='high'
)

class BrainBuster:
    
    def __init__(self): 
        self.qa_list = []
        self.f = []  # Inicializa a lista de perguntas
        self.janela_principal()

    def janela_principal(self):
        self.janela = tk.Tk()
        self.janela.title('Menu')
        self.janela.state('zoomed')

        tk.Label(self.janela, text='BrainBuster', font=('Georgia', 20)).place(rely=0.15, relx=0.44)

        tk.Button(self.janela, text='Quiz', height=2, width=15, command=self.quiz).place(rely=0.45, relx=0.35)
        tk.Button(self.janela, text='Perguntas', height=2, width=15, command=self.lista).place(rely=0.45, relx=0.45)
        tk.Button(self.janela, text='Informações', height=2, width=15).place(rely=0.45, relx=0.55)
        tk.Button(self.janela, text='Retornar', height=2, width=17, command=lambda: self.retornar(self.janela)).place(rely=0.94, relx=0.02)
        tk.Button(self.janela, text='Sair', height=2, width=17, command=lambda: self.sair(self.janela)).place(rely=0.94, relx=0.9)

        self.janela.mainloop()

    def quiz(self):
        self.selecionar_pergunta()
        self.janela.destroy()
        self.janela1 = tk.Tk()
        self.janela1.title('Quiz')
        self.janela1.state('zoomed')
        
        if self.f:  # Verifica se a lista não está vazia
            pergunta = self.f[0][0]  # Exibe a primeira pergunta
            tk.Label(self.janela1, text=pergunta, font=('georgia', 20)).place(rely=0.2, relx=0.44)
        else:
            messagebox.showinfo('Sem perguntas', 'Nao tem pergunta registrada!')
        
        r_e = tk.Entry(self.janela1, font=2, border=3, width=15)
        r_e.place(rely=0.45, relx=0.443)
        
        tk.Button(self.janela1, text='Enviar', border=3, width=5).place(rely=0.45, relx=0.56)
        tk.Button(self.janela1, text='Pular resposta', border=3, width=10).place(rely=0.5, relx=0.47)
        tk.Button(self.janela1, text='Retornar', height=2, width=17, command=lambda: self.retornar(self.janela1)).place(rely=0.94, relx=0.02)
        tk.Button(self.janela1, text='Sair', height=2, width=17, command=lambda: self.sair(self.janela1)).place(rely=0.94, relx=0.9)

    def lista(self):
        self.janela.destroy()
        self.janela2 = tk.Tk()
        self.janela2.title('Registro de Perguntas e Respostas')
        self.janela2.state('zoomed')

        tk.Label(self.janela2, text='Registro de Perguntas e Respostas', font=('Arial', 16)).pack(pady=10)

        tk.Label(self.janela2, text='Digite sua pergunta:').pack(pady=5)
        self.p_e = tk.Entry(self.janela2, width=40)
        self.p_e.pack(pady=5)

        tk.Label(self.janela2, text='Digite sua resposta:').pack(pady=5)
        self.answer_entry = tk.Entry(self.janela2, width=40)
        self.answer_entry.pack(pady=5)

        tk.Button(self.janela2, text='Registrar Pergunta e Resposta', command=self.registra_pergunta).pack(pady=10)

        self.listbox = tk.Listbox(self.janela2, width=50, height=10)
        self.listbox.pack(pady=10)

        tk.Button(self.janela2, text='Apagar Seleção', command=self.deletar).pack(pady=5)
        tk.Button(self.janela2, text='Retornar', height=2, width=17, command=lambda: self.retornar(self.janela2)).place(rely=0.94, relx=0.02)
        tk.Button(self.janela2, text='Sair', height=2, width=17, command=lambda: self.sair(self.janela2)).place(rely=0.94, relx=0.9)

        self.carregar_perguntas()  # Carrega as perguntas ao abrir a janela
        
    def selecionar_pergunta(self):
        with conexao.cursor() as cursor:
            sql = 'SELECT Perguntas FROM estudos'
            cursor.execute(sql)
            self.f = cursor.fetchall()  # Armazena as perguntas em self.f

    def deletar(self):
        try:
            selected_index = self.listbox.curselection()[0]  # Obtém o índice selecionado
            selected_item = self.listbox.get(selected_index)
            item_id = int(selected_item.split('|')[0].split(': ')[1])  # Extrai o ID do item selecionado

            # Remover do banco de dados
            with conexao.cursor() as cursor:  # Use a conexão global
                sql = 'DELETE FROM estudos WHERE id = %s'
                cursor.execute(sql, (item_id,))
                conexao.commit()

            # Remove do Listbox
            self.listbox.delete(selected_index)
            messagebox.showinfo('Sucesso', 'Pergunta e resposta apagadas com sucesso!')
        
        except IndexError:
            messagebox.showwarning('Aviso', 'Por favor, selecione uma pergunta e resposta para apagar.')
        except pymysql.Error as error:
            messagebox.showerror('Erro', f'Ocorreu um erro ao apagar a pergunta: {error}')
        
    def registra_pergunta(self):
        self.question = self.p_e.get()
        self.answer = self.answer_entry.get()
    
        try:
            with conexao.cursor() as cursor:
                if not self.question or not self.answer:  # Verifica os valores dos campos
                    messagebox.showwarning('Aviso', 'Por favor, preencha tanto a pergunta quanto a resposta.')
                else:
                    sql = 'INSERT INTO estudos(Perguntas, Respostas) VALUES(%s, %s)'
                    cursor.execute(sql, (self.question, self.answer))
                    conexao.commit()
                
                    # Adicione a pergunta e resposta ao Listbox
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
                sql = 'SELECT Perguntas, Respostas FROM estudos'
                cursor.execute(sql)
                resultados = cursor.fetchall()
            
                # Limpa o Listbox antes de carregar os dados
                self.listbox.delete(0, tk.END)
                for pergunta, resposta in resultados:  # Adiciona cada resultado ao Listbox
                    self.listbox.insert(tk.END, f'Pergunta: {pergunta} | Resposta: {resposta}')
                
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
            self.janela_principal()  # Chama o método para reiniciar a janela principal

BrainBuster()