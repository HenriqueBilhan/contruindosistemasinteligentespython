import tkinter as tk

import tkinter as tk
import math


janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("430x620")
janela.resizable(False, False)
janela.configure(bg="#20242b")

expressao = tk.StringVar()


def adicionar(valor):
    expressao.set(expressao.get() + str(valor))


def limpar():
    expressao.set("")


def apagar():
    expressao.set(expressao.get()[:-1])


def calcular():
    try:
        texto = expressao.get()

        funcoes = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
        }

        resultado = eval(texto, {"__builtins__": {}}, funcoes)

        expressao.set(str(resultado))

    except Exception:
        expressao.set("Erro")


def fatorial():
    try:
        valor = int(float(expressao.get()))

        if valor < 0:
            raise ValueError

        expressao.set(str(math.factorial(valor)))

    except Exception:
        expressao.set("Erro")


def criar_botao(texto, linha, coluna, comando, cor="#343b46"):
    botao = tk.Button(
        janela,
        text=texto,
        font=("Arial", 13, "bold"),
        bg=cor,
        fg="white",
        activebackground="#566273",
        activeforeground="white",
        relief="flat",
        command=comando
    )

    botao.grid(
        row=linha,
        column=coluna,
        padx=4,
        pady=4,
        sticky="nsew"
    )


tela = tk.Entry(
    janela,
    textvariable=expressao,
    font=("Arial", 24),
    justify="right",
    bg="#11151b",
    fg="white",
    insertbackground="white",
    relief="flat"
)

tela.grid(
    row=0,
    column=0,
    columnspan=5,
    padx=12,
    pady=20,
    ipady=20,
    sticky="nsew"
)


botoes = [
    [("sin(", "#"), ("cos(", "#"), ("tan(", "#"), ("log(", "#"), ("ln(", "#")],
    [("√", "sqrt("), ("x²", "**2"), ("xʸ", "**"), ("(", "("), (")", ")")],
    [("7", "7"), ("8", "8"), ("9", "9"), ("/", "/"), ("C", "C")],
    [("4", "4"), ("5", "5"), ("6", "6"), ("*", "*"), ("⌫", "back")],
    [("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"), ("π", "pi")],
    [("0", "0"), (".", "."), ("%", "%"), ("+", "+"), ("e", "e")],
]

for linha, grupo in enumerate(botoes, start=1):
    for coluna, (texto, valor) in enumerate(grupo):

        if valor == "C":
            comando = limpar
        elif valor == "back":
            comando = apagar
        elif valor == "sqrt(":
            comando = lambda: adicionar("sqrt(")
        else:
            comando = lambda v=valor: adicionar(v)

        cor = "#2878d0" if texto in ["C", "⌫"] else "#343b46"

        criar_botao(texto, linha, coluna, comando, cor)


criar_botao("n!", 7, 0, fatorial, "#7652b5")
criar_botao("x²", 7, 1, lambda: adicionar("**2"), "#7652b5")
criar_botao("=", 7, 2, calcular, "#168a60")
criar_botao("Ans", 7, 3, calcular, "#168a60")
criar_botao("AC", 7, 4, limpar, "#c0392b")


for coluna in range(5):
    janela.grid_columnconfigure(coluna, weight=1)

for linha in range(1, 8):
    janela.grid_rowconfigure(linha, weight=1)


janela.mainloop()
