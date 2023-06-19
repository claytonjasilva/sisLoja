clientes = {}

def ger_clientes():

    def checaCpf(x):
        # Função para verificar se o CPF é válido
        cpf = ''.join(filter(str.isdigit, x))
        if len(cpf) != 11:
            return False
        res = sum(int(i) for i in cpf)
        if (res % 11) == 0:
            return True
        else:
            return False

    def mensagem_cliente(x, y, z, k):
        # Função para exibir a mensagem final da operação
        # x = Número de clientes cadastrados
        # y = % de clientes com renda inferior a 5 mil
        # z = % de clientes com renda entre 5 mil e 10 mil
        # k = % de clientes com renda superior a 10 mil
        print('---------------------------------')
        print('OPERAÇÃO REALIZADA COM SUCESSO')
        print('Total de clientes cadastrados:', x)
        print('----------------------------------------------')
        print('FAIXA                              PORCENTAGEM')
        print(f'Abaixo de R$ 5.000,00                   {y:.2f}%')
        print(f'Entre R$ 5.000,00 e R$ 10.000,00        {z:.2f}%')
        print(f'Acima de R$ 10.000,00                   {k:.2f}%')
        print('----------------------------------------------')
        print('Pressione 0 para retornar à tela principal')

    def incluir_cliente():
        # Função para incluir um cliente
        cpf = input("Informe o CPF do cliente (no formato xxx.xxx.xxx-xx): ")
        if cpf == '0':
            return
        cpf = ''.join(filter(str.isdigit, cpf))
        if checaCpf(cpf):
            renda_cliente = float(input("Informe a renda do cliente: "))
            clientes[cpf] = renda_cliente
            print("Cliente cadastrado com sucesso.")
        else:
            print('CPF inválido')

    def excluir_cliente():
        # Função para excluir um cliente
        cpf = input("Informe o CPF do cliente que deseja excluir (no formato xxx.xxx.xxx-xx): ")
        if cpf == '0':
            return
        cpf = ''.join(filter(str.isdigit, cpf))
        if cpf in clientes:
            del clientes[cpf]
            print("Cliente removido com sucesso.")
        else:
            print("Cliente não encontrado.")

    def alterar_cliente():
        # Função para alterar a renda de um cliente
        cpf = input("Informe o CPF do cliente que deseja alterar (no formato xxx.xxx.xxx-xx): ")
        if cpf == '0':
            return
        cpf = ''.join(filter(str.isdigit, cpf))
        if cpf in clientes:
            nova_renda = float(input("Informe a nova renda do cliente: "))
            clientes[cpf] = nova_renda
            print("Renda do cliente atualizada com sucesso.")
        else:
            print("Cliente não encontrado.")

    cont = 0
    perc_b = 0
    perc_m = 0
    perc_a = 0

    while True:
        print("Escolha a opção:")
        print("1 - Incluir cliente")
        print("2 - Excluir cliente")
        print("3 - Alterar renda de cliente")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            incluir_cliente()
            cont = len(clientes)
            perc_b = sum(1 for renda in clientes.values() if renda < 5000) / cont * 100
            perc_m = sum(1 for renda in clientes.values() if 5000 <= renda < 10000) / cont * 100
            perc_a = sum(1 for renda in clientes.values() if renda >= 10000) / cont * 100

        elif opcao == '2':
            excluir_cliente()
            cont = len(clientes)
            perc_b = sum(1 for renda in clientes.values() if renda < 5000) / cont * 100
            perc_m = sum(1 for renda in clientes.values() if 5000 <= renda < 10000) / cont * 100
            perc_a = sum(1 for renda in clientes.values() if renda >= 10000) / cont * 100

        elif opcao == '3':
            alterar_cliente()
            cont = len(clientes)
            perc_b = sum(1 for renda in clientes.values() if renda < 5000) / cont * 100
            perc_m = sum(1 for renda in clientes.values() if 5000 <= renda < 10000) / cont * 100
            perc_a = sum(1 for renda in clientes.values() if renda >= 10000) / cont * 100

        elif opcao == '0':
            break

        else:
            print("Opção inválida. Digite novamente.")

    mensagem_cliente(cont, perc_b, perc_m, perc_a)
