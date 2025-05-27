# PROVA – Introdução à Programação (BIA)
#**Nome completo:** Ivanildo Hyvo Silva Santos
#**Matrícula:** 2022129520039
#**E-mail institucional:** ivanildohyvo@discente.ufg.br

## QUESTÃO 2
### a-O programa inicia solicitando do usuário um conjunto de categorias e seus gastos mensais por categoria que são salvos em um dicionario e dps cada dicionario é mandado para lista.
#Se o usuario digitar o gasto da categoria errado ele tera que escrever de novo a categoria e se responder diferente de 's' ou 'n' para continuar, a pergunta será feita novamente
categorias = []
print("Digite um conjunto de metas de gastos mensais por categoria:")
while True:
  nome = input("Nome da categoria: ")
  try:
    orcamento = float(input("Orçamento da categoria: "))
  except ValueError:
    print("Valor inválido. Use números.")
    continue
  categorias.append({'nome': nome, 'orcamento': orcamento, 'lancamentos': []})
  continuar = input("Deseja adicionar outra categoria? [s/n]: ").lower()
  while continuar not in ('s', 'n'):
      continuar = input("Digite apenas 's' ou 'n': ").lower()
  if continuar == 'n':
      break
### b-o usuario estara dentro de um lopping e só saira quando responder a pergunta do numero de lançamentos comm um numero inteiro 
while True:
  try:
      numero_lançamentos = int(input("Número total de lançamentos: "))
  except ValueError:
    print("Valor inválido.")
    continue
  break
###c)O usuario tera que escrever o nome do lançamento o seu valor e a qual o numero da  categoria o lançamento pertence(pra ajudar o usuário com isso é mostrado o numero das categorias)
#isso vai durar equivalente ao numero de lançamentos que o usuario digitou
for a in range(0,numero_lançamentos):
  nome = input(f"Nome do lançamento {a+1}: ")
  valor = int(input(f"Valor do lançamento {a+1}: "))
  print("Categorias disponíveis:")
  for categoria,oçamento in enumerate(categorias, 1):
    print(f"{categoria}. {oçamento['nome']} (Orçamento: {oçamento['orcamento']})")
  categoria_correspondente=int(input("qual o numero da categoria correspondente ao lançamento?"))
  categorias[ categoria_correspondente - 1]['lancamentos'].append({'nome': nome, 'valor': valor})
###d-Nessa parte sera feito os calculos da:  total da despesa da categoria, a media de gasto da categoria, a despesa mensal das categorias 
#E uma análise comparativa entre o valor gasto dentro da categoria e o orçamento da categoria inseridas pelo usuário
#logica aplicada para referencia:
#total da despesa da categoria= soma do valor dos lançamentos de cada categoria
#media de gasto da categoria= total da despesa da categoria / nº de lançamentos da categoria
#despesa mensal das categorias = soma do total da despesa de todas as categoria
total_mensal = 0
categoria_maior_gasto = ''
maior_valor = 0

for b in categorias:
    print(f"Categoria: {b['nome']}")
    print(f"Orçamento: R$ {b['orcamento']}")
    print("Lançamentos:")
        
    total_da_despesa_categoria = 0
    for c in b['lancamentos']:
        print(f"- {c['nome']}: R$ {c['valor']}")
        total_da_despesa_categoria += c['valor']

    media_da_categoria =  total_da_despesa_categoria / len(b['lancamentos']) if b['lancamentos'] else 0
    resto = b['orcamento'] - total_da_despesa_categoria
    total_mensal +=  total_da_despesa_categoria

    print(f"Total gasto: R$ { total_da_despesa_categoria}")
    print(f"Média de gastos: R$ {media_da_categoria}")
    print(f"Restante do orçamento: R$ {resto}")

    if total_da_despesa_categoria > maior_valor:
        maior_valor = total_da_despesa_categoria
        categoria_maior_gasto = b['nome']

print(f"Despesa mensal total: R$ {total_mensal}")
print(f"Categoria com maior gasto foi :{categoria_maior_gasto} com uma despesa de  R$ {maior_valor}")