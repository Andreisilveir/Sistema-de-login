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

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz de Perguntas e Respostas")
        self.perguntas = []
        self.indice_pergunta = 0
        self.pontuacao = 0

        # Interface para adicionar perguntas
        self.frame_adicionar_pergunta = tk.Frame(master)
        self.frame_adicionar_pergunta.pack(pady=10)

        tk.Label(self.frame_adicionar_pergunta, text="Pergunta:").grid(row=0, column=0)
        self.entrada_pergunta = tk.Entry(self.frame_adicionar_pergunta, width=40)
        self.entrada_pergunta.grid(row=0, column=1)

        tk.Label(self.frame_adicionar_pergunta, text="Resposta Correta:").grid(row=1, column=0)
        self.entrada_resposta_correta = tk.Entry(self.frame_adicionar_pergunta, width=40)
        self.entrada_resposta_correta.grid(row=1, column=1)

        tk.Button(self.frame_adicionar_pergunta, text="Adicionar Pergunta", command=self.adicionar_pergunta).grid(row=2, columnspan=2, pady=10)

        self.label_pergunta = tk.Label(master, text="", wraplength=300)
        self.label_pergunta.pack(pady=20)

        self.entrada_resposta = tk.Entry(master, width=40)
        self.entrada_resposta.pack(pady=10)

        self.botao_enviar = tk.Button(master, text="Enviar Resposta", command=self.verificar_resposta)
        self.botao_enviar.pack(pady=5)

        self.botao_proxima = tk.Button(master, text="Próxima Pergunta", command=self.proxima_pergunta)
        self.botao_proxima.pack(pady=5)

        self.botao_embaralhar = tk.Button(master, text="Embaralhar Perguntas", command=self.embaralhar_perguntas)
        self.botao_embaralhar.pack(pady=5)

    def adicionar_pergunta(self):
        pergunta = self.entrada_pergunta.get()
        resposta_correta = self.entrada_resposta_correta.get()

        if pergunta and resposta_correta:
            self.perguntas.append({
                "pergunta": pergunta,
                "resposta": resposta_correta
            })
            messagebox.showinfo("Sucesso", "Pergunta adicionada com sucesso!")
            self.limpar_entradas()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    def limpar_entradas(self):
        self.entrada_pergunta.delete(0, tk.END)
        self.entrada_resposta_correta.delete(0, tk.END)

    def embaralhar_perguntas(self):
        random.shuffle(self.perguntas)
        self.indice_pergunta = 0
        self.pontuacao = 0
        self.exibir_pergunta()

    def exibir_pergunta(self):
        if self.indice_pergunta < len(self.perguntas):
            self.label_pergunta.config(text=self.perguntas[self.indice_pergunta]["pergunta"])
            self.entrada_resposta.delete(0, tk.END)
        else:
            self.label_pergunta.config(text=f"Sua pontuação: {self.pontuacao}/{len(self.perguntas)}")
            self.entrada_resposta.pack_forget()
            self.botao_enviar.pack_forget()
            self.botao_proxima.pack_forget()
            self.botao_embaralhar.pack_forget()

    def verificar_resposta(self):
        resposta_usuario = self.entrada_resposta.get()
        resposta_correta = self.perguntas[self.indice_pergunta]["resposta"]

        if resposta_usuario.strip().lower() == resposta_correta.strip().lower():
            self.pontuacao += 1
            messagebox.showinfo("Correto!", "Você acertou!")
        else:
            messagebox.showinfo("Incorreto", f"A resposta correta é: {resposta_correta}")

    def proxima_pergunta(self):
        self.indice_pergunta += 1
        self.exibir_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    app_quiz = QuizApp(root)
    root.mainloop()