estoque = []

def ger_estoque():  # modulo GerEstoque

    def valida_cod(x):
        # Função para validar o código do item
        res = sum(int(i) for i in str(x))
        if res <= 20:
            return False
        else:
            return True

    def confirma_excl(x, y):
        # Função para confirmar a exclusão de um item do estoque
        print('TEM CERTEZA QUE DESEJA EXCLUIR O ITEM?')
        resp = input('')
        if resp == 'sim':
            for i in range(len(y)):
                if y[i][0] == x:
                    print(f'Item excluído {y[i]}')
                    del (y[i])

    def multi_del():
        # Função para permitir a exclusão de múltiplos itens
        multi = input('Deseja deletar mais itens? ')
        if multi == 'nao':
            return 1
        elif multi == 'sim':
            return 0
        else:
            multi_del()

    def natureza_estoque():
        # Função para exibir as opções disponíveis para manipulação do estoque
        print('Selecionar a opção desejada:')
        print('Incluir itens (1)')
        print('Excluir item (2)')
        print('Alterar item (3)')

    def conclu_excl(x, y):
        # Função para exibir o relatório de itens excluídos
        print('----------------------------------------')
        print('RELATÓRIO DE ITENS EXCLUÍDOS')
        print('ITEM     SALDO')
        for i in range(len(x)):
            print(x[i][0], "    ", y.count(x[i]))
        print('----------------------------------------')
        print('Pressione 0 para retornar à tela principal')

    def conclu_incl(x, y, z):
        # Função para exibir o relatório de inclusão de itens
        print('-----------------------------')
        print(f'Valor médio dos itens cadastrados: R$ {x}')
        print(f'Item de maior valor cadastrado: código {y}, valor R$ {z}')
        print('-----------------------------')
        print('Pressione 0 para retornar à tela principal')

    def alterar_item(x, y):
        # Função para alterar um item do estoque
        cod_alterar = int(input('Informe o código do item a ser alterado: '))
        for i in range(len(x)):
            if x[i][0] == cod_alterar:
                print(f'Dados atuais do item {x[i]}')
                print('Informe os novos dados:')
                x[i][1] = input('Nova descrição do item: ')
                x[i][2] = float(input('Novo valor do item: '))
                x[i][3] = int(input('Novo saldo em estoque: '))
                print(f'Item alterado: {x[i]}')

                # Gerar relatório de item alterado
                print('----------------------------------------')
                print('RELATÓRIO DE ITEM ALTERADO')
                print('ITEM     DESCRICAO     VALOR     SALDO EM ESTOQUE')
                print(f'{x[i][0]}    {x[i][1]}    {x[i][2]}    {x[i][3]}')
                print('----------------------------------------')
                print('Pressione 0 para retornar à tela principal')
                break
        else:
            print('Item não encontrado no estoque.')

    natureza = int(input('Selecionar a opção desejada:\n1 - Incluir itens\n2 - Excluir itens\n3 - Alterar item\n'))

    if natureza == 1:
        N = float(input('Informe o número de itens que deseja adicionar: '))
        soma = 0
        maior = 0

        for i in range(int(N)):
            x = True
            while x:
                cod_item = int(input('Informe o código do item: '))

                if not valida_cod(cod_item):
                    print('Código inválido')
                else:
                    item = []
                    desc_item = input('Informe a descrição do item: ')
                    valor_item = float(input('Informe o valor do item: '))
                    saldo_item = int(input('Informe o saldo em estoque: '))
                    item.append(cod_item)
                    item.append(desc_item)
                    item.append(valor_item)
                    item.append(saldo_item)
                    estoque.append(item)
                    x = False

                    if valor_item > maior:
                        maior = valor_item
                        maior_cod = cod_item
                    soma += valor_item

        media_valor = soma / N
        conclu_incl(media_valor, maior_cod, maior)

    elif natureza == 2:
        N = 0
        while N == 0:
            cod_excl = int(input('Informe o código do item a ser excluído: '))
            confirma_excl(cod_excl, estoque)
            N += multi_del()

        estoque_limpo = []
        for i in estoque:
            if i not in estoque_limpo:
                estoque_limpo.append(i)

        conclu_excl(estoque_limpo, estoque)

    elif natureza == 3:
        alterar_item(estoque, estoque)


