import datetime  # biblioteca para formatar as datas
import re  # biblioteca para formatar datas
import os  #Apaga o que foi escrito anteriormente deixando o console
from gercliente import *

def Data():
  #Formata a data sempre que necessario
  data_input = input("Digite a data: ")

  # Verifica se a entrada é uma string numérica de 8 dígitos
  if not re.match(r'^\d{8}$', data_input):
    print("Data inválida")
    Data()
  else:
    # Converte a string de entrada em um objeto datetime
    try:
      data = datetime.datetime.strptime(data_input, '%d%m%Y')
    except ValueError:
      print("Data inválida")
      Data()
    else:
      # Formata a data para o formato desejado
      global data_formatada
      data_formatada = data.strftime('%d/%m/%Y')

def menu_caixa ():
  os.system('cls' if os.name == 'nt' else 'clear')  #limpa o console
  global saldoCaixa
  saldoCaixa = 0
  num_item = 0
  print("-----------------------------\n")
  print("GERENCIAMENTO DE CAIXA\n")
  Data()
  saldo_inicial = float(input("Digite o saldo inicial do caixa: ")) #Pergunta o saldo inicial do caixa
  N = int(input("Digite o numero de vendas total do dia: ")) #Pergunta o total de vendas do dia 
  print("\n-----------------------------\n")
  tot_venda = 0
  som_item = 0
  for i in range(1, N + 1):
    cpf = input("Digite o CPF do cliente: ")
    while not validar_cpf(cpf):
      print("CPF inválido!")
      cpf = input("Digite o CPF do cliente: ")
    cod_item = int(input("\nDigite o codigo do item: ")) #Pergunta o codigo do item
    #verifica se o codigo é valido
    while cod_item > 100 or cod_item < 30:
      print ("CODIGO INVALIDO")
      cod_item = int(input("Código do item: "))
    print ("CODIGO VALIDO")
    #Pergunta as demais informaçoes necessarias
    quant_item = int(input("Digite a quantidade de itens: "))
    valor_un = float(input("Valor unitario do item em reais: "))
    tot_venda = (quant_item * valor_un) + tot_venda
    som_item = quant_item + som_item
    num_item = quant_item + num_item
    
  #chama do main a data que acabamos de formatar
  
  print("\n-----------------------------\n")
  print("RELATORIO DE VENDAS")
  print("Data da movimentaçao:", data_formatada)
  print("Saldo: R$", saldo_inicial + tot_venda)
  print("Media de valor dos produtos vendidos: R$", tot_venda / som_item)
  print("Total de vendas:", num_item , "unidades\n")
  print("-----------------------------\n")

  #voltar para o menu
  voltar = int(input("Teclar 0 para retornar à tela principal "))
  if (voltar != 0):
    print("Ação inválida")
    voltar = int(input("tecle 0 para voltar ao menu principal"))
  else:
    from main import sisloja

#Alex Euzebio (202301134358) TA
#Emily Fernandes (@02303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA