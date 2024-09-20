import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Perguntas e Respostas")
        self.master.geometry("400x400")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()