# 1 Tarefa


""" nome = input("Nome: ")
cidade = input("Cidade: ")
idade = input("Idade: ")
print("=== CADASTRO ===")
print("Nome:", nome)
print("Cidade:", cidade)
print("Idade:", idade)

 """



# 2 Tarefa 



""" preco = int(input(f"qual o preço do lanche?\n"))
quantidade = int(input(f'qual é a quantidade que foi comprada\n'))
print(f"Você comprou {quantidade}, Então você gastou {preco}")
if preco >= 50:
    preco %10
else:
    print("Você nao ganhou desconto") """



# 3 Tarefa



""" num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.") """


# 4 Tarefa


""" temperatura = int(input("Qual é a temperatura de hj?"))
if temperatura > 25:
    print("Dia quente!")
elif temperatura > 15:
    print("Dia agradável!")  
else:
    print("Dia frio!") """


# 5 Tarefa


""" nota = int(input("Qual é a sua nota?"))
if nota > 8:
    print("Aprovado com nota boa")
elif nota >= 6:
    print("Na média")  
else:
    print("reprovado")  """


# 6 Tarefa


""" 
idade = int(input("Qual a sua idade?\n"))
inscricao = input("Você possui inscrição? (sim/não): ").strip().lower()

print(f"Idade: {idade}, Inscrição: {inscricao}")

if inscricao not in ("sim", "não", "nao"):
    print("Resposta inválida! Digite sim ou não.")

elif idade >= 14 and inscricao == "sim":
    print("Sua inscrição foi concedida!!")

else:
    print("Sua inscrição não foi realizada!")
 """



# 7 Tarefa


""" idade = int(input("Qual a sua idade?\n"))
preco = 20
print(f"sua idade é? \n{idade}")
if idade < 12 or idade > 60:
    print("Sua entrada para o museu é gratuita")
else:
    print(f"irá pagar R${preco}") """

# 8 Tarefa


""" quantidade = int(input("Qual é quantidade de livros \n"))
print(f"Você pegou {quantidade} livros!")
if quantidade <= 0:
    print(" O cadastro do(s) livros são invalidas")
elif quantidade > 4:
    print("a quantidade de livros, nao há exemplares suficientes")
else:
    print("O pedido foi confirmado") """



# 9 Tarefa


""" num = int(input("Qual é o seu numero? \n"))
num2 = int(input("Qual é o seu segundo numero? \n"))
print("Qual operação ira utilizar?\nsub = 1 \nadi = 2 \nmult = 3 \ndiv = 4")
operacao = int(input("Qual operação ira utilizar: "))
if operacao == 1:
  print(f"Resultado: {num - num2}")
elif operacao == 2:
  print(f"Resultado: {num + num2}")
elif operacao == 3:
  print(f"Resultado: {num * num2}")
elif operacao == 4:
  print(f"Resultado: {num / num2}")
else:
  print("Opção inválida!")
 """
# 10 Tarefa

""" idade = int(input("Idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao.lower() == "sim":
  print("Participação permitida.")
else:
  print("Participação não permitida.")
 """

  # 11 Tarefa Desafio


""" def executar_loja():
    nome = input("Digite seu nome: ")

    try:
        ouro = int(input("Quanto ouro você tem? "))
    except ValueError:
        print("Digite um número inteiro.")
        return

    if ouro < 0:
        print("Quantidade de ouro inválida.")
        return

    print("\n--- LOJA ---")
    print("1 - Poção de Vida (25 moedas)")
    print("2 - Escudo (60 moedas)")
    print("3 - Espada (100 moedas)")

    opcao = input("Escolha um item: ")

    itens = {
        "1": ("Poção de Vida", 25),
        "2": ("Escudo", 60),
        "3": ("Espada", 100)
    }

    if opcao not in itens:
        print("Item inválido.")
        return

    nome_item, preco = itens[opcao]

    if ouro >= preco:
        ouro -= preco
        print(f"{nome} comprou {nome_item}!")
        print(f"Ouro restante: {ouro}")
    else:
        print(f"Faltam {preco - ouro} moedas.")

executar_loja() """