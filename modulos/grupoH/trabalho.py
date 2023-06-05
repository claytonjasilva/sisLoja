#Ger_Estoque: Thiago e Breno
#Thiago: TA
#Breno: TA
while True:
    print('-'*40)
    print('SISTEMA DE GESTÃO DE LOJA (SisLoja)')
    print('Selecione a opção desejada:  ') 
    print('Gestão de estoque (1)')
    print('Gestão de clientes (2)')
    print('Gestão de fluxo de caixa (3)')
    direcao = int(input('-'*40))

    match direcao:
      case 1:
        lista_estoque = []
        lista_estoque_valores = []
        lista_estoque_codigos = []
        escolha = None
        qtd = 0
        cod_item = 0
        desc_item = None
        valor_item = 0
        item = None
        media_valores_cadastrados = 0
        cod_item_maior_valor = 0
        valor_item_mais_valioso = 0
        contador = 0
        soma_valores = 0
        soma_dig_cod = 0
        indice = 0
        escolha_2 = None
        certeza = None

        def saldo(codigo , lista):
          retorno = 0
        for i in lista:
          if codigo == i:
            retorno += 1
    return retorno


# loop infinito inicialização
while True:
  print('Bem vindo ao Estoque do sistema SisLoja')
  escolha = input(
    'Você deseja incluir ou excluir algum item do estoque ? : ').lower()
  if escolha == 'incluir':
    qtd = int(input('Quantos itens você deseja incluir no estoque: '))
    if qtd == 0:
      continue

    elif qtd == 1:
      item = input('Escreva o item: ')
      cod_item = int(input('Digite o código do item: '))
      des_item = input('Inclua uma descrição do item: ')
      valor_item = float(input('Digite o valor do item: '))
      lista_estoque.append(item)
      lista_estoque_valores.append(valor_item)
      lista_estoque_codigos.append(cod_item)
      print('-' * 40)
      for count in lista_estoque:
        contador += 1
      for valor in lista_estoque_valores:
        soma_valores += valor
      if valor_item > valor_item_mais_valioso:
        valor_item_mais_valioso = valor_item
        cod_item_maior_valor = cod_item
      media_valores_cadastrados = round(soma_valores / contador, 2)
      print(
        f'Valor médio dos itens cadastrados: R$ {media_valores_cadastrados}')
      print(
        f'Item de maior valor cadastrado: {cod_item_maior_valor} , valor R$ {valor_item_mais_valioso}'
      )
      print('-' * 40)
      if input('Tecle 0 para retornar à tela principal') == 0:
        continue

    else:
      for i in range(1, qtd + 1):
        item = input(f'Digite o item {i}: ')
        cod_item = int(input(f'Digite o código do item {i}: '))
        des_item = input(f'Inclua uma descrição do item {i}: ')
        valor_item = float(input(f'Digite o valor do item {i}: '))
        lista_estoque.append(item)
        lista_estoque_valores.append(valor_item)
        lista_estoque_codigos.append(cod_item)
        if valor_item > valor_item_mais_valioso:
          valor_item_mais_valioso = valor_item
          cod_item_maior_valor = cod_item
      print('-' * 40)
      for count in lista_estoque:
        contador += 1
      for valor in lista_estoque_valores:
        soma_valores += valor
      media_valores_cadastrados = round(soma_valores / contador, 2)
      print(
        f'Valor médio dos itens cadastrados: R$ {media_valores_cadastrados}')
      print(
        f'Item de maior valor cadastrado: código =  {cod_item_maior_valor} , valor R$ {valor_item_mais_valioso}'
      )
      print('-' * 40)
      if input('Tecle 0 para retornar à tela principal:   ') == 0:
        continue
  elif escolha == 'excluir':
    while True:
      cod_item = input(
        'Digite o código do item que deseja excluir do estoque:  ')
      soma_dig_cod = 0
      for dig in cod_item:
        dig = int(dig)
        soma_dig_cod += dig
      cod_item = int(cod_item)
      certeza = input('TEM CERTEZA QUE DESEJA EXCLUIR O ITEM ?   ').lower()
      if certeza == 'sim':
        if soma_dig_cod > 30 and soma_dig_cod < 100:
          if cod_item in lista_estoque_codigos:
              lista_estoque_codigos.remove(cod_item)
              for i in lista_estoque_codigos:
                indice = 0
                if cod_item == i:
                  item = lista_estoque.pop(indice)
                indice += 1
              saldo_exclusao = saldo(cod_item , lista_estoque_codigos)
              print('OPERAÇÃO REALIZADA COM SUCESSO')
          escolha_2 = input(
            'Você deseja excluir mais algum item da lista ?  ').lower()
          if escolha_2 == 'sim':
            continue
          elif escolha_2 == 'nao':
            print('-' * 40)
            print('RELÁTORIO DE ITENS EXCLUÍDOS ')
            print('  ITEM              SALDO')
            print(f'{item}            {saldo_exclusao} ')
            print('-' * 40)
            if input('Tecle 0 para retornar à tela principal:   ') == 0:
              continue
            

        else:
          print('CÓDIGO INVÁLIDO')
          break

      elif certeza == 'nao':
        break
  else:
    print('Digite uma escolha válida')
#Ger_Cliente: Lua e Vitor
#Lua: TA
#Vitor: TA
case 2:
        def get_clientes():
    listaClientes = []
    cpf = ""
    while cpf != "0":
        cpf = input("Digite o CPF do cliente (ou 0 para encerrar): ")
        if cpf == "0":
            break
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido!")
            continue
        renda_cliente = float(input("Digite a renda do cliente: "))
        listaClientes.append({"cpf": cpf, "renda": renda_cliente})

    total_clientes = len(listaClientes)
    renda_acima_10k = len([cliente for cliente in listaClientes if cliente["renda"] > 10000])
    renda_entre_5k_e_10k = len([cliente for cliente in listaClientes if 5000 <= cliente["renda"] <= 10000])
    renda_abaixo_5k = len([cliente for cliente in listaClientes if cliente["renda"] < 5000])

    print("OPERAÇÃO REALIZADA COM SUCESSO")
    print(f"Total de clientes cadastrados: {total_clientes}")
    print(f"Percentual de clientes com renda acima de R$ 10.000,00: {(renda_acima_10k/total_clientes)*100:.2f}%")
    print(f"Percentual de clientes com renda entre R$ 5.000,00 e R$ 10.000,00: {(renda_entre_5k_e_10k/total_clientes)*100:.2f}%")
    print(f"Percentual de clientes com renda abaixo de R$ 5.000,00: {(renda_abaixo_5k/total_clientes)*100:.2f}%")

    return listaClientes

clientes = get_clientes()
print("Lista de clientes cadastrados:")
for cliente in clientes:
    print(f"CPF: {cliente['cpf']}, Renda: R$ {cliente['renda']:.2f}")
#Ger_Caixa: Fabiano e Pedro
#Fabiano: TA
#Pedro: TA
      case 3:
        print('Bem vindo ao GerCaixa')
data = input('Digite a data:  ')
saldo_inicial = float(input('Digite o saldo inicial do dia:  '))
n = int(input('Digite o número total de vendas realizadas:  '))
lista_valores = []
lista_totais_vendas = []
lista_qtd_itens = []
o=0
n=o

def media(arg1 , arg2):
    m = round(arg1 / arg2, 2)
    return m


def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    round(soma , 2)
    return soma


def saldo_final(saldo1, saldo2):
    saldo_total = round(saldo1 + saldo2 , 2)
    return saldo_total

if n == 0:
    pass

elif n == 1:
    cpf = input('Digite o CPF do cliente:  ')
    quant_item = int(input('Digite a quantidade de itens que o cliente comprou:   '))
    lista_qtd_itens.append(quant_item)
    count = 1
    while quant_item > 0:
        valor_un = float(input(f'Digite o valor do item {count} que o cliente comprou:   '))
        lista_valores.append(valor_un)
        cod_item = int(input(f'Digite o código do item {count} que o cliente comprou:   '))
        quant_item -= 1
        count += 1
    tot_venda = soma_lista(lista_valores)
else:
    count_2 = 1
    while n > 0:
         cpf = input(f'Digite o CPF do cliente {count_2}:  ')
         quant_item = int(input(f'Digite a quantidade de itens que o cliente comprou {count_2}:'))
         lista_qtd_itens.append(quant_item)
         count_2 += 1
         count_3 = 1
         while quant_item > 0:
          valor_un = float(input(f'Digite o valor do item {count_3} que o cliente comprou:   '))
          lista_valores.append(valor_un)
          cod_item = int(input(f'Digite o código do item {count_3} que o cliente comprou:   '))
          quant_item -= 1
          count_3 += 1
          n -= 1
        tot_venda = soma_lista(lista_valores)


   
print('-'*40)
print('RELATÓRIO DE VENDAS')
print(f'Data da movimentação:  {data}')
print(f'Saldo: {saldo_final(saldo_inicial , tot_venda)}')
print(f'Valor médio das vendas: {media(tot_venda , o)}')
print(f'Total das vendas: {soma_lista(lista_qtd_itens)}')
print('-'*40)
if input('Tecle 0 para retornar à tela principal:   ') == 0:
    continue
      case other:
        print('Por favor digite uma opção válida')
