#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TA






while True: # inicio do loop
    while True:
        print(' ------------------------------------------------- ')
        data = input(" | Digite a data da movimentação (DD/MM/AAAA) |: ") #Entrada da data
        data = data.replace("/", "").replace(" ", "")  # Remover separadores "/" e espaços em branco se estiverem presentes
        if len(data) < 8:
            print(" Data inválida. Digite a data no formato DD/MM/AAAA. \n")
            continue  # Retorna ao início do loop interno
        else:
            # Separar dia, mês e ano
            dia = data[:2]  # Extrai os dois primeiros caracteres da string data
            mes = data[2:4]  # Extrai os dois caracteres seguintes da string data
            ano = data[4:]  # Extrai os caracteres restantes a partir do quarto índice
            break
          
# Entrada de dados do saldo inicial e de total de vendas
    print('\n')
    saldo_inicial = float(input(" | Digite o saldo inicial do caixa no dia: |> "))
    print('\n')
    total_vendas = int(input(" | Digite o número total de vendas realizadas: |> "))
  
    vendas = []
    print('\n')
    cpf = input(" | Digite o CPF do cliente: |> ")
    print('\n')
    cod_item = input(" | Digite o código do item: |> ")
    print('\n')
    quant_item = int(input(" | Digite a quantidade de itens: |> "))
    print('\n')
    valor_un = float(input(" | Digite o valor unitário do item: |> "))#Entrada de dados do cpf e codigo de item, quantidade de itense valor unitario do item.

    tot_venda = quant_item * valor_un #calcula o total de vendas
  
    vendas.append({
        'cpf': cpf,
        'cod_item': cod_item,
        'quant_item': quant_item,
        'valor_un': valor_un,
        'tot_venda': tot_venda
    })#Neste passo,está anexando um dicionário à lista de vendas. Cada dicionário representa uma venda e contém as seguintes informações:
  
    saldo_final = saldo_inicial
    for venda in vendas:
        saldo_final += venda['tot_venda'] # calcula o saldo final (saldo_final) com base no saldo inicial (saldo_inicial) e nos valores totais das vendas armazenados na lista de vendas.
  

    valor_total_vendas = sum(venda['tot_venda'] for venda in vendas)#calcula o valor total de todas as vendas armazenadas na lista de vendas.
  
    valor_medio_vendas = valor_total_vendas / total_vendas if total_vendas > 0 else 0 #calcula o valor médio das vendas por transação.

    total_itens_vendidos = sum(venda['quant_item'] for venda in vendas) #calcula o número total de itens vendidos em todas as transações de vendas.

    print('\n')
    print(' ---------------------------------------------- ')
    print(f" Data da movimentação: {dia}/{mes}/{ano} ")
    print('\n')
    print(f" Saldo final do caixa: R$ {saldo_final:.2f} ")
    print('\n')
    print(f" Valor médio das vendas no dia: R$ {valor_medio_vendas:.2f} ")
    print('\n')
    print(f" Total de itens vendidos: {total_itens_vendidos} ")
    print(' ----------------------------------------------- ') # imprime, data da movimentação, saldo final, valor médio total com as porcentagens 

    opcao = input(" Deseja repetir a entrada de informações? (S/N): ") #Pergunta se quer repetir a ação
    if opcao.lower() != 's':
        break # finaliza o codigo
