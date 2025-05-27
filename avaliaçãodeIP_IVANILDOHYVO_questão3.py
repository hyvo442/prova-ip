# PROVA – Introdução à Programação (BIA)
#**Nome completo:** Ivanildo Hyvo Silva Santos
#**Matrícula:** 2022129520039
#**E-mail institucional:** ivanildohyvo@discente.ufg.br

## QUESTÃO 3
## importação das bibliotecas usadas no programa
import random
import numpy as np
import pandas as pd
#geração dos dados que vão ser utilizados no programa usando o random dentro de um loop que vai gerar 30 valores entra 13 e 30, cada um sendo armazenado dentro de uma lista chamada_lista_do_mes
#geração de 30 numero do 1 ao 30 que são guardados na lista lista_dias pra ser usado mais tarde
lista_do_mes=[]
lista_dias=[]
dia=1
for a in range(0,30):
    temperatura=random.randint(13,30)
    lista_do_mes.append(temperatura)
    lista_dias.append(dia)
    dia+=1

###A-Utilização do numpy para calcular:a média das temperaturasa, mediana ,o desvio padrão e o indice de variação termica do mes

media_do_mes=np.mean(lista_do_mes)
desvio_padrao=np.std(lista_do_mes)
mediana = np.median(lista_do_mes)
indice_variação = desvio_padrao / media_do_mes
###B-Criação deum DataFrame do Pandas com dados:Dia do mês (1 a 30),Temperatura média do dia,E uma coluna chamada "Diferença para a média"
#é preciso calcular a  diferença entre a temperatura do dia e a média mensal pra poder criar a coluna "Diferença para a média".
#para isso usei um lopping que vai pegar cada elemento da lista 'lista_do_mes' que contem as temperutas de cada dia e subtrair desses elementos a media do mes.
#logo em seguida salvando esses valores em outra lista chamada 'diferença_para_a_média'
diferença_para_a_média=[]
for b in lista_do_mes:
  diferença=b-media_do_mes
  diferença_para_a_média.append(diferença)
#criação do date frame com as listas
data = {
    'dia do mês': lista_dias,
    'temperatura media do dia': lista_do_mes,
    'Diferença para a média': diferença_para_a_média
}
df = pd.DataFrame(data)
###C)Criação de  uma nova coluna no DataFrame chamada "Classificação térmica", com base nos seguintes critérios:
#“Frio”: temperatura < 18°C
#“Agradável”: 18°C ≤ temperatura ≤ 25°C
#“Quente”: temperatura > 25°C
#para isso usei um lopping que vai pegar cada elemento da lista 'lista_do_mes' que contem as temperutas de cada dia e colocar rotulos os rotulos frio ou agravel ou quente em cada um deles
#e em seguida salvando os rotulos em uma lista chamada 'Classificação_térmica'
###d)Contagem do número total de dias classificados como: “Frio” “Agradável” “Quente”
#para isso utilizo os mesmo lopping pra salvar eles em uma variavel que conta um por um 

Classificação_térmica=[]
frio=0
quente=0
agradavel=0
for c in lista_do_mes:
  if c < 18:
    Classificação_térmica.append('Frio')
    frio+=1
  if 18<=c<=25:
    Classificação_térmica.append('Agradavel')
    agradavel+=1
  if c > 25:
    Classificação_térmica.append('Quente')
    quente+=1
data = {
    'dia': lista_dias,
    'temperatura': lista_do_mes,
    'Diferença para a média': diferença_para_a_média,
    'Classificação termica': Classificação_térmica
}

df = pd.DataFrame(data)
print(df)
print(f"{frio} dia(s) foram frios, {agradavel} dia(s) foram agradaveis, {quente} dia(s) foram quentes")
#Analise dos 5 dias mais quentes e os 5 dias mais frios, com base na temperatura média.
# para isso Criei uma  lista de dicionários com dia e temperatura de cada elemento da lista 'lista_do_mes' que contem as temperutas de cada dia
valores = [{"pos": i+1, "valor": v} for i, v in enumerate(lista_do_mes)]
# Ordenar a lista de dicionários pelo valor
valores_ordenados = sorted(valores, key=lambda x: x["valor"])
# 5 menores
menores = valores_ordenados[:5]
# 5 maiores (inverter para mostrar do maior ao menor)
maiores = valores_ordenados[-5:][::-1]
# Exibir resultados
print("os 5 dias mais quentes foram:")
for item in maiores:
    print(f"temperatura: {item['valor']}, dia: {item['pos']} ", end='temperatura ')
# nesses 10 dias, cruzei a classificação térmica com a diferença para a média, indicando se o dia ficou:Acima da média mensalAbaixo da média mensalExatamente na média
    if item['valor']<media_do_mes:
      print('abaixo da média mensal')
    if  item['valor']>media_do_mes:
      print('acima da média mensal')
    if item['valor']==media_do_mes:
      print('exatamente na média')
print("\nos 5 dias mais frios foram:")
for item in menores:
    print(f"temperatura: {item['valor']}, dia: {item['pos']} ", end='temperatura ')
#nessa parte faço o mesmo indicando se o dia ficou:Acima da média mensalAbaixo da média mensalExatamente na média
    if item['valor']<media_do_mes:
      print('abaixo da média mensal')
    if  item['valor']>media_do_mes:
      print('acima da média mensal')
    if item['valor']==media_do_mes:
      print('exatamente na média')

print(f'a media do mes foi {media_do_mes}')
#Houve dias classificados como “Frio” que estavam acima da média do mês? não teve
#Houve dias classificados como “Quente” que estavam abaixo da média? não teve