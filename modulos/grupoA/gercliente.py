import re
import os

clientes = {}

def cpfValido(x):
    if len(x) != 11:
        return False

    mult_decre = 10
    digt_final_1 = 0
    digt_final_2 = 0
    for a in range(9):
        digt_final_1 += int(x[a]) * mult_decre
        mult_decre -= 1
    digt_final_1 = 11 - (digt_final_1 % 11)

    mult_decre = 10
    for a in range(9):
        digt_final_2 += int(x[a + 1]) * mult_decre
        mult_decre -= 1
    digt_final_2 = 0 if digt_final_2 % 11 < 2 else 11 - (digt_final_2 % 11)

    return x[9] == str(digt_final_1) and x[10] == str(digt_final_2)

def formatar_cpf(cpf):
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

def formatar_renda(renda):
    return "R${:,.2f}".format(renda).replace(",", ".")

def cadastrar_cliente(cpf, renda):
    if cpfValido(cpf):
        cpf_formatado = formatar_cpf(cpf)
        if cpf_formatado not in clientes:
            clientes[cpf_formatado] = renda
            print("Cliente cadastrado com sucesso!")
        else:
            print("CPF já cadastrado!")
    else:
        print("CPF inválido!")

def atualizar_renda(cpf, nova_renda):
    cpf_formatado = formatar_cpf(cpf)
    if cpf_formatado in clientes:
        clientes[cpf_formatado] = nova_renda
        print("Renda atualizada com sucesso!")
    else:
        print("CPF não encontrado!")

def exibir_clientes():
    for cpf, renda in clientes.items():
        renda_formatada = formatar_renda(renda)
        print("CPF:", cpf, "- Renda:", renda_formatada)

def validar_cpf(cpf):
    cpf = re.sub('[^0-9]', '', cpf)  # remove caracteres não numéricos
    if len(cpf) != 11:
        return False
    if cpf in (str(i)*11 for i in range(10)):
        return False
    # cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10-i) for i in range(9))
    resto = (soma * 10) % 11
    if resto in (10, 11):
        resto = 0
    if resto != int(cpf[9]):
        return False
    # cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11-i) for i in range(10))
    resto = (soma * 10) % 11
    if resto in (10, 11):
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True

def menu_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console
    adicionados = 0
    print("-----------------------------\n")
    print("GERENCIAMENTO DE CLIENTE")
    print("Escolha a opção desejada: \n")
    print("Incluir um novo cliente (1)\n")
    print("Alterar cliente existente (2)\n")
    print("-----------------------------\n")
    cliente = int(input("O que deseja fazer? "))
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console

    if cliente == 1:
        cadastrar_cliente()
    elif cliente == 2:
        alterar_renda_cliente()

def cadastrar_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa o console
    while True:
        cpf = input("Digite o CPF do cliente (0 para sair): ")
        cpf = cpf.replace(".", "").replace("-", "")  # Remover caracteres de formatação
        if cpf == "0":
            break
        if not cpfValido(cpf):
            print("CPF inválido!")
            continue
        cpf_formatado = formatar_cpf(cpf)
        if cpf_formatado in clientes:
            print("CPF já cadastrado!")
            continue
        renda_cliente = float(input("Digite a renda do cliente: R$ "))
        clientes[cpf_formatado] = renda_cliente

    if clientes:
        print("OPERAÇÃO REALIZADA COM SUCESSO")
        print(clientes)
        total = len(clientes)
        abaixo5k = len([c for c in clientes.values() if c < 5000])
        entre5k10k = len([c for c in clientes.values() if 5000 <= c < 10000])
        acima10k = len([c for c in clientes.values() if c >= 10000])
        print(f"Total de clientes cadastrados: {total}")
        print("----------------------------------------------")
        print("FAIXA", " " * 25 ,"PORCENTAGEM")
        print(f"Abaixo de R$ 5.000,00 {abaixo5k/total:.0%}")
        print(f"Entre R$ 5.000,00 e R$ 10.000,00 {entre5k10k/total:.0%}")
        print(f"Acima de R$ 10.000,00 {acima10k/total:.0%}")
        print("----------------------------------------------")
        voltar = int(input("Tecle 0 para retornar à tela principal: "))
        if voltar != 0:
            print("Ação inválida")
            voltar = int(input("Tecle 0 para voltar ao menu principal: "))

def alterar_renda_cliente():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console
    cpf_v = input("Digite o CPF do cliente a ser alterado: ")
    cpf_v = cpf_v.replace(".", "").replace("-", "")  # Remover caracteres de formatação
    cpf_formatado = formatar_cpf(cpf_v)
    if cpf_formatado in clientes:
        nova_renda = float(input("Digite a nova renda do cliente: R$ "))
        clientes[cpf_formatado] = nova_renda
        print("Renda do cliente alterada com sucesso!")
    else:
        print("Cliente não encontrado.\n")

    total = len(clientes)
    abaixo5k = len([c for c in clientes.values() if c < 5000])
    entre5k10k = len([c for c in clientes.values() if 5000 <= c < 10000])
    acima10k = len([c for c in clientes.values() if c >= 10000])
    print(f"Total de clientes cadastrados: {total}")
    print("----------------------------------------------")
    print("FAIXA", " " * 25 ,"PORCENTAGEM")
    print(f"Abaixo de R$ 5.000,00 {abaixo5k/total:.0%}")
    print(f"Entre R$ 5.000,00 e R$ 10.000,00 {entre5k10k/total:.0%}")
    print(f"Acima de R$ 10.000,00 {acima10k/total:.0%}")
    print("\n-----------------------------\n")

    # Voltar para o menu principal (sisloja)
    voltar = int(input("Tecle 0 para retornar à tela principal: "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal: "))
    else:
        from main import sisloja
      
#Alex Euzebio (202301134358) TA
#Emily Fernandes (202303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA
