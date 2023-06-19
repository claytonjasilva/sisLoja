#Grupo:
# Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva Marques de Lima - 202208386334 - TA
# Ricardo Castro - NT
# João Victor Carneiro - NT
listaClientes = []

def ger_clientes():
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

    def cadastrar_cliente():
        while True:
            cpf = input("Digite o CPF do cliente (ou '0' para sair): ")
            if cpf == '0':
                break
            if any(cliente[0] == cpf for cliente in listaClientes):
                print("CPF já cadastrado")
                continue
            if not validar_cpf(cpf):
                print("CPF inválido")
                continue
            renda = float(input("Digite a renda do cliente: R$ "))
            listaClientes.append((cpf, renda))
        print("Operação realizada com sucesso!")

    def alterar_renda_cliente():
        cpf = input("Digite o CPF do cliente a ser alterado: ")
        for i, cliente in enumerate(listaClientes):
            if cliente[0] == cpf:
                nova_renda = float(input("Digite a nova renda do cliente: R$ "))
                listaClientes[i] = (cpf, nova_renda)
                print("Renda do cliente alterada com sucesso.")
                return
        print("CPF não encontrado.")

    def excluir_cliente():
        cpf = input("Digite o CPF do cliente a ser excluído: ")
        for i, cliente in enumerate(listaClientes):
            if cliente[0] == cpf:
                del listaClientes[i]
                print("Cliente excluído com sucesso.")
                return
        print("CPF não encontrado.")

    def calcular_percentual_clientes():
        total_clientes = len(listaClientes)
        acima_10000 = len([cliente for cliente in listaClientes if cliente[1] > 10000])
        entre_5000_10000 = len([cliente for cliente in listaClientes if 5000 <= cliente[1] <= 10000])
        abaixo_5000 = len([cliente for cliente in listaClientes if cliente[1] < 5000])

        percentual_acima_10000 = (acima_10000 / total_clientes) * 100
        percentual_entre_5000_10000 = (entre_5000_10000 / total_clientes) * 100
        percentual_abaixo_5000 = (abaixo_5000 / total_clientes) * 100

        return percentual_acima_10000, percentual_entre_5000_10000, percentual_abaixo_5000

    def menu():
        while True:
            print("\n=== Gerenciamento de Clientes ===")
            print("1- Cadastrar cliente")
            print("2- Alterar renda de cliente")
            print("3- Excluir cliente")
            print("4- Imprimir relatório de clientes")
            print("0- Fechar o programa")
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                cadastrar_cliente()
            elif opcao == "2":
                alterar_renda_cliente()
            elif opcao == "3":
                excluir_cliente()
            elif opcao == "4":
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

    menu()

ger_clientes()