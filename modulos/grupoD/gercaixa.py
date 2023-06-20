# Feita por Hannah (TA)
# OBS: João Gois (NT)

# SISTEMA SISLOJA
estoque = []  
listacodigo = []
listavalores = []
modulo = []
listaCPF = []
listaRenda_clientes = []
caixa = []
clientes = []
listacaixa = []


# funcao do gercaixa
def c(caixa):
    print(estoque) # mostra o estoque
    print(listaCPF) # mostra a lista de CPFs cadastrados

    while True: #opcoes do gercaixa 
        print("[1] Transação de Movimentação Financeira")
        print("[2] Cadastrar Venda")
        print("[3] Quantidade de Vendas em Determinado Dia")
        print("[0] Retornar à tela principal")
        opcao = input("Escolha uma opção: ") 

        if opcao == "1": # Transação de Movimentação financeira
            data = input("\nData [dd/mm/aaaa]: ")
            saldo_inicial = float(input("Saldo inicial do caixa no dia: "))
            N = int(input("Número total de vendas no dia: "))

            for i in range(N): # repete o pedido de dados para cada venda feita
                cpf = input("CPF: ")
                cod_item = int(input("Código do item: "))
                quant_item = int(input("Quantidade de itens: "))
                valor_un = float(input("Valor do item: "))

                listacaixa.append({'data': data, 'cpf': cpf, 'cod_item': cod_item, 'quant_item': quant_item, 'valor_un': valor_un}) # adiciona os dados da compra em uma lista do caixa

          # faz a soma dos valores das vendas para calcular a média do valor
            tot_venda = 0 
            for venda in listacaixa:
                tot_venda += venda['quant_item'] * venda['valor_un']
            med_venda = tot_venda / N
            saldo_final = saldo_inicial + tot_venda

            print("\n")
            print("----------------------------------------")
            print("RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA")
            print("Data da movimentação:", data)
            print("Saldo: R$", saldo_final)
            print("Valor médio das vendas: R$", med_venda)
            print("Total das vendas:", N, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "2": # Transação para cadastrar uma nova venda
            def cadastro_vendas(data, cpf, cod_item, quant_item):
                cad_venda = {
                    'data': data,
                    'cpf': cpf,
                    'cod_item': cod_item,
                    'quant_item': quant_item
                }
                listacaixa.append(cad_venda) #adiciona o dicionario de cadastros na lista do caixa

            data = input("Data da venda [dd/mm/aaaa]: ")
            cpf = input("CPF: ")
            cod_item = int(input("Código do item: "))     
            quant_item = int(input("Quantidade de itens: "))

            cadastro_vendas(data, cpf, cod_item, quant_item) # pega os dados do cadastro e inclui no dicionario de cadastros

            print("\n")
            print("----------------------------------------")
            print("CADASTRO DA VENDA")
            print("Data da movimentação:", data)
            print("Código do cliente:", cpf)
            print("Código do item:", cod_item)
            print("Total das vendas:", quant_item, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "3": # Determina a quantidade de vendas em determinado dia
            def quantidade_vendida_dia(data): # Funcao para determinar a quantidade de itens vendidos no dia
                quant_total = 0
                for venda in listacaixa: # varre as vendas na lista do caixa
                    if venda['data'] == data: # procura as vendas determinantes de uma data
                        quant_total += venda['quant_item'] # pega a quantidade de vendas e retorna a soma
                return quant_total
            data = input("Data [dd/mm/aaaa]: ")
            quantidade = quantidade_vendida_dia(data)
            print("\n")
            print("----------------------------------------")
            print("Quantidade de vendas no dia", data, ":", quantidade, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "0": # Retorna ao menu principal
            m(modulo) # menu principal
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    while True:  # opcao para o usuario retornar a tela principal ou utilizar novamente o modulo caixa
        menu = int(input("[0] Para retornar à tela principal \n[1] Para iniciar o caixa novamente.\n"))
        if (menu == 0):
            m(modulo)
        elif (menu == 1):
            c(caixa)


def m(modulo):
    print("Bem vindo ao sistema SISLOJA!")
    while True:
        modulo = input(
            "Escolha o módulo desejado:\n [1] Para GerEstoque \n [2] Para GerClientes\n [3] Para GerCaixa \n [4] Para sair \nDigite o módulo que deseja: ")
        print("\n")

        match modulo:
            case '3':
              c(caixa)
            case "4":
                print("Saindo")
                break
    return ("Esse foi o sistema SISLOJA")
m(modulo)

