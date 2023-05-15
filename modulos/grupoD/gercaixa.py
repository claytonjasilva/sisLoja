# SISTEMA SISLOJA
estoque = []
listacodigo = []
listavalores = []
listaquantidade = []
modulo = []
listaCPF = []
listaRenda_clientes = []
caixa = []
clientes = []


# funcao do gercaixa
def c(caixa):
    print(estoque)  # mostra o estoque
    print(listaCPF) 
    print(clientes)

    # computa a data da movimentação, o saldo inicial antes da venda e o numero total de vendas no dia
    data = str(input("\nData [dd/mm/aaaa]: "))
    saldo_inicial = float(input("Saldo inicial do caixa no dia: "))
    N = int(input("Número total de vendas no dia: "))
    listacaixa = []

    # repete o pedido dos dados para as N vendas
    for i in range(N):
        cpf = input("CPF: ")
        cod_item = int(input("Código do item: "))
        quant_item = int(input("Quantidade de itens: "))
        valor_un = float(input("Valor do item: "))

        listacaixa.append({'cpf': cpf, 'cod_item': cod_item, 'quant_item': quant_item, 'valor_un': valor_un})

    # valor total das vendas
    tot_venda = 0
    for venda in listacaixa:
        tot_venda += venda['quant_item'] * venda['valor_un']

    # media do valor da venda
    med_venda = tot_venda / N
    # saldo apos a venda
    saldo_final = saldo_inicial + tot_venda

    print("\n")
    print("----------------------------------------")
    print("RELATÓRIO DE VENDAS")
    print("Data da movimentação:", data)
    print("Saldo: R$", saldo_final)
    print("Valor médio das vendas: R$", med_venda)
    print("Total das vendas:", quant_item, "unidades")
    print("----------------------------------------")
    print("\n")
    print("Teclar 0 para retornar à tela principal")
