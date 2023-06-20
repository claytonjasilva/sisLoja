#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TP

def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Validar dígitos verificadores
    def calcular_digito_verificador(digitos):
        soma = 0
        for i, digito in enumerate(digitos):
            soma += int(digito) * (len(digitos) + 1 - i)
        resto = soma % 11
        if resto < 2:
            return 0
        else:
            return 11 - resto

    digitos = cpf[:9]
    digito_verif1 = calcular_digito_verificador(digitos)
    if int(cpf[9]) != digito_verif1:
        return False

    digitos += str(digito_verif1)
    digito_verif2 = calcular_digito_verificador(digitos)
    if int(cpf[10]) != digito_verif2:
        return False

    return True


listaClientes = {}
rendas_superiores_10k = 0
rendas_entre_5k_e_10k = 0
rendas_inferiores_5k = 0

# Inicio para escolher as opções 
while True:
    print('--------------------------------------------\n')
    print('Escolha uma opção: ')
    print('1 Incluir cliente ')
    print('2 Alterar renda do cliente ')
    print('3 Excluir cliente ')
    print('0 Sair')
    opcao = input('Opção: ')

    if opcao == '0':
        break
#Inicio da opção 1 para incluir o cliente
    elif opcao == '1':
        while True:
            cpf = input("Digite o CPF do cliente: ")
            if cpf in listaClientes:
                print("CPF já cadastrado. Tente novamente.")
                continue

            if not validar_cpf(cpf):
                print('\nCPF inválido. Tente novamente.\n')
                continue

            renda_str = input("Digite a renda do cliente: ")
            try:
                renda = float(renda_str)
            except ValueError:
                print("Valor de renda inválido. Tente novamente.\n")
                continue

            cliente = {'cpf': cpf, 'renda': renda}
            listaClientes[cpf] = cliente

            if renda == 10000:
                rendas_superiores_10k += 1
            elif renda > 5000 and renda < 10000:
                rendas_entre_5k_e_10k += 1
            elif renda < 5000:
                rendas_inferiores_5k += 1

            break
#Inicia a operação de alterar a renda do cliente
    elif opcao == '2':
        if not listaClientes:
            print("Não há clientes cadastrados. ")
            continue 
         
        while True:
            cpf = input("Digite o CPF do cliente: ")
            if cpf not in listaClientes:
                print("CPF não encontrado. Tente novamente. ")
                continue

            renda_str = input("Digite a nova renda do cliente: ")
            try:
                nova_renda = float(renda_str)
            except ValueError:
                print("Valor de renda inválido. Tente novamente. ")
                continue

            cliente = listaClientes[cpf]
            renda = cliente['renda']
            cliente['renda'] = nova_renda

            # Atualizar a contagem de rendas
            if renda == 10000:
                rendas_superiores_10k -= 1
            elif renda > 5000 and renda < 10000:
                rendas_entre_5k_e_10k -= 1
            elif renda < 5000:
                rendas_inferiores_5k -= 1

            if nova_renda == 10000:
                rendas_superiores_10k += 1
            elif nova_renda > 5000 and nova_renda < 10000:
                rendas_entre_5k_e_10k += 1
            elif nova_renda < 5000:
                rendas_inferiores_5k += 1

            break
#Inicia a operação de excluir o cliente e a renda
    elif opcao == '3':
        cpf = input("Digite o CPF do cliente que deseja excluir: ")
        if cpf in listaClientes:
            cliente = listaClientes[cpf]
            renda = cliente['renda']
            del listaClientes[cpf]
            print("Cliente excluído com sucesso.")
            # Atualizar a contagem de rendas
            if renda == 10000:
                rendas_superiores_10k -= 1
            elif renda > 5000 and renda < 10000:
                rendas_entre_5k_e_10k -= 1
            elif renda < 5000:
                rendas_inferiores_5k -= 1
        else:
            print("CPF não encontrado. Tente novamente.")
            continue

# Parte das informações de resultado da operação
total_clientes = len(listaClientes)
print('--------------------------------------------\n')
print("OPERAÇÃO REALIZADA COM SUCESSO\n")
print(f"Total de clientes cadastrados: {total_clientes}\n")
print('--------------------------------------------\n')

# Inicializa variáveis de contagem
clientes_superiores_10k = 0
clientes_entre_5k_e_10k = 0
clientes_inferiores_5k = 0

# Contagem de clientes em cada faixa de renda
for cliente in listaClientes.values():
    renda = cliente['renda']
    if renda > 10000:
        clientes_superiores_10k += 1
    elif 5000 <= renda <= 10000:
        clientes_entre_5k_e_10k += 1
    elif renda < 5000:
        clientes_inferiores_5k += 1
#imprimi os resultados de toda a operação realizada
if total_clientes > 0:
    print("Faixa                             Porcentagem")
    print(f"Superior a R$ 10.000,00:         {int((clientes_superiores_10k/total_clientes)*100)}%")
    print(f"Entre R$ 5.000,00 e R$ 10.000,00: {int((clientes_entre_5k_e_10k/total_clientes)*100)}%")
    print(f"Inferior a R$ 5.000,00:           {int((clientes_inferiores_5k/total_clientes)*100)}%")
else:
    print("Nenhum cliente cadastrado.\n")
print('--------------------------------------------\n')
