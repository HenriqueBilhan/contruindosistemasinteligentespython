print("12 + 3")
print(12 + 3)
print("Resultado:", 12 + 3)
print("12", "3")



nome_oficina = "Robótica para iniciantes"
sala = "Laboratório 2"
quantidade_vagas = 24
duracao_horas = 2.5
inscricoes_abertas = True

print("Cadastro da oficina")
print("Nome:", nome_oficina)
print("Sala:", sala)
print("Quantidade de vagas:", quantidade_vagas)
print("Duração em horas:", duracao_horas)
print("Inscrições abertas:", inscricoes_abertas)

print(type(nome_oficina))
print(type(sala))
print(type(quantidade_vagas))
print(type(duracao_horas))
print(type(inscricoes_abertas))

preco_pizza = 48.00
preco_bebida = 12.00
quantidade_amigos = 4

total_conta = preco_pizza + preco_bebida
valor_por_pessoa = total_conta / quantidade_amigos

print("Total da conta: R$", total_conta)
print("Valor por pessoa: R$", valor_por_pessoa)
print("Tipo do valor por pessoa:", type(valor_por_pessoa))

livros_disponiveis = 40
print("Quantidade inicial:", livros_disponiveis)

livros_disponiveis = livros_disponiveis + 12
print("Após receber 12 livros:", livros_disponiveis)

livros_disponiveis = livros_disponiveis - 9
print("Após emprestar 9 livros:", livros_disponiveis)

livros_disponiveis = livros_disponiveis + 4
print("Após receber 4 devoluções:", livros_disponiveis)

livros_disponiveis = livros_disponiveis - 6
print("Após emprestar mais 6 livros:", livros_disponiveis)
 
nome_aluno = "Lucas"
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 9.5

soma_notas = nota_1 + nota_2 + nota_3
quantidade_atividades = 3
media = soma_notas / quantidade_atividades

print("Nome do aluno:", nome_aluno)
print("Nota 1:", nota_1)
print("Nota 2:", nota_2)
print("Nota 3:", nota_3)
print("Média:", media)


nome_curso = "Python básico"

mensalidade = 89.90


matricula_ativa = True

print("Curso:", nome_curso)


print("Mensalidade:", mensalidade)

print("Matrícula ativa:", matricula_ativa)
print("Tipo da mensalidade:", type(mensalidade))


saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)


saldo = saldo - 15

print("Saldo anterior após a despesa:", saldo_anterior)
print("Saldo atual após a despesa:", saldo)

quantidade_alunos = 20
custo_onibus = 600.00
preco_ingresso = 15.00
preco_lanche = 10.00

custo_ingressos = quantidade_alunos * preco_ingresso
custo_lanches = quantidade_alunos * preco_lanche
custo_total = custo_onibus + custo_ingressos + custo_lanches
valor_por_aluno = custo_total / quantidade_alunos

print("Quantidade de alunos:", quantidade_alunos)
print("Custo do ônibus: R$", custo_onibus)
print("Custo dos ingressos: R$", custo_ingressos)
print("Custo dos lanches: R$", custo_lanches)
print("Custo total: R$", custo_total)
print("Valor por aluno: R$", valor_por_aluno)


informacao = "42"
print("Valor:", informacao)
print("Tipo:", type(informacao))

informacao = 42
print("Valor:", informacao)
print("Tipo:", type(informacao))

informacao = 42.0
print("Valor:", informacao)
print("Tipo:", type(informacao))

informacao = False
print("Valor:", informacao)
print("Tipo:", type(informacao))



nome_robo = "Atlas"
energia = 100
distancia_percorrida = 0
amostras_coletadas = 0
missao_em_andamento = True

print("=== Estado inicial ===")
print("Nome:", nome_robo)
print("Energia:", energia)
print("Distância:", distancia_percorrida, "metros")
print("Amostras:", amostras_coletadas)
print("Missão em andamento:", missao_em_andamento)

distancia_percorrida = distancia_percorrida + 120
energia = energia - 20
print("Etapa 1: percorreu 120 metros. Energia:", energia)

amostras_coletadas = amostras_coletadas + 3
energia = energia - 15
print("Etapa 2: coletou 3 amostras. Energia:", energia)

energia = energia + 10
print("Etapa 3: recarregou energia. Energia:", energia)

distancia_percorrida = distancia_percorrida + 80
energia = energia - 25
print("Etapa 4: percorreu mais 80 metros. Energia:", energia)

amostras_coletadas = amostras_coletadas + 2
energia = energia - 10
print("Etapa 5: coletou mais 2 amostras. Energia:", energia)

missao_em_andamento = False
print("Etapa 6: missão encerrada.")

duracao_minutos = 4
distancia_media_por_minuto = distancia_percorrida / duracao_minutos

print("=== Relatório final ===")
print("Nome:", nome_robo)
print("Energia final:", energia)
print("Distância percorrida:", distancia_percorrida, "metros")
print("Amostras coletadas:", amostras_coletadas)
print("Missão em andamento:", missao_em_andamento)
print("Distância média:", distancia_media_por_minuto, "metros por minuto")
