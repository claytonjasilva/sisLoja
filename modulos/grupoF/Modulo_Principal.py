from GerCaixa import ger_caixa
from GerClientes import ger_clientes
from GerEstoque import ger_estoque


def sis_loja():
  print('\nSISTEMA DE GESTÃO DE LOJA \nDigite a opção desejada:\n1 - Gerenciador de Estoque \n2 - Gerenciador de Clientes \n3 - Gerenciador de Caixa \n')
  opcao = int(input('Informe a Opção: '))
  if opcao == 1:
    ger_estoque()
  elif opcao == 2:
    ger_clientes()
  elif opcao == 3:
    ger_caixa()
  else:
    print("\nOpção Inválida! \nTente Novamente!")
    sis_loja()


clientes = []
estoque = []
sis_loja()