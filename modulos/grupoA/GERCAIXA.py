import datetime
import re
import os
from gercliente import *
from gerestoque import *

def Data():
    # Formata a data sempre que necessário
    data_input = str(input("Digite a data (dd/mm/aaaa): "))
    if (data_input[2] == '/' or data_input[5] == '/'):
        # Verifica se a entrada é uma string numérica de 8 dígitos
        return data_input
    else:
        if not re.match(r'^\d{8}$', data_input):
            print("Data inválida")
            return Data()
        else:
            # Converte a string de entrada em um objeto datetime
            try:
                data = datetime.datetime.strptime(data_input, '%d%m%Y')
            except ValueError:
                print("Data inválida")
                return Data()
            else:
                # Formata a data para o formato desejado
                return data.strftime('%d/%m/%Y')

def menu_caixa():
    from main import vendas
    from main import codigos
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("MENU CAIXA")
    print("\nEscolha a opção desejada:")
    print("Cadastrar vendas (1)")
    print("Gestão Financeira (2)")
    print("-----------------------------")
    opcao = int(input("O que deseja fazer? "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        gestao_financeira(vendas)
    elif opcao == 2:
        cadastrar_vendas()

def gestao_financeira(vendas):
    os.system('cls' if os.name == 'nt' else 'clear')
    saldoCaixa = 0
    num_item = 0
    print("-----------------------------")
    print("GERENCIAMENTO DE CAIXA\n")
    data_formatada = Data()
    saldo_inicial = float(input("Digite o saldo inicial do caixa: "))

    if any(item["Data"] == data_formatada for item in vendas):
        indice_item = next(i for i, item in enumerate(vendas) if item["Data"] == data_formatada)
        cpfs_cadastrados = vendas[indice_item]["CPFs cadastrados"]
        print("A data já possui vendas cadastradas.")
    else:
        cpfs_cadastrados = {}

    N = int(input("Digite o número total de vendas do dia: "))
    print("-----------------------------")
    tot_venda = 0
    som_item = 0

    for i in range(1, N + 1):
        cpf = input("Digite o CPF do cliente (ou 's' para sair): ")
        if cpf == 's':
            break

        while not validar_cpf(cpf):
            print("CPF inválido!")
            cpf = input("Digite o CPF do cliente: ")

        if cpf not in cpfs_cadastrados:
            cpfs_cadastrados[cpf] = []

        while True:
            cod_item = input("Código do item: ")
            try:
                valor = str(cod_item)
                if verificar_soma(valor):
                    print("A soma dos dígitos é válida.")
                    break
                else:
                    print("A soma dos dígitos não está no intervalo desejado. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um valor inteiro.")

        quant_item = int(input("Digite a quantidade de itens: "))
        valor_un = float(input("Valor unitário do item em reais: "))
        tot_venda += quant_item * valor_un
        som_item += quant_item
        num_item += quant_item
        cpfs_cadastrados[cpf].append({
            "Código do item": cod_item,
            "Quantidade de itens": quant_item,
            "Valor unitário": valor_un
        })
        print("-----------------------------")

    print("-----------------------------")
    print("RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA")
    print("Data da movimentação:", data_formatada)
    print("Saldo: R$", saldo_inicial + tot_venda)
    print("Valor médio das vendas: R$", tot_venda / som_item)
    print("Total das vendas:", num_item, "unidades")
    print("-----------------------------")
    vendas.append({
        "Data": data_formatada,
        "CPFs cadastrados": cpfs_cadastrados
    })
    print("CPFs cadastrados:")
    for cpf, itens in cpfs_cadastrados.items():
        print("CPF:", cpf)
        print("Itens:")
        for item in itens:
            print("  Código do item:", item["Código do item"])
            print("  Quantidade de itens:", item["Quantidade de itens"])
            print("  Valor unitário:", item["Valor unitário"])
        print("-----------------------------")

    voltar = int(input("Teclar 0 para retornar à tela principal "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal"))
    else:
        from main import sisloja

def cadastrar_vendas():
    from main import vendas
    data_formatada = Data()
    indice_item = -1  # Inicialize a variável fora do loop

    for i, item in enumerate(vendas):
        if item["Data"] == data_formatada:
            indice_item = i
            break 

    if indice_item != -1:
        # Exibição do relatório de vendas
        print("CADASTRO DA VENDA")
        print("Data da movimentação:", vendas[indice_item]["Data"])
        cpfs_cadastrados = vendas[indice_item]["CPFs cadastrados"]
        print("CPFs cadastrados:")
        for cpf, itens in cpfs_cadastrados.items():
            print("CPF:", cpf)
            print("Itens:")
            for item in itens:
                print("  Código do item:", item["Código do item"])
                print("  Quantidade de itens:", item["Quantidade de itens"])
                print("  Valor unitário:", item["Valor unitário"])
            print("-----------------------------")
    else:
        print("A data solicitada não está cadastrada ou não pode ser encontrada")

    voltar = int(input("Teclar 0 para retornar à tela principal "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal"))
    else:
        from main import sisloja
      
#Alex Euzebio (202301134358) TA
#Emily Fernandes (@02303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA
