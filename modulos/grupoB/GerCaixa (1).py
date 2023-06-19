def ger_caixa():  # modulo GerCaixa

    # resumo do total do cliente
    # x = codigo do cliente | y = valor gasto
    def relatorio_cliente(x, y):
        print('------------------------------------------')
        print(f'Cliente {x} Total de vendas: R$ {y}')
        print('------------------------------------------')

    # valida o codigo do cliente(cpf)
    def checaCpf(x):
        # checa o tamanho do cpf
        if len(str(x)) != 11:
            return False
        # valida o cpf
        res = sum(int(i) for i in str(x))
        if (res % 11) == 0:
            return True
        else:
            return False

    # valida o codigo do produto
    def valida_cod(x):
        res = sum(int(i) for i in str(x))
        if res <= 20:
            return False
        else:
            return True

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

    def cadastrar_venda():
        cpf = int(input('Informe o código do cliente: '))
        if checaCpf(cpf):
            n_itens_compra = int(input('Informe o número de itens distintos na compra: '))
            tot_cliente = 0
            for _ in range(n_itens_compra):
                cod_item = int(input('Informe o código do item: '))
                if valida_cod(cod_item):
                    quant_item = int(input('Informe a quantidade de itens: '))
                    valor_un = float(input('Informe o valor unitário: '))
                    tot_cliente += quant_item * valor_un
                else:
                    print('Código inválido!')

            relatorio_cliente(cpf, tot_cliente)
        else:
            print('Código do cliente inválido!')

    vendas_por_dia = {}  # Dicionário para armazenar as vendas por dia

    while True:
        print('1 - Cadastrar venda')
        print('2 - Encerrar o dia')
        print('3 - Consultar quantidade de itens vendidos por dia')
        print('0 - Sair')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            data = input('Insira a Data (dd/mm/aa): ')
            if data not in vendas_por_dia:
                vendas_por_dia[data] = 0
            cadastrar_venda()
            vendas_por_dia[data] += 1
        elif opcao == 2:
            break
        elif opcao == 3:
            data_consulta = input('Insira a Data para consulta (dd/mm/aa): ')
            if data_consulta in vendas_por_dia:
                print(f'Quantidade de itens vendidos em {data_consulta}: {vendas_por_dia[data_consulta]}')
            else:
                print('Não há vendas registradas para essa data.')
        elif opcao == 0:
            return
        else:
            print('Opção inválida!')

    saldo_inicial = float(input('Informe o saldo inicial do dia: '))
    N = sum(vendas_por_dia.values())
    tot_saldo = 0
    unidades = 0
    maior_cliente = 0

    relatorio_caixa('', (tot_saldo + saldo_inicial), (tot_saldo / N), unidades, maior_cliente)



