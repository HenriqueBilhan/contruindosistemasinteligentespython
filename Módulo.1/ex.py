""" ---- O básico pro primata intender como funciona!! ----

1 print('hello world')

2 print(15 + 5)
"""
# Atividade 1
nome = 'Henrique'
idade= 17
cidade= 'São Leopoldo'
Tecnologia= 'Construindo Sistemas Inteligente Python'
print(nome, "\n",idade, "\n", cidade, "\n", Tecnologia)

# Atividade 2
produto= "Celular"
preco= 890
quantidadeemestoque= 4
disponivel= True

print(f" O produto é um {produto}, O preço é {preco}, A quantidade em estoque é {quantidadeemestoque}, {disponivel}")
 
# Atividade 3
jogador= "Henrique"
pontuacao= 250
vida= 150
acerto= 120
acerto1= 30
dano= 50
print (jogador, vida + acerto - dano + acerto1)

# Atividade 4
quantidadeproduto= 4
preco= 18.50 
print(f"Total do valor é quantidadeproduto * preco")

# Atividade 5
min= 60
horas= 7
print(f"{min * horas}minutos")

# Atividade 6
personagem= 'henrique'
vida= 200
dano1= 45
dano2= 30
regen= 20
print(f"personagem {personagem}, recebe 75 em um ataque {vida - dano1 + dano2} e recupera 20 de vida {vida + regen}")


# Atividade 7

salario = 2800
bonus= 450
print( salario + bonus)

# Atividade 8

largura= 90
altura= 30
print(largura * altura) 

# Atividade 9
titulo = 'python'
versao= 3
nota= 9.5
finalizado= False
print(titulo, versao, nota, type(finalizado))

# Atividade 10 
nome1 = 'henrique'
classe = 'predador'
nivel = 67
vida= 200
ataque= 100
defesa= 75
possui_magia= False

print(f"============================== \n Personagem \n ==================================    \n Nome: {nome1} \n Classe: {classe} \n Nivel: {nivel} \n Vida: {vida} \n ataque: {ataque} \n Defesa:{defesa}, Poder total:{ataque + defesa}, \n Possui magia:{type(possui_magia)}")

#Atividade Extra
nome = "Brás"
vida = 60
ouro = 300
nivel = 16

ouro += 50
vida -= 10
ouro -= 100
vida += 17
nivel += 4

print(f"===== EXTRA =====\nNome: {nome}\nVida: {vida}\nOuro: {ouro}\nNível: {nivel}")
