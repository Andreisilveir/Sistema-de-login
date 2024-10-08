import tkinter as tk
from tkinter import messagebox
import pymysql

import tkinter as tk
from tkinter import messagebox
import mysql.connector

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Dados do MySQL")
        
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=20)

        self.carregar_dados()

    def conectar_banco(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='seu_usuario',
                password='sua_senha',
                database='meu_banco'
            )
            return conn
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
            return None

    def carregar_dados(self):
        conn = self.conectar_banco()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pessoas")
            resultados = cursor.fetchall()

            self.listbox.delete(0, tk.END)  # Limpa o Listbox antes de carregar os dados
            for id, nome, idade in resultados:
                self.listbox.insert(tk.END, f'ID: {id}, Nome: {nome}, Idade: {idade}')

            cursor.close()
            conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()