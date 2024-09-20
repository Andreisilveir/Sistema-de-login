import tkinter as tk
import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'high'
)

cursor = conexao.cursor()

janela = tk.Tk()
janela.title('menu')

janela.mainloop()