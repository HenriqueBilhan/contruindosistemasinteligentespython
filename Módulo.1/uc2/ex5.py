# Exercício 01 — Contagem progressiva
numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0:
    print("O número deve ser positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

contador = 1
while contador <= numero:
    print(contador)
    contador += 1


# Exercício 02 — Contagem regressiva
numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))
while numero <= 0:
    print("O número deve ser positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1
print("Lançamento realizado!")


# Exercício 03 — Tabuada
numero = int(input("Digite um número inteiro para ver a tabuada: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1


# Exercício 04 — Somando cinco números
soma = 0
contador = 1
while contador <= 5:
    numero = int(input(f"Digite o {contador}º número inteiro: "))
    soma += numero
    contador += 1
print("A soma dos cinco números é:", soma)


# Exercício 05 — Média da turma
quantidade_alunos = int(input("Digite a quantidade de alunos da turma: "))
while quantidade_alunos <= 0:
    print("A quantidade de alunos deve ser maior que zero.")
    quantidade_alunos = int(input("Digite a quantidade de alunos da turma: "))

soma_notas = 0
contador = 1
while contador <= quantidade_alunos:
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    soma_notas += nota
    contador += 1

media = soma_notas / quantidade_alunos
print(f"A média geral da turma é: {media:.2f}")


# Exercício 06 — Validando uma nota
nota = float(input("Digite uma nota entre 0 e 10: "))
while not 0 <= nota <= 10:
    print("Nota inválida.")
    nota = float(input("Digite uma nota entre 0 e 10: "))
print("Nota registrada com sucesso!")


# Exercício 07 — Menu de operações
while True:
    print("\n=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar maioridade")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado da soma:", numero1 + numero2)
    elif opcao == "2":
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    elif opcao == "0":
        print("Saindo do menu...")
        break
    else:
        print("Opção inválida. Tente novamente.")


# Exercício 08 — Caixa eletrônico (desafio extra)
saldo = 500.00
quantidade_depositos = 0
quantidade_saques = 0

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            quantidade_depositos += 1
            print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")
        else:
            print("O valor do depósito deve ser maior que zero.")
    elif opcao == "3":
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            quantidade_saques += 1
            print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")
    elif opcao == "0":
        print(f"Depósitos realizados: {quantidade_depositos}")
        print(f"Saques realizados: {quantidade_saques}")
        print("Saindo do caixa eletrônico...")
        break
    else:
        print("Opção inválida. Tente novamente.")
