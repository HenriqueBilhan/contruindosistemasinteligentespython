from pathlib import Path

code = '''import tkinter as tk
from tkinter import messagebox


def centralizar(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def exercicio_01():
    janela = tk.Toplevel()
    janela.title("Minha Aplicação")
    janela.geometry("300x200")
    janela.resizable(False, False)
    centralizar(janela, 300, 200)

    rotulo = tk.Label(janela, text="Olá, mundo!", font=("Arial", 14))
    rotulo.place(relx=0.5, rely=0.5, anchor="center")


def exercicio_02():
    janela = tk.Toplevel()
    janela.title("Contador de cliques")
    janela.geometry("300x180")
    janela.resizable(False, False)
    centralizar(janela, 300, 180)

    cliques = 0
    rotulo = tk.Label(janela, text="Cliques: 0", font=("Arial", 14))
    rotulo.pack(pady=30)

    def contar():
        nonlocal cliques
        cliques += 1
        rotulo.config(text=f"Cliques: {cliques}")

    botao = tk.Button(janela, text="Clique aqui", command=contar)
    botao.pack()


def exercicio_03():
    janela = tk.Toplevel()
    janela.title("Formulário de cadastro")
    janela.geometry("400x300")
    janela.resizable(False, False)
    centralizar(janela, 400, 300)

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_nome = tk.Entry(janela, width=30)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entrada_idade = tk.Entry(janela, width=30)
    entrada_idade.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(janela, text="E-mail:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entrada_email = tk.Entry(janela, width=30)
    entrada_email.grid(row=2, column=1, padx=10, pady=10)

    resultado = tk.Label(janela, text="", wraplength=360, justify="left")
    resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=15)

    def cadastrar():
        nome = entrada_nome.get().strip()
        idade = entrada_idade.get().strip()
        email = entrada_email.get().strip()

        if not nome or not idade or not email:
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
            return

        try:
            idade_numero = int(idade)
            if idade_numero <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Informe uma idade válida.", parent=janela)
            return

        resultado.config(text=f"Cadastro realizado!\\nNome: {nome}\\nIdade: {idade_numero}\\nE-mail: {email}")

    tk.Button(janela, text="Cadastrar", command=cadastrar).grid(
        row=3, column=0, columnspan=2, pady=10
    )


def exercicio_04():
    janela = tk.Toplevel()
    janela.title("Calculadora simples")
    janela.geometry("380x260")
    janela.resizable(False, False)
    centralizar(janela, 380, 260)

    tk.Label(janela, text="Primeiro valor:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entrada_a = tk.Entry(janela, width=22)
    entrada_a.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Segundo valor:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entrada_b = tk.Entry(janela, width=22)
    entrada_b.grid(row=1, column=1, padx=10, pady=10)

    resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12))
    resultado.grid(row=3, column=0, columnspan=2, pady=20)

    def calcular(operacao):
        try:
            a = float(entrada_a.get().replace(",", "."))
            b = float(entrada_b.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite dois valores numéricos válidos.", parent=janela)
            return

        if operacao == "+":
            valor = a + b
        elif operacao == "-":
            valor = a - b
        elif operacao == "*":
            valor = a * b
        else:
            if b == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero.", parent=janela)
                return
            valor = a / b

        resultado.config(text=f"Resultado: {valor:g}")

    botoes = tk.Frame(janela)
    botoes.grid(row=2, column=0, columnspan=2, pady=15)

    for simbolo in ["+", "-", "*", "/"]:
        tk.Button(
            botoes,
            text=simbolo,
            width=5,
            command=lambda op=simbolo: calcular(op)
        ).pack(side="left", padx=5)


def exercicio_05():
    janela = tk.Toplevel()
    janela.title("Cadastro de personagens")
    janela.geometry("550x480")
    janela.resizable(False, False)
    centralizar(janela, 550, 480)

    personagens = []

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    entrada_nome = tk.Entry(janela, width=30)
    entrada_nome.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(janela, text="Classe:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    entrada_classe = tk.Entry(janela, width=30)
    entrada_classe.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(janela, text="Nível:").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    entrada_nivel = tk.Entry(janela, width=30)
    entrada_nivel.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(janela, text="Pontos de vida:").grid(row=3, column=0, padx=10, pady=8, sticky="e")
    entrada_vida = tk.Entry(janela, width=30)
    entrada_vida.grid(row=3, column=1, padx=10, pady=8)

    lista = tk.Listbox(janela, width=65, height=12)
    lista.grid(row=5, column=0, columnspan=2, padx=15, pady=15)

    def cadastrar_personagem():
        nome = entrada_nome.get().strip()
        classe = entrada_classe.get().strip()
        nivel = entrada_nivel.get().strip()
        vida = entrada_vida.get().strip()

        if not nome or not classe or not nivel or not vida:
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
            return

        try:
            nivel_numero = int(nivel)
            vida_numero = int(vida)
            if nivel_numero <= 0 or vida_numero <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Nível e pontos de vida devem ser números inteiros positivos.",
                parent=janela
            )
            return

        personagem = {
            "nome": nome,
            "classe": classe,
            "nivel": nivel_numero,
            "vida": vida_numero
        }
        personagens.append(personagem)

        lista.insert(
            tk.END,
            f"{nome} | Classe: {classe} | Nível: {nivel_numero} | Vida: {vida_numero}"
        )

        entrada_nome.delete(0, tk.END)
        entrada_classe.delete(0, tk.END)
        entrada_nivel.delete(0, tk.END)
        entrada_vida.delete(0, tk.END)
        entrada_nome.focus()

    tk.Button(
        janela,
        text="Cadastrar personagem",
        command=cadastrar_personagem
    ).grid(row=4, column=0, columnspan=2, pady=10)


app = tk.Tk()
app.title("Exercícios de Tkinter")
app.geometry("350x390")
app.resizable(False, False)
centralizar(app, 350, 390)

tk.Label(
    app,
    text="Lista de exercícios - Tkinter",
    font=("Arial", 15, "bold")
).pack(pady=20)

tk.Button(app, text="Exercício 01 - Minha primeira aplicação", width=38, command=exercicio_01).pack(pady=6)
tk.Button(app, text="Exercício 02 - Contador de cliques", width=38, command=exercicio_02).pack(pady=6)
tk.Button(app, text="Exercício 03 - Formulário de cadastro", width=38, command=exercicio_03).pack(pady=6)
tk.Button(app, text="Exercício 04 - Calculadora simples", width=38, command=exercicio_04).pack(pady=6)
tk.Button(app, text="Exercício 05 - Cadastro de personagens", width=38, command=exercicio_05).pack(pady=6)

app.mainloop()
'''

path = Path("/mnt/data/exercicios_tkinter.py")
path.write_text(code, encoding="utf-8")
print(f"Arquivo criado: {path}")
