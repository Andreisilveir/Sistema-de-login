import tkinter as tk

janela = tk.Tk()
janela.title('menu')
janela.state('zoomed')

p = tk.Label(janela, text='Rhay', font=('Georgia', 25))
p.place(rely=0.3, relx=0.465)



janela.mainloop()