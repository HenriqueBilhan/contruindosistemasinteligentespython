import tkinter as tk

janela = tk.Tk()

janela.title("Minha primeira aplicação")
janela.geometry("400x300")

texto = tk.Label(
    janela,
    text="Escreva seu nome, seu email e sua cidade",
    font=("Arial", 20),
    fg='blue'
)

texto.pack(pady=20)

entrada = tk.Entry(
    janela,
    fg='black',
    
  width=30)

entrada.pack(pady=10)

email = tk.Entry(
    janela,
    fg='black',
    
  width=30)

email.pack(pady=10)

cidade = tk.Entry(
    janela,
    fg='black',
    
  width=30)

cidade.pack(pady=10)
aceitar = tk.Button(
  janela,
  text="Aceitar",
)
janela.mainloop()