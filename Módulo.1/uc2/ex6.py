# Atividade 1
""" 
numero = int(input("Digite um número positivo: "))

if numero > 0:
    for i in range(1, numero + 1):
        print(i)
else:
    print("Valor inválido!")
 """
# Atividade 2
""" 
numero = int(input("Digite um número maior ou igual a zero: "))

if numero >= 0:
    for i in range(numero, -1, -1):
        print(i)

    print("Lançamento realizado!")
else:
    print("Valor inválido!")    """

# Atividade 3
""" 
limite = int(input("Digite um número positivo: "))

if limite <= 0:
    print("Limite inválido!")

elif limite == 1:
    print("Não há pares no intervalo.")

else:
    for i in range(2, limite + 1, 2):
        print(i) """
# Atividade 4
""" numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado) """

# Atividade 5
"""
soma = 0
positivos = 0

for i in range(1, 7):
    numero = int(input("Digite um número: "))

    soma += numero

    if numero > 0:
        positivos += 1

print("Soma total:", soma)
print("Quantidade de positivos:", positivos)

"""
# Atividade 6
"""
quantidade = int(input("Quantidade de alunos: "))

if quantidade <= 0:
    print("Quantidade inválida!")

else:
    soma = 0
    aprovados = 0

    for aluno in range(1, quantidade + 1):
        nota = float(input("Digite a nota do aluno: "))

        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida! Digite novamente: "))

        soma += nota

        if nota >= 7:
            aprovados += 1

    media = soma / quantidade

    print("Média da turma:", media)
    print("Alunos com nota a partir de 7:", aprovados)
"""
# Atividade 7

""" palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

contador = 0

for caractere in palavra:
    if caractere == letra:
        contador += 1

print("A letra aparece", contador, "vezes.") """
# Atividade 8
""" 
codigo_correto = "ROBO123"
acertou = False

for tentativa in range(1, 4):
    print("Tentativa:", tentativa)

    codigo = input("Digite o código: ")

    if codigo == codigo_correto:
        acertou = True
        break

    else:
        print("Código incorreto!")

if acertou:
    print("Acesso autorizado!")
else:
    print("As tentativas acabaram!") """
# Atividade 9
""" energia = 100
soma = 0
missoes = 0

for missao in range(1, 6):

    if energia < 25:
        print("Energia insuficiente!")
        break

    print("Missão:", missao)

    pontuacao = int(input("Digite a pontuação (0 a 100): "))

    while pontuacao < 0 or pontuacao > 100:
        pontuacao = int(input("Pontuação inválida! Digite novamente: "))

    energia -= 25
    soma += pontuacao
    missoes += 1

print("Missões realizadas:", missoes)
print("Pontuação total:", soma)
print("Energia restante:", energia)

if missoes > 0:
    media = soma / missoes
    print("Média de pontos:", media)
else:
    print("Não foi possível calcular a média.") """
# Atividade 10 desafio final
""" total = 0

for numero in range(2, 9, 2):
    total += numero
    print(numero, total)

print("Total:", total) """