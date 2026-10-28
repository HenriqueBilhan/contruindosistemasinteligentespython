
identificacao = input("Identificação da mensagem: ")
tempo_disponivel = float(input("Tempo disponível (minutos): "))
tempo_necessario = float(input("Tempo necessário (minutos): "))
risco = input("A mensagem indica risco imediato? (sim/nao): ")
pista = input("A mensagem contém uma pista recorrente? (sim/nao): ")

if tempo_disponivel <= 0 or tempo_necessario <= 0:
    print("Tempo inválido")
elif (risco != "sim" and risco != "nao") or (pista != "sim" and pista != "nao"):
    print("Resposta inválida")
else:
    print("Identificação:", identificacao)

    if tempo_necessario > tempo_disponivel:
        print("Solicitar apoio: tempo insuficiente")
    elif risco == "sim":
        print("Prioridade máxima")
        print("Tempo restante:", tempo_disponivel - tempo_necessario, "minutos")
    elif pista == "sim":
        print("Prioridade alta")
        print("Tempo restante:", tempo_disponivel - tempo_necessario, "minutos")
    else:
        print("Prioridade normal")
        print("Tempo restante:", tempo_disponivel - tempo_necessario, "minutos")
