def ger_clientes():
        clientes = []
        cpf_antigo = ''
        while True:
           #função pede para o usuario digitar um cpf e verifica se esse cpf é possivel ou impossivel
            print("--------------------------------------")
            cpf = input("Digite o CPF do cliente (0 para sair): ")
            if cpf == '0':
                break
            
            cpf = cpf.replace(".", "").replace("-", "")

            if len(cpf) != 11:
                print("CPF inválido! Não é possível inserir esse CPF.")
                continue

            if cpf == cpf_antigo:
                print("CPF repetido! Digite um CPF diferente.")
                continue

            cpf_antigo = cpf
          #pede que o usuario digite a renda do cliente (cpf) 
            renda = float(input("Digite a renda do cliente: "))
            cliente = {'cpf': cpf, 'renda': renda}
            clientes.append(cliente)

        num_clientes = len(clientes)
        #caso o primeiro cpf inserido seja igual '0'
        if num_clientes == 0:
            print("Nenhum cliente foi cadastrado.")
            print("--------------------------------------")
            return clientes
          #função que define se a renda dos usuarios cadastrados são superiores aR$ 10.000,00; entre R$ 5.000,00 e R$ 10.000,00; e inferior a R$ 5.000,00.
        renda_superior_10000 = sum(1 for cliente in clientes if cliente['renda'] > 10000)
        renda_entre_10000_e_5000 = sum(1 for cliente in clientes if 10000 >= cliente['renda'] >= 5000)
        renda_inferior_5000 = sum(1 for cliente in clientes if cliente['renda'] < 5000)
      # printa os valores registrados 
        print("--------------------------------------")
        print("OPERAÇÃO REALIZADA COM SUCESSO")
        print("Clientes cadastrados:")

        for cliente in clientes:
            cpf_formatado = "{}.{}.{}/{}".format(cliente['cpf'][:3], cliente['cpf'][3:6],
                                                 cliente['cpf'][6:9], cliente['cpf'][9:])
            print("CPF:", cpf_formatado, "- Renda:", cliente['renda'])

        print("Número de clientes cadastrados:", num_clientes)
        print("Percentual de clientes com renda superior a R$10.000,0: {:.2%}".format(renda_superior_10000 / num_clientes))
        print("Percentual de clientes com renda entre R$10.000,00 e R$5.000,00: {:.2%}".format(renda_entre_10000_e_5000 / num_clientes))
        print("Percentual de clientes com renda inferior a R$5.000,00: {:.2%}".format(renda_inferior_5000 / num_clientes))

        print("--------------------------------------")

        return clientes

lista_clientes = ger_clientes()

