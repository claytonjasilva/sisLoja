import os  # Apaga o que foi escrito anteriormente
import gerestoque  # importa as funçoes
import gercliente  # importa as funçoes
import gercaixa

vendas = []
codigos = []
listaEstoque = []  # inicializa a lista do estoque vazia
listacpf = []
listaClientes = []
cpf = ""


def menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("------------------------------")
  print("SISTEMA DE GESTAO DE LOJA (SISLOJA)")
  print("Selecionar a opção desejada:")
  print("Gestão de estoque (1)")
  print("Gestão de clientes (2)")
  print("Gestão de fluxo de caixa (3)")
  print("------------------------------")


def sisloja():
  while True:
    menu()
    opcao = int(input("O que deseja fazer? "))

    if opcao == 1:
      gerestoque.menu_estoque(listaEstoque)
    elif opcao == 2:
      gercliente.menu_cliente()
    elif opcao == 3:
      gercaixa.menu_caixa()
    else:
      print("Ação inválida. Tente novamente.")


sisloja()

#Alex Euzebio (202301134358) TA
#Emily Fernandes (202303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA
