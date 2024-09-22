from tkinter import messagebox
import tkinter as tk
import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'high'
)

janela = ''
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
        
def entrar():
    
    global  s_es, n_es, janela3
    
    nomes = n_es.get()
    senha = s_es.get()
        
    try:
        
       with conexao.cursor() as cursor:
           
            sql = 'select * from registro WHERE nome = %s AND senha = %s'
            cursor.execute(sql, (nomes, senha))
            w = cursor.fetchone()
            
            if w == None:
                messagebox.showinfo('Acesso Negado!', 'Acesso negado, verifique as informações inseridas ou se registre!')

            else:
                messagebox.showinfo('Acesso aceito!', f'Seja bem-vindo(a) {nomes}')
                janela3.destroy()
                perguntass()
                
    except pymysql.Error as error:
        conexao.rollback()
        messagebox.showerror('Erro', f'{error}')
        
                 

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
                r = messagebox.showinfo('Usuario aceito', 'Usuário registrado com sucesso, agora façã login!')
                
    except pymysql.Error as error:
        conexao.rollback()
        messagebox.showerror('Erro', f'{error}')
        
            
class perguntass:
    def __init__(self, titulo):
        self.titulo = titulo
        self.titulo.title("Sistema de Perguntas e Respostas")
        self.titulo.geometry("400x400")

        self.temas = {}
        self.tema_atual = ""
        self.perguntas = []
        self.respostas = []
        self.indice_pergunta = 0

        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=20)

        self.label_tema = tk.Label(self.frame, text="Tema:")
        self.label_tema.pack()

        self.entry_tema = tk.Entry(self.frame)
        self.entry_tema.pack()

        self.botao_adicionar_tema = tk.Button(self.frame, text="Adicionar Tema", command=self.adicionar_tema)
        self.botao_adicionar_tema.pack(pady=10)

        self.botao_iniciar_quiz = tk.Button(self.frame, text="Iniciar Quiz", command=self.iniciar_quiz)
        self.botao_iniciar_quiz.pack(pady=10)

        self.label_pergunta = tk.Label(self.master, text="", wraplength=300)
        self.label_pergunta.pack(pady=10)

        self.entry_resposta = tk.Entry(self.master)
        self.entry_resposta.pack(pady=10)

        self.botao_responder = tk.Button(self.master, text="Responder", command=self.responder)
        self.botao_responder.pack(pady=10)

    def adicionar_tema(self):
        tema = self.entry_tema.get()
        if tema and tema not in self.temas:
            self.temas[tema] = []
            self.entry_tema.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f"Tema '{tema}' adicionado!")
        else:
            messagebox.showwarning("Aviso", "Tema inválido ou já existe.")

    def iniciar_quiz(self):
        tema = simpledialog.askstring("Escolha um Tema", "Digite o tema do quiz:")
        if tema in self.temas:
            self.tema_atual = tema
            self.perguntas.clear()
            self.respostas.clear()

            num_perguntas = simpledialog.askinteger("Número de Perguntas", "Quantas perguntas deseja adicionar?")
            for _ in range(num_perguntas):
                pergunta = simpledialog.askstring("Pergunta", f"Digite a pergunta {_ + 1}:")
                resposta = simpledialog.askstring("Resposta", "Digite a resposta:")
                self.temas[tema].append((pergunta, resposta))

            self.perguntas, self.respostas = zip(*self.temas[tema])
            self.indice_pergunta = 0
            self.embaralhar_perguntas()
            self.mostrar_pergunta()
        else:
            messagebox.showwarning("Aviso", "Tema não encontrado.")

    def mostrar_pergunta(self):
        if self.indice_pergunta < len(self.perguntas):
            self.label_pergunta.config(text=self.perguntas[self.indice_pergunta])
            self.entry_resposta.delete(0, tk.END)
        else:
            messagebox.showinfo("Fim do Quiz", "Você respondeu todas as perguntas!")

    def responder(self):
        resposta_usuario = self.entry_resposta.get().strip()
        resposta_correta = self.respostas[self.indice_pergunta]
        
        if resposta_usuario.lower() == resposta_correta.lower():
            self.indice_pergunta += 1
            self.mostrar_pergunta()
        else:
            messagebox.showwarning("Resposta Errada", "Você errou a resposta!")
            self.embaralhar_perguntas()
            self.mostrar_pergunta()

    def embaralhar_perguntas(self):
        combined = list(zip(self.perguntas, self.respostas))
        random.shuffle(combined)
        self.perguntas, self.respostas = zip(*combined)
        
def login():
    
    global janela3, janela, s_es, n_es
    
    janela.destroy()
    
    janela3 = tk.Tk()
    janela3.title('Entrar')
    
    e = tk.Label(janela3, text='Login', font=('Arial', 20))
    e.place(rely=0.15, relx=0.46)
    
    n_t = tk.Label(janela3, text='Nome', font=('Arial', 16))
    n_t.place(rely=0.3, relx=0.43)
    
    n_es = tk.Entry(janela3, font=20, border=3, borderwidth=3)
    n_es.place(rely=0.305, relx=0.47)
    
    s_t = tk.Label(janela3, text='senha', font=('Arial', 16))
    s_t.place(rely=0.35, relx=0.43)
    
    s_es = tk.Entry(janela3,font=20, border=3, borderwidth=3, show='*')
    s_es.place(rely=0.353, relx=0.47)
    
    b = tk.Button(janela3, text='login', height=1, width=8, border=3, borderwidth=3, command=entrar)
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