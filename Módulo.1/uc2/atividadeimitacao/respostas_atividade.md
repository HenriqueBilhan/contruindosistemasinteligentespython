
Os dois arquivos Python estão incluídos nesta pasta:
- `01_cadastro_mensagem.py`
- `02_central_prioridades.py`
  
Porque a identificação serve como código para reconhecer a mensagem, e não para fazer cálculos. Por isso, pode ser armazenada como texto (`input()`).

Porque o tempo pode ter casas decimais, como 2.5 ou 5.0 minutos.

 
Aparece `Solicitar apoio: tempo insuficiente`, porque a condição que verifica se o tempo necessário é maior que o disponível vem antes da condição de risco imediato. Assim, a falta de tempo tem prioridade na regra da atividade.

Porque as condições do programa influenciam as decisões. Pessoas responsáveis precisam definir regras adequadas, avaliar consequências e evitar que uma simulação simplificada seja usada como se representasse todas as situações reais.



As previsões abaixo usam a lógica dos códigos fornecidos. A coluna “Saída obtida” deve ser preenchida após executar cada teste no computador; ela não é afirmada como uma execução real.



Usei o analista `Alex` e a identificação `MSG-007`.

| Grupos | Minutos por grupo | Resultado esperado | Saída obtida |
|---:|---:|---|---|
| 10 | 5.0 | Total 50 minutos; `Análise dentro do prazo` | Preencher após executar |
| 12 | 5.0 | Total 60 minutos; `Análise dentro do prazo` | Preencher após executar |
| 13 | 5.0 | Total 65 minutos; `Reorganizar o trabalho` | Preencher após executar |
| 0 | 5.0 | `Dados inválidos`; não calcula o total | Preencher após executar |
| 10 | -1.0 | `Dados inválidos`; não calcula o total | Preencher após executar |

 5 grupos e 2.5 minutos por grupo.  
se o programa aceita tempo decimal e calcula corretamente o total de 12.5 minutos, mostrando `Análise dentro do prazo`.



Usei a identificação `MSG-010`.

| Tempo disponível | Tempo necessário | Risco | Pista | Resultado esperado | Saída obtida |
|---:|---:|---|---|---|---|
| 60 | 60 | sim | sim | `Prioridade máxima`; restam 0 minutos | Preencher após executar |
| 60 | 61 | sim | sim | `Solicitar apoio: tempo insuficiente` | Preencher após executar |
| 60 | 30 | nao | sim | `Prioridade alta`; restam 30 minutos | Preencher após executar |
| 60 | 30 | nao | nao | `Prioridade normal`; restam 30 minutos | Preencher após executar |
| 60 | 30 | sim | nao | `Prioridade máxima`; restam 30 minutos | Preencher após executar |
| 0 | 30 | nao | nao | `Tempo inválido` | Preencher após executar |
| 60 | 30 | talvez | nao | `Resposta inválida` | Preencher após executar |
| -1 | 30 | talvez | nao | `Tempo inválido`, pois a validação dos tempos vem primeiro | Preencher após executar |

 tempo disponível 45, tempo necessário 45, risco `nao`, pista `nao`.  
 se o programa aceita uma análise que ocupa exatamente todo o tempo disponível e mostra `Prioridade normal`, com 0 minutos restantes.



O filme *O Jogo da Imitação* e os programas desta atividade mostram que resolver um problema exige organizar informações, definir regras e testar resultados. No meu código, uma condição importante é verificar se o tempo necessário é maior que o tempo disponível. Se for, o programa solicita apoio, mesmo que exista risco imediato, porque essa condição aparece primeiro. Os testes ajudam a descobrir se o programa está seguindo as regras definidas, inclusive nos limites, como quando os dois tempos são iguais. Um limite da simulação é que suas prioridades e seus valores foram criados para a atividade e não representam o funcionamento real da Enigma nem decisões de investigação do mundo real.
