def ger_caixa():  # modulo GerCaixa

  #resumo do total do cliente
  # x = codigo do cliente | y = valor gasto
  def relatorio_cliente(x, y):
    print('------------------------------------------')
    print(f'Cliente {x} Total de vendas: R$ {y}')
    print('------------------------------------------')

  #valida o codigo do cliente(cpf)
  def checaCpf(x):
    #checa o tamanho do cpf
    if len(str(x)) != 11:
      return 0
    #valida o cpf
    res = sum(int(i) for i in str(x))
    if (res % 11) == 0:
      return 1
    else:
      return 0

  #valida o codigo do produto
  def valida_cod(x):
    res = sum(int(i) for i in str(x))
    if res <= 20:
      return 0
    else:
      return 1

  #  relatório do caixa com
  # x = data | y = Saldo | z = valor médio
  # k = unidades vendidas | w = codigo do cliente que mais gastou
  def relatorio_caixa(x, y, z, k, w):
    print('---------------------------')
    print('RELATÓRIO DE VENDAS')
    print(f'Data da movimentação: {x}')
    print(f'Saldo: R$ {y}')
    print(f'Valor médio das vendas: R$ {z}')
    print(f'Total das vendas: {k} unidades')
    print(f'Cliente de maior consumo: código {w}')
    print('---------------------------')
    print('Teclar 0 para retornar à tela principal')

  data = input('Insira a Data(dd/mm/aa): ')
  saldo_inicial = float(input('Informe o saldo inicial do dia: '))
  N = int(input('Informe o número de vendas do dia: '))
  vendas_tot = N
  tot_saldo = 0
  maior = 0
  unidades = 0
  maior_cliente = 0

  while N != 0:
    cpf = int(input('Informe o codigo do cliente: '))
    tot_cliente = 0

    if checaCpf(cpf) == 1:  #so decrementa o contador quando cod é verdadeiro
      n_compras = int(
        input('Informe o número de compras desse cliente no dia: '))
      if N - n_compras >= 0:
        N -= n_compras
        for compra in range(n_compras):

          #A variavel n_itens_compra representa o número de itens genericos comprados, exemplo, em uma lista com banana, maça e pera o n_itens_compra é 3, em uma lista com banana, maça, banana o n_itens_compra é 2
          n_itens_compra = int(
            input('Informe o número de itens distintos na compra: '))

          while n_itens_compra != 0:
            #loop while que so permite codigo de itens validos
            cod_item = int(input('Informe o codigo do item: '))

            if valida_cod(cod_item) == 1:
              #apos validar o codigo, coleta a qtd de itens, o valor unitário, calcula o tot_cliente, soma às unidades e diminuiu um ciclo do loop
              quant_item = int(input('Informe a quantidade de itens: '))
              valor_un = float(input('Informe o valor unitario: '))
              tot_cliente += quant_item * valor_un
              unidades += quant_item
              n_itens_compra -= 1  # so decrementa o contador quando o                                               cod é verdadeiro
            else:
              print('Código inválido!')

          relatorio_cliente(cpf, tot_cliente)

      else:
        print('Número de compras inválido')

    else:
      print('Codigo do cliente invalido!')

    #a cada loop, compara o total do cliente com a variavel maior, caso o primeiro seja maior, atualiza as variaveis maior_cliente e maior
    if tot_cliente > maior:
      maior_cliente = cpf
      maior = tot_cliente
    tot_saldo += tot_cliente

  #                 X   |     Y = Saldo       | Z=media compra
  relatorio_caixa(data, (tot_saldo + saldo_inicial), (tot_saldo / vendas_tot),
                  unidades, maior_cliente)
  # K      |    W