
#========================================================================
# 08_conta.py
#========================================================================

# Exercício 08 — Conta com operações validadas

class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        return False


conta1 = Conta("Marina")
conta2 = Conta("Pedro")

print("Depósito de 50:", conta1.depositar(50))
print("Saque de 20:", conta1.sacar(20))
print("Saque de 40:", conta1.sacar(40))
print("Depósito de -10:", conta1.depositar(-10))

print("Saldo da primeira conta:", conta1.saldo)
print("Saldo da segunda conta:", conta2.saldo)


#========================================================================
# 09_biblioteca.py
#========================================================================

# Exercício 09 — Biblioteca com menu

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False


livros = [
    Livro("O Hobbit"),
    Livro("Dom Casmurro"),
    Livro("O Pequeno Príncipe")
]

opcao = -1

while opcao != 0:
    print("\n===== BIBLIOTECA =====")
    print("1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        for livro in livros:
            if livro.emprestado:
                disponibilidade = "Emprestado"
            else:
                disponibilidade = "Disponível"

            print(livro.titulo, "-", disponibilidade)

    elif opcao == 2:
        titulo = input("Digite o título do livro: ")
        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.emprestar():
                    print("Livro emprestado com sucesso.")
                else:
                    print("Este livro já está emprestado.")
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == 3:
        titulo = input("Digite o título do livro: ")
        encontrado = False

        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.devolver():
                    print("Livro devolvido com sucesso.")
                else:
                    print("Este livro já está disponível.")
                break

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == 0:
        print("Encerrando a biblioteca...")

    else:
        print("Opção desconhecida.")
