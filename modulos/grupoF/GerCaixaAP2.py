#Grupo:
# Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva Marques de Lima - 202208386334 - TA
# Ricardo Castro - NT
# João Victor Carneiro - NT
import datetime

# Lista de vendas
vendas = []

# Função para validar o formato da data
def validar_formato_data(data):
    try:
        datetime.datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Função para calcular o saldo final do caixa
def calcular_saldo_final(saldo_inicial):
    saldo_final = saldo_inicial
    for venda in vendas:
        saldo_final += venda['quant_item'] * venda['valor_un']
    return saldo_final

# Função para registrar a venda
def cadastrar_venda():
    # Obtenção dos dados da venda
    data = input("Digite a data da venda (dd/mm/aaaa): ")
    while not validar_formato_data(data):
        print("Formato de data inválido. Utilize o formato dd/mm/aaaa.")
        data = input("Digite a data da venda (dd/mm/aaaa): ")

    cpf = input("Digite o CPF do cliente (11 dígitos): ")
    while len(cpf) != 11:
        print("CPF inválido. O CPF deve ter 11 dígitos.")
        cpf = input("Digite o CPF do cliente (11 dígitos): ")

    cod_item = input("Digite o código do item: ")
    quant_item = int(input("Digite a quantidade de itens: "))

    # Criação do dicionário de venda
    venda = {'data': data, 'cpf': cpf, 'cod_item': cod_item, 'quant_item': quant_item}
    vendas.append(venda)

    print("Venda cadastrada com sucesso!")

# Função para obter as informações das vendas de um determinado dia
def obter_quantidade_itens_vendidos(dia):
    vendas_dia = [venda for venda in vendas if venda['data'] == dia]
    quantidade_total = sum(venda['quant_item'] for venda in vendas_dia)
    print("Quantidade de itens vendidos no dia", dia, ":", quantidade_total)

# Função para imprimir os dados de vendas cadastrados
def imprimir_vendas_cadastradas():
    print("=== Vendas Cadastradas ===")
    for venda in vendas:
        print("Data:", venda['data'])
        print("CPF:", venda['cpf'])
        print("Código do Item:", venda['cod_item'])
        print("Quantidade de Itens:", venda['quant_item'])
        print("-----------------------")

# Execução do módulo GerCaixa
print("=== Gerenciamento de Caixa ===")

while True:
    print("\nOpções:")
    print("1. Cadastrar Venda")
    print("2. Obter Quantidade de Itens Vendidos por Dia")
    print("3. Imprimir Vendas Cadastradas")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_venda()
    elif opcao == "2":
        dia_pesquisado = input("Digite a data para verificar a quantidade de itens vendidos (dd/mm/aaaa): ")
        while not validar_formato_data(dia_pesquisado):
            print("Formato de data inválido. Utilize o formato dd/mm/aaaa.")
            dia_pesquisado = input("Digite a data para verificar a quantidade de itens vendidos (dd/mm/aaaa): ")
        obter_quantidade_itens_vendidos(dia_pesquisado)
    elif opcao == "3":
        imprimir_vendas_cadastradas()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite novamente.")