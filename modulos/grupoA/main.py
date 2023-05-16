import os  # Apaga o que foi escrito anteriormente
import gerestoque  # importa as funçoes
import gercliente  # importa as funçoes
import gercaixa

listaEstoque = []  # inicializa a lista do estoque vazia
listacpf = []
cpf = ""

def menu():
  #menu principal do sisloja
  os.system('cls' if os.name == 'nt' else 'clear')  # limpa o console
  print("------------------------------\n")
  print("SISTEMA DE GESTAO DE LOJA (SISLOJA)\n")
  print("Escolha a opção desejada: \n")
  print("Gestão de estoque (1) \n")
  print("Gestao de clientes (2) \n")
  print("Gestão de fluxo de caixa (3) \n")
  print("------------------------------\n")

def sisloja():
  #Separa as funçoes de acordo com o que o cliente decidir
  while True:
    menu()
    Gestao = int(input("O que deseja fazer? "))

    if Gestao == 1:
      gerestoque.menu_estoque(listaEstoque)  # Realiza os comandos da funçao
    elif Gestao == 2:
      gercliente.cadastrar_cliente()  #Realiza os comandos da funçao
    elif Gestao == 3:
      gercaixa.menu_caixa()  #Realiza os comandos da funçao
    else:
      print("Ação inválida. Tente novamente.\n")
      print("------------------------------\n")
      return

sisloja()

#Alex Euzebio (202301134358) TA
#Emily Fernandes (202303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA