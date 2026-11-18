from pathlib import Path
import py_compile

code = '''import tkinter as tk
from tkinter import messagebox


def exercicio_01():
    janela = tk.Toplevel()
    janela.title("Minha Aplicação")
    janela.geometry("300x200")
    janela.resizable(False, False)

    rotulo = tk.Label(janela, text="Olá, mundo!", font=("Arial", 14))
    rotulo.pack(expand=True)


def exercicio_02():
    janela = tk.Toplevel()
    janela.title("Contador de cliques")
    janela.geometry("300x180")
    janela.resizable(False, False)

    contador = 0

    rotulo = tk.Label(janela, text="Cliques: 0", font=("Arial", 14))
    rotulo.pack(pady=25)

    def contar_clique():
        nonlocal contador
        contador += 1
        rotulo.config(text=f"Cliques: {contador}")

    botao = tk.Button(janela, text="Clique aqui", command=contar_clique)
    botao.pack()


def exercicio_03():
    janela = tk.Toplevel()
    janela.title("Formulário de cadastro")
    janela.geometry("400x280")
    janela.resizable(False, False)

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_nome = tk.Entry(janela, width=30)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entrada_idade = tk.Entry(janela, width=30)
    entrada_idade.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(janela, text="E-mail:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entrada_email = tk.Entry(janela, width=30)
    entrada_email.grid(row=2, column=1, padx=10, pady=10)

    resultado = tk.Label(janela, text="", justify="left", wraplength=360)
    resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=15)

    def cadastrar():
        nome = entrada_nome.get().strip()
        idade = entrada_idade.get().strip()
        email = entrada_email.get().strip()

        if not nome or not idade or not email:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            idade_numero = int(idade)
            if idade_numero <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe uma idade válida.")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Erro", "Informe um e-mail válido.")
            return

        resultado.config(
            text=f"Cadastro realizado!\\\\nNome: {nome}\\\\nIdade: {idade_numero}\\\\nE-mail: {email}"
        )

    botao = tk.Button(janela, text="Cadastrar", command=cadastrar)
    botao.grid(row=3, column=0, columnspan=2, pady=5)


def exercicio_04():
    janela = tk.Toplevel()
    janela.title("Calculadora simples")
    janela.geometry("380x260")
    janela.resizable(False, False)

    tk.Label(janela, text="Primeiro valor:").grid(
        row=0, column=0, padx=10, pady=10, sticky="e"
    )
    entrada1 = tk.Entry(janela, width=20)
    entrada1.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Segundo valor:").grid(
        row=1, column=0, padx=10, pady=10, sticky="e"
    )
    entrada2 = tk.Entry(janela, width=20)
    entrada2.grid(row=1, column=1, padx=10, pady=10)

    resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12))
    resultado.grid(row=3, column=0, columnspan=2, pady=20)

    def calcular(operacao):
        try:
            valor1 = float(entrada1.get().replace(",", "."))
            valor2 = float(entrada2.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite dois valores numéricos válidos.")
            return

        if operacao == "+":
            resposta = valor1 + valor2
        elif operacao == "-":
            resposta = valor1 - valor2
        elif operacao == "*":
            resposta = valor1 * valor2
        else:
            if valor2 == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero.")
                return
            resposta = valor1 / valor2

        resultado.config(text=f"Resultado: {resposta:g}")

    frame_botoes = tk.Frame(janela)
    frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

    for operacao in ["+", "-", "*", "/"]:
        botao = tk.Button(
            frame_botoes,
            text=operacao,
            width=5,
            command=lambda op=operacao: calcular(op)
        )
        botao.pack(side="left", padx=5)


class Personagem:
    def __init__(self, nome, classe, nivel, pontos_vida):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = pontos_vida

    def __str__(self):
        return (
            f"Nome: {self.nome} | Classe: {self.classe} | "
            f"Nível: {self.nivel} | Vida: {self.pontos_vida} PV"
        )


def exercicio_05():
    janela = tk.Toplevel()
    janela.title("Cadastro de personagens")
    janela.geometry("600x450")
    janela.resizable(False, False)

    personagens = []

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    entrada_nome = tk.Entry(janela, width=30)
    entrada_nome.grid(row=0, column=1, padx=10, pady=8, sticky="w")

    tk.Label(janela, text="Classe:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    entrada_classe = tk.Entry(janela, width=30)
    entrada_classe.grid(row=1, column=1, padx=10, pady=8, sticky="w")

    tk.Label(janela, text="Nível:").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    entrada_nivel = tk.Entry(janela, width=30)
    entrada_nivel.grid(row=2, column=1, padx=10, pady=8, sticky="w")

    tk.Label(janela, text="Pontos de vida:").grid(
        row=3, column=0, padx=10, pady=8, sticky="e"
    )
    entrada_vida = tk.Entry(janela, width=30)
    entrada_vida.grid(row=3, column=1, padx=10, pady=8, sticky="w")

    tk.Label(janela, text="Personagens cadastrados:").grid(
        row=5, column=0, columnspan=2, pady=(15, 5)
    )

    lista = tk.Listbox(janela, width=75, height=10)
    lista.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def cadastrar_personagem():
        nome = entrada_nome.get().strip()
        classe = entrada_classe.get().strip()
        nivel = entrada_nivel.get().strip()
        vida = entrada_vida.get().strip()

        if not nome or not classe or not nivel or not vida:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            nivel_numero = int(nivel)
            vida_numero = int(vida)

            if nivel_numero <= 0 or vida_numero <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Nível e pontos de vida devem ser números inteiros positivos."
            )
            return

        personagem = Personagem(nome, classe, nivel_numero, vida_numero)
        personagens.append(personagem)
        lista.insert(tk.END, str(personagem))

        entrada_nome.delete(0, tk.END)
        entrada_classe.delete(0, tk.END)
        entrada_nivel.delete(0, tk.END)
        entrada_vida.delete(0, tk.END)
        entrada_nome.focus()

    botao = tk.Button(
        janela,
        text="Cadastrar personagem",
        command=cadastrar_personagem
    )
    botao.grid(row=4, column=0, columnspan=2, pady=10)


janela_principal = tk.Tk()
janela_principal.title("Lista de exercícios - Tkinter")
janela_principal.geometry("420x390")
janela_principal.resizable(False, False)

tk.Label(
    janela_principal,
    text="Exercícios de Python - Tkinter",
    font=("Arial", 15, "bold")
).pack(pady=20)

tk.Label(
    janela_principal,
    text="Selecione um exercício:",
    font=("Arial", 10)
).pack(pady=5)

exercicios = [
    ("Exercício 01 - Minha primeira aplicação", exercicio_01),
    ("Exercício 02 - Contador de cliques", exercicio_02),
    ("Exercício 03 - Formulário de cadastro", exercicio_03),
    ("Exercício 04 - Calculadora simples", exercicio_04),
    ("Exercício 05 - Cadastro de personagens", exercicio_05)
]

for texto, funcao in exercicios:
    tk.Button(
        janela_principal,
        text=texto,
        width=42,
        command=funcao
    ).pack(pady=7)

janela_principal.mainloop()
'''

path = Path("/mnt/data/exercicios_tkinter.py")
path.write_text(code, encoding="utf-8")
py_compile.compile(str(path), doraise=True)
print("Arquivo refeito e validado. Sem comentários, com os cinco exercícios em blocos separados.")
