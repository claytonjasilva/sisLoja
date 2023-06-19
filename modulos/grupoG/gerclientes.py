def cadastrar_cliente(clientes):
    conjunto_clientes = set()

    while True:
        print("--------------------------------------")
        cpf = input("Digite o CPF do cliente (0 para sair): ")

        if cpf == '0':
            break

        cpf = cpf.replace(".", "").replace("-", "")

        if len(cpf) != 11:
            print("CPF inválido! Não é possível inserir esse CPF.")
            continue

        if cpf in clientes:
            print("CPF repetido! Digite um CPF diferente.")
            continue

        renda = input("Digite a renda do cliente: ")

        renda = float

        cliente = {'cpf': cpf, 'renda': renda}
        clientes[cpf] = cliente

        cpf_formatado = "{}.{}.{}/{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        conjunto_clientes.add((cpf_formatado, renda))

    print("--------------------------------------")
    print("OPERAÇÃO REALIZADA COM SUCESSO")
    print("Clientes cadastrados:")
    for cpf, renda in conjunto_clientes:
        print("CPF:", cpf, "- Renda:", renda)
    print("Número de clientes cadastrados:", len(clientes))
    print("--------------------------------------")

    return conjunto_clientes


def alterar_renda(clientes):
    cpf = input("Digite o CPF do cliente que deseja alterar a renda: ")
    cpf = cpf.replace(".", "").replace("-", "")

    if cpf in clientes:
        while True:
            nova_renda = input("Digite a nova renda de {}: ".format(cpf))

            try:
                nova_renda = float(nova_renda)
            except ValueError:
                print("Valor de renda inválido! Digite um número válido.")
                continue

            clientes[cpf]['renda'] = nova_renda
            print("A renda foi atualizada com sucesso!")
            print("A renda de {} agora é {}".format(cpf, nova_renda))
            break

    else:
        print("CPF não cadastrado. Digite outro CPF válido.")


def exibir_clientes(clientes):
    conjunto_clientes = set()

    for cliente in clientes.values():
        cpf_formatado = "{}.{}.{}/{}".format(cliente['cpf'][:3], cliente['cpf'][3:6], cliente['cpf'][6:9], cliente['cpf'][9:])
        conjunto_clientes.add((cpf_formatado, cliente['renda']))

    return conjunto_clientes

def main():
    clientes = {}
    while True:
        print("1. Cadastrar cliente")
        print("2. Exibir clientes cadastrados")
        print("3. Alterar renda de cliente")
        print("0. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            conjunto_clientes = cadastrar_cliente(clientes)
            print("Conjunto de clientes cadastrados:")
            for cpf, renda in conjunto_clientes:
                print("CPF:", cpf, "- Renda:", renda)
        elif opcao == '2':
            conjunto_clientes = exibir_clientes(clientes)
            print("Conjunto de clientes cadastrados:")
            for cpf, renda in conjunto_clientes:
                print("CPF:", cpf, "- Renda:", renda)
        elif opcao == '3':
            alterar_renda(clientes)
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Digite um número válido.")

        print()


if __name__ == "__main__":
    main()

