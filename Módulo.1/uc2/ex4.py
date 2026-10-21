# 1 Atividade
""" 
vaga = int(input("Digite o tempo que ira ficar na Vaga:"))
print(vaga)
if vaga >= 2 or vaga > 1:
    print("Ira pagar 10 real tua vaga bobão")
elif vaga >= 5:
    print("quer posar aqui tambem?, vai pagar 20 pilinha")
else:
    print("visitinha de médico")
 """
#  2 Atividade
""" nivel = int(input("Qual é o seu nível:"))
print(nivel)
if nivel <= 5:
        print("Aprendiz")
elif nivel > 6 or nivel <= 15:
        print("Guerreiro")
elif nivel > 16 or nivel <= 30:
        print("veterano")
elif nivel > 31:
        print("Superior")
else:
        print("Minoria")
 """

# 3 Atividade

""" 
usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado!")

 """
# 4 Atividade
""" 
salario = 2000
emprestimo = 10
parcela = 30

preco = int(input("Qual é o seu salario? minimo R$2000 para o emprestimo"))
print(preco)
if preco == salario:
    print("atende o requisito de emprestimo")
else:
    print("nao atende o requisito do emprestimo")
    preco2 = preco * emprestimo
    print(preco2)
     """
# 5 Atividade


""" nome = input("Nome do personagem: ")
vida = int(input("Vida atual: "))
ataque = int(input("Pontos de ataque: "))
vida_inimigo = int(input("Vida do inimigo: "))
defesa = int(input("Pontos de defesa do inimigo: "))

dano = ataque - defesa

if vida <= 0:
    print(f"{nome} não pode atacar, pois está sem vida!")

elif dano <= 0:
    print("O ataque não causou dano!")

elif dano >= vida_inimigo:
    vida_restante = max(0, vida_inimigo - dano)
    print("Inimigo derrotado!")
    print(f"Vida restante do inimigo: {vida_restante}")

else:
    vida_restante = max(0, vida_inimigo - dano)
    print("O inimigo sobreviveu!")
    print(f"Vida restante do inimigo: {vida_restante}")
 """
# 6 Atividade
""" idade = float(input("Qual sua idade?"))
print(idade)
matricula = (input("você esta matriculado (sim/nao)"))
print(matricula)
autorizacao = (input("voce tem autorização do professor? (sim/nao)"))
print(autorizacao)
laboratorio = (input("O laboratorio esta disponivel? (true/false)"))
print(laboratorio)
if idade >= 16 and matricula  == "sim" and autorizacao == "true":
    print("voce está autorizado a entrar")
elif idade < 16:
    print("nao pode entrar llllloser")
else:
    print("tu acha ainda que vai entrar? burrAO")
    
 """
# 7 Atividade
""" valor_compra = int(input("Qual o valor vai dar da compra?"))
frete = int(input("qual regiao você mora (sul/sudeste/centro/norte)"))
if frete == 1:
    print(f"Valor do frete incluso: {valor_compra + 15}")
elif frete == 2:
    print(f"Valor do frete incluso: {valor_compra + 20}")
elif frete == 3:
    print(f"Valor do frete incluso: {valor_compra + 25}")
elif frete == 4:
    print(f"Valor do frete incluso: {valor_compra + 35}")
else: 
    print("Regiao invalida, Cade a porra da esquerda cidadão")
 """
# 8 Atividade

""" a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# Primeiro: validar o triângulo
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    
    # Depois: classificar
    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

else:
    print("Triângulo inválido")
 """