
analista = input("Nome ou apelido do analista: ")
identificacao = input("Identificação da mensagem (ex.: MSG-007): ")
grupos = int(input("Quantidade de grupos de símbolos: "))
tempo_por_grupo = float(input("Tempo para analisar cada grupo (minutos): "))

if grupos <= 0 or tempo_por_grupo <= 0:
    print("Dados inválidos")
else:
 
    tempo_total = grupos * tempo_por_grupo

    print("\n--- Ficha da mensagem ---")
    print("Analista:", analista)
    print("Identificação:", identificacao)
    print("Quantidade de grupos:", grupos)
    print("Tempo total estimado:", tempo_total, "minutos")


    if tempo_total <= 60:
        print("Análise dentro do prazo")
    else:
        print("Reorganizar o trabalho")
