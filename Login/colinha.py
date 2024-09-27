from tkinter import messagebox, simpledialog
import tkinter as tk
import pymysql
import random

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='high'
)

class BrainBuster:
    def __init__(self, titulo):
        quiz = tk.Tk()
        quiz.title('BrainBuster')
        
        t = tk.Label(quiz, text='BrainBuster', font=('Georgia', 20))
        t.place(rely=0.15, relx=0.44)
    
        b_r = tk.Button(quiz, text='Estudos', height=2, width =15, border =3, borderwidth=3,)
        b_r.place(rely=0.45, relx=0.35)
    
        b_l = tk.Button(quiz, text='Diversão', height=2, width=15, border=3, borderwidth=3,)
        b_l.place(rely=0.45, relx=0.45)
    
        b_i = tk.Button(quiz, text='Lista', height=2, width=15, border=3, borderwidth=3, )
        b_i.place(rely =0.45, relx=0.55)
        
        b_r = tk.Button(quiz, text='Retornar', height=2, width=17, border=3, borderwidth=3,)
        b_r.place(rely=0.94, relx=0.02)
    
        b_s = tk.Button(quiz, text='Sair', height=2, width=17, border=3, borderwidth=3,)
        b_s.place(rely=0.94, relx=0.9)
        
        quiz.mainloop()
        
    def perguntas(self):
        print()

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

BrainBuster('BrainBuster')