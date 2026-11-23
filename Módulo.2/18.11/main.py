import tkinter as tk

janela = tk.Tk()

janela.title("Minha primeira aplicação")
janela.geometry("400x300")

texto =tk.Label(
    janela,
    text="Olá, mundo!",
    font=("Arial", 20),
    fg =  'blue'
)

texto.pack(pady=120)

entrada = tk.Entry(
    janela,
  width=30)
janela.mainloop()