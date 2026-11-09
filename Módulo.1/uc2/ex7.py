

# Atividade 1

""" 
objetos = ["Mesa", "Cadeira", "Celular", "Livro", "Caneta"]

print("Lista completa:", objetos)
print("Quantidade:", len(objetos))

print("Primeiro objeto:", objetos[0])
print("Último objeto:", objetos[-1])

objetos[2] = "Computador"

print("Lista atualizada:", objetos) """

# Atividade 2

colegas = []

for i in range(4):
    nome = input("Digite o nome do colega: ")

    colegas.append(nome)

print("Colegas cadastrados:")

for nome in colegas:
    print(nome)

# Atividade 3
""" numeros = []

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
print("Lista:", numeros)
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Maior número:", max(numeros))
print("Menor número:", min(numeros)) """

# Atividade 4

""" mochila = ["corda", "água", "mapa", "água"]
item = input("Digite o nome do item: ")
quantidade = mochila.count(item)
if quantidade > 0:
    print("Item encontrado!")
    print("Quantidade de ocorrências:", quantidade)
else:
    print("Item não encontrado.") """

# Atividade 5

""" 
numeros = []
pares = []
for i in range(8):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Lista original:", numeros)
print("Lista de pares:", pares) """

# Atividade 6
""" 
nomes = ["Ana", "Bruno", "Ana", "Carla"]
nome = input("Digite o nome que deseja remover: ")
if nome in nomes:
    nomes.remove(nome)
    print("Nome removido com sucesso!")
else:
    print("Nome não encontrado.")
print("Lista:", nomes)
print("Quantidade restante:", len(nomes))
 """
# Atividade 7
""" 
notas = []
quantidade = int(input("Digite a quantidade de alunos: "))
if quantidade <= 0:
    print("Quantidade inválida.")
else:
    for i in range(quantidade):
        nota = float(input("Digite a nota do aluno: "))
        while nota < 0 or nota > 10:
            print("Nota inválida!")
            nota = float(input("Digite novamente: "))
        notas.append(nota)
    aprovados = 0
    for nota in notas:
        if nota >= 7:
            aprovados += 1
    print("Notas:", notas)
    print("Média:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))
    print("Notas maiores ou iguais a 7:", aprovados) """

# Atividade 8

""" fila = []
opcao = -1
while opcao != 0:
    print("\n1 - Adicionar pessoa ao final da fila")
    print("2 - Atender a primeira pessoa")
    print("3 - Mostrar a fila e sua quantidade")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Digite o nome: ")
        fila.append(nome)
        print("Pessoa adicionada!")
    elif opcao == 2:
        if len(fila) > 0:
            atendido = fila.pop(0)
            print("Pessoa atendida:", atendido)
        else:
            print("A fila está vazia!")
    elif opcao == 3:
        print("Fila atual:", fila)
        print("Quantidade de pessoas:", len(fila))
    elif opcao == 0:
        print("Programa encerrado!")
    else:
        print("Opção inválida!") """


# Atividade 9
""" pontuacoes = []
opcao = -1
while opcao != 0:
    print("\n1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        pontuacao = int(input("Digite a pontuação (0 a 100): "))
        while pontuacao < 0 or pontuacao > 100:
            print("Pontuação inválida!")
            pontuacao = int(input("Digite novamente: "))
        pontuacoes.append(pontuacao)
        print("Pontuação registrada!")
    elif opcao == 2:
        if len(pontuacoes) == 0:
            print("Não há missões registradas.")
        else:
            total = sum(pontuacoes)
            media = total / len(pontuacoes)
            maior = max(pontuacoes)

            aprovadas = []
            quantidade = 0
            for pontuacao in pontuacoes:
                if pontuacao >= 70:
                    quantidade += 1
                    aprovadas.append(pontuacao)
            print("\nRelatório de missões:")
            print("Pontuações:", pontuacoes)
            print("Quantidade:", len(pontuacoes))
            print("Total:", total)
            print("Média:", media)
            print("Maior pontuação:", maior)
            print("Missões com pelo menos 70 pontos:", quantidade)
            print("Pontuações a partir de 70:", aprovadas)
    elif opcao == 3:
        if len(pontuacoes) > 0:
            removida = pontuacoes.pop()
            print("Pontuação removida:", removida)
        else:
            print("Não há registro para desfazer.")
    elif opcao == 0:
        print("Central de missões encerrada!")
    else:
        print("Opção inválida!")
 """

