# PROVA – Introdução à Programação (BIA)
#**Nome completo:** Ivanildo Hyvo Silva Santos
#**Matrícula:** 2022129520039
#**E-mail institucional:** ivanildohyvo@discente.ufg.br

## QUESTÃO 1

###a) criei as variaveis potencia e tempo que o usuario ira preenher pra saber o consumo mensal em KWh
potencia=float(input("qual a potêcia em kw dos aparelhos?"))
tempo=float(input("quantas horas por dia em media é usado os aparelhos?"))

###b)Garantindo que ambos os valores inseridos sejam positivos e realistas. Caso contrário, vai exibir uma mensagem de erro compatível com os exemplos.
##Se  o usuario digitar uma potencia menor que 0 (que é impossivel), ou digitar uma potencia maior que 4 (que é o nosso valor maximo do codigo),o usuario passara por um laço de repetição até digitar um valor usual

if potencia<0 :
  print("erro, potência negativa")
  while True:
    potencia=float(input("digite novamente o valor da potencia"))
    if potencia<0:
      print("erro, potência negativa")
    if potencia>4:
      print('erro, potência muito alta')
    if 0<potencia<=4:
      break

# 
if potencia>4:
  print('erro, potência muito alta')
  while True:
    potencia=float(input("digite novamente o valor da potencia"))
    if potencia<0:
      print("erro, potência negativa")
    if potencia>4:
      print('erro, potência muito alta')
    if 0<potencia<=4:
      break
##Se o usuario digitar uma tempo menor que 0 (que é impossivel), ou digitar um tempo maior que 6 (que é o nosso valor maximo do codigo),o usuario passara por um laço de repetição até digitar um valor usual
if tempo<0 :
  print("erro, tempo negativo")
  while True:
    tempo=float(input("digite novamente as horas"))
    if tempo<0:
      print("erro, tempo negativo")
    if tempo>6:
      print('erro, tempo muito alto')
    if 0<tempo<6:
      break

if tempo>6:
  print('erro, tempo muito alto')
  while True:
    tempo=float(input("digite novamente as horas"))
    if tempo<0:
      print("erro, tempo negativo")
    if tempo>6:
      print('erro, tempo muito alto')
    if 0<tempo<6:
      break

###c) função que vai calcular o consumo mensal do usuario baseado na formula :Consumo mensal (kWh)=Potência (kW)×Horas por dia×30
def calcular_consumo_mensal(pot, horas):
  return pot*horas*30

###d)Apresentanção dos dados de forma clara para o usuário.
print(f'potência: {potencia}')
print(f'horas por dia: {tempo}')
print(f'consumo mensal(KWh): {calcular_consumo_mensal(potencia,tempo)}')