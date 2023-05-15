# GerCleintes

listaCPF = []
listaRenda_clientes = []
clientes = []

def g(clientes):
    # Função para encontrar o primeiro dígito verificador
    def d1(cpf_d1):
        num_str = str(cpf_d1)
        primeiros_nove = num_str[0:9]
        lista_numeros = [int(digito) for digito in primeiros_nove]
        lista_multiplicada = [lista_numeros[i] * (10 - i) for i in range(len(lista_numeros))]
        soma = sum(lista_multiplicada)
        r1 = soma % 11
        if r1 >= 2:
            d1 = 11 - r1
        else:
            d1 = 0
        r1 = str(d1)
        return r1

    # Função para encontrar o segundo dígito verificador
    def d2(cpf_d2):
        num_str = str(cpf_d2)
        primeiros_nove = num_str[1:10]
        lista_numeros = [int(digito) for digito in primeiros_nove]
        lista_multiplicada = [lista_numeros[i] * (10 - i) for i in range(len(lista_numeros))]
        soma = sum(lista_multiplicada)
        r2 = soma % 11
        if r2 >= 2:
            d2 = 11 - r2
        else:
            d2 = 0
        r2 = str(d2)
        return r2

        # Função para encontar o último e o penúltimo do CPF

    def penultimo_e_ultimo(peun):
        peun_inteiro = int(peun)
        ultimo_digito = peun_inteiro % 10
        penultimo_digito = (peun_inteiro // 10) % 10
        str_ultimo = str(ultimo_digito)
        str_penultimo = str(penultimo_digito)
        penultimo_e_ultimo = str_penultimo + str_ultimo
        return penultimo_e_ultimo

    def clientes(listaRenda_clientes):
        clientes_ate_5 = sum(1 for renda in listaRenda_clientes if renda < 5000)
        clientes_entre_5e10 = sum(1 for renda in listaRenda_clientes if 5000 <= renda < 10000)
        clientes_acima_10 = sum(1 for renda in listaRenda_clientes if renda >= 10000)
        total_clientes = clientes_ate_5 + clientes_entre_5e10 + clientes_acima_10
        print('Total de clientes cadastrados: {}'.format(total_clientes))

        print('------------------------------------------------')
        print('FAIXA                             PORCENTAGEM')

        percentual_5 = (clientes_ate_5 / total_clientes) * 100
        print('Até R$5.000                        {}%'.format(percentual_5))
        percentual_5a10 = (clientes_entre_5e10 / total_clientes) * 100
        print('Entre R$5.000 e R$10.000           {}%'.format(percentual_5a10))
        percentual_10 = (clientes_acima_10 / total_clientes) * 100
        print('Acima de R$10.000                  {}%'.format(percentual_10))

        print('------------------------------------------------')
        return (" ")

    print('Para parar a operação aperte o 0 uma vez.\n')

    flag = 1
    while flag == 1:
        cpf = str(input('Digite o seu CPF (Somente números): '))
        cpf_inteiro = int(cpf)
        if cpf_inteiro == 0:
            break
        else:
            renda_cliente = int(input('Digite sua renda (Somente números): '))
            listaCPF.append(cpf)
            listaRenda_clientes.append(renda_cliente)

        dois_digitos_verificados = d1(cpf) + d2(cpf)

        if dois_digitos_verificados == penultimo_e_ultimo(cpf):
            print('CPF VALIDO')
        else:
            print('CPF INVÁLIDO')
            listaCPF.remove(cpf)
            listaRenda_clientes.remove(renda_cliente)

        print('\n')

    print('\n')

    print('------------------------------------')
    print('OPERAÇÃO REALIZADA COM SUCESSO')
    print(clientes(listaRenda_clientes))
