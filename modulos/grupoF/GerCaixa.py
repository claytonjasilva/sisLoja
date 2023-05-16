#Grupo: Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva - TA
# Ricardo Castro - TP
# João Victor Carneiro - NT
print("=== Gerenciamento de Caixa ===")

# Função para calcular o saldo final do caixa
def calcular_saldo_final(saldo_inicial, vendas):
    saldo_final = saldo_inicial
    for venda in vendas:
        saldo_final += venda['tot_venda']
    return saldo_final

# Função para calcular a média das vendas no dia
def calcular_media_vendas(vendas):
    if len(vendas) == 0:
        return 0
    total_vendas = sum(venda['tot_venda'] for venda in vendas)
    media_vendas = total_vendas / len(vendas)
    return media_vendas

# Função para registrar a movimentação financeira
def registrar_movimentacao():
    # Obtenção dos dados iniciais
    data = input("Digite a data da movimentação: ")
    saldo_inicial = float(input("Digite o saldo inicial do caixa: R$ "))
    num_vendas = int(input("Digite o número total de vendas realizadas: "))

    vendas = []
    for _ in range(num_vendas):
        # Entrada dos dados de cada venda
        cpf = input("Digite o CPF do cliente: ")
        cod_item = input("Digite o código do item: ")
        quant_item = int(input("Digite a quantidade de itens: "))
        valor_un = float(input("Digite o valor unitário do item em reais: "))

        # Cálculo do valor total da venda
        tot_venda = quant_item * valor_un
        vendas.append({'cpf': cpf, 'cod_item': cod_item, 'quant_item': quant_item, 'valor_un': valor_un, 'tot_venda': tot_venda})

    # Cálculo do saldo final, média de vendas e total de itens vendidos
    saldo_final = calcular_saldo_final(saldo_inicial, vendas)
    media_vendas = calcular_media_vendas(vendas)
    total_itens_vendidos = sum(venda['quant_item'] for venda in vendas)

    # Exibição do relatório
    print("\n=== Relatório ===")
    print("Data da movimentação:", data)
    print("Saldo final do caixa: R$", saldo_final)
    print("Valor médio das vendas no dia: R$", media_vendas)
    print("Total de itens vendidos:", total_itens_vendidos)

# Execução do módulo GerCaixa
registrar_movimentacao()
