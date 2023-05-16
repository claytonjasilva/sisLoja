#Grupo: Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva - TA
# Ricardo Castro - TP
# João Victor Carneiro - NT
# Criando a lista de clientes
listaClientes = []

#Função para validar o cpf
def validar_cpf(cpf):
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Verificar se o CPF é válido usando o algoritmo de verificação
    cpf = [int(digito) for digito in cpf]
    soma = sum(cpf[i] * (10 - i) for i in range(9))
    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != cpf[9]:
        return False

    soma = sum(cpf[i] * (11 - i) for i in range(10))
    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != cpf[10]:
        return False

    return True
      
# Função para cadastrar um cliente
def cadastrar_cliente():
    while True:
        cpf = input("Digite o CPF do cliente (ou '0' para sair): ")
        if cpf == '0':
            break
        if not validar_cpf(cpf):
            print("CPF inválido")
            continue
        renda = float(input("Digite a renda do cliente: R$ "))
        listaClientes.append((cpf, renda))
    print("Operação realizada com sucesso!")

# Função para calcular o percentual de clientes por faixa de renda
def calcular_percentual_clientes():
    total_clientes = len(listaClientes)
    acima_10000 = len([cliente for cliente in listaClientes if cliente[1] > 10000])
    entre_5000_10000 = len([cliente for cliente in listaClientes if 5000 <= cliente[1] <= 10000])
    abaixo_5000 = len([cliente for cliente in listaClientes if cliente[1] < 5000])

    percentual_acima_10000 = (acima_10000 / total_clientes) * 100
    percentual_entre_5000_10000 = (entre_5000_10000 / total_clientes) * 100
    percentual_abaixo_5000 = (abaixo_5000 / total_clientes) * 100

    return percentual_acima_10000, percentual_entre_5000_10000, percentual_abaixo_5000

# Função do Menu
def menu():
    while True:
        print("\n=== Gerenciamento de Clientes ===")
        print("1- Cadastrar cliente")
        print("2- Imprimir relatório de clientes")
        print("0- Fechar o programa")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            percentual_acima_10000, percentual_entre_5000_10000, percentual_abaixo_5000 = calcular_percentual_clientes()
            print("\nRelatório de Clientes:")
            print(f"Total de clientes: {len(listaClientes)}")
            print(f"Percentual de clientes com renda acima de R$ 10.000,00: {percentual_acima_10000:.2f}%")
            print(f"Percentual de clientes com renda entre R$ 5.000,00 e R$ 10.000,00: {percentual_entre_5000_10000:.2f}%")
            print(f"Percentual de clientes com renda abaixo de R$ 5.000,00: {percentual_abaixo_5000:.2f}%")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")

# Execução da função Menu
menu()
