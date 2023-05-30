estoque = []


def ger_estoque():  #modulo GerEstoque

  # códigos de produtos válidos = soma dos digitos > 20
  def valida_cod(x):
    res = sum(int(i) for i in str(x))
    if res <= 20:
      return 0
    else:
      return 1

  #funcao que confirma a exclusao do item
  def confirma_excl(x, y):
    print('TEM CERTEZA QUE DESEJA EXCLUIR O ITEM?')
    resp = input('')
    if resp == 'sim':
      for i in range(len(y)):
        if y[i][0] == x:
          print(f'Item excluido {y[i]}')
          del (y[i])

  #funcao para deletar mais de um item
  def multi_del():
    multi = input('Deseja deletar mais itens? ')
    if multi == 'nao':
      return 1
    elif multi == 'sim':
      return 0
    else:
      multi_del()
      #recursividade parar permanecer na funcao ate receber uma resposta apropriada

  def natureza_estoque():
    print('Selecionar a opção desejada:', '\n Incluir itens (1)',
          '\n Excluir item (2)')

  #mensagem de conlusao da  operacao de exclusao do GerEstoque
  #x = lista do estoque limpo | y = lista do estoque bruto
  def conclu_excl(x, y):
    print(
      '---------------------------------------- \nRELATÓRIO DE ITENS EXCLUÍDOS \nITEM     SALDO'
    )
    for i in range(len(x)):
      print(x[i][0], "    ", y.count(x[i]))
    print(
      '----------------------------------------\nTeclar 0 para retornar à tela principal'
    )

  #mensagem de conclusao da operacao de exclusao
  # x = media_valor | y = maior_cod | z= maior
  def conclu_incl(x, y, z):
    print(
      f'----------------------------- \n Valor médio dos itens cadastrados: R$ {x} \n Item de maior valor cadastrado: código {y}, valor R$ {z} \n------------------------------\nTeclar 0 para retornar à tela principal'
    )

  natureza = int(
    input(
      'Selecionar a opção desejada: \n Incluir itens (1) \n Excluir itens (2)\n'
    ))

  if natureza == 1:
    N = float(input('Informe o número de itens que deseja adicionar: '))
    soma = 0
    maior = 0

    for i in range(int(N)):
      x = True
      while x == True:
        cod_item = int(input('Informe o codigo do item: '))

        if valida_cod(cod_item) == 0:
          print('Codigo invalido')

        else:
          #caso o codigo seja válido, cria uma lista, coleta a descricao do item, o valor unitario do item. Adiciona o codigo, a descricao e o valor do item na lista 'item' e esta lista no 'estoque'
          item = []
          desc_item = input('Informe a descrição do item: ')
          valor_item = float(input('Informe o valor do item: '))
          item.append(cod_item)
          item.append(desc_item)
          item.append(valor_item)
          estoque.append(item)
          x = False

          #compara o valor do item com a variavel maior para encontra o item de maior valor
          if valor_item > maior:
            maior = valor_item
            maior_cod = cod_item
          soma += valor_item

    media_valor = soma / N
    #---->           X      |     Y    |  Z
    conclu_incl(media_valor, maior_cod, maior)

  elif natureza == 2:
    #exemplo para testar!!
    #estoque = [[55555, 'bala', 0.4], [999, 'maça', 2], [888, 'melancia',30], [55555, 'bala', 0.4]]
    N = 0
    while N == 0:
      cod_excl = int(input('Informe o codigo do item a ser excluido: '))
      confirma_excl(cod_excl, estoque)
      N += multi_del()

    #cria um lista com os itens genericos do estoque
    estoque_limpo = []
    for i in estoque:
      if i not in estoque_limpo:
        estoque_limpo.append(i)

    conclu_excl(estoque_limpo, estoque)