# Parte feita por Luiza (TA) e Beatriz (TA)
# OBS: João Gois (NT)
# GerClientes

listaCPF = []
listaRenda_clientes = []
listaGeral = dict()
clientes = []
modulo = []

def g(clientes):
    # Função para encontrar o primeiro dígito verificador
    def d1(cpf_d1):
        num_str = str(cpf_d1)      # converter para uma string
        primeiros_nove = num_str[0:9]      # selecionar os primeiros nove dígitos
        lista_numeros = [int(digito) for digito in primeiros_nove]      # converter cada dígito em um número inteiro
        lista_multiplicada = [lista_numeros[i] * (10 - i) for i in range(len(lista_numeros))]        # aplicar a multiplicação
        soma = sum(lista_multiplicada)         # somar os resultados
        r1 = soma % 11         # obter o resto da divisão por 11
        if r1 >= 2:
            d1 = 11 - r1
        else:
            d1 = 0
        r1 = str(d1)
        return r1

    # Função para encontrar o segundo dígito verificador
    def d2(cpf_d2):
        num_str = str(cpf_d2)      # converter para uma string
        primeiros_nove = num_str[1:10]      # pular o primeiro e selecionar os outros nove dígitos
        lista_numeros = [int(digito) for digito in primeiros_nove]      # converter cada dígito em um número inteiro
        lista_multiplicada = [lista_numeros[i] * (10 - i) for i in range(len(lista_numeros))]          # aplicar a multiplicação 
        soma = sum(lista_multiplicada)        # somar os resultados
        r2 = soma % 11         # obter o resto da divisão por 11
        if r2 >= 2:
            d2 = 11 - r2
        else:
            d2 = 0
        r2 = str(d2)
        return r2

        # Função para encontar o último e o penúltimo do CPF
    def penultimo_e_ultimo(peun):
        peun_inteiro = int(peun)        # converter para um inteiro
        ultimo_digito = peun_inteiro % 10         # obter o resto da divisão por 10
        penultimo_digito = (peun_inteiro // 10) % 10
        str_ultimo = str(ultimo_digito)           # converter para uma string
        str_penultimo = str(penultimo_digito)          # converter para uma string
        penultimo_e_ultimo = str_penultimo + str_ultimo        
        return penultimo_e_ultimo
    
    def clientes(listaRenda_clientes):
        clientes_ate_5 = sum(1 for renda in listaRenda_clientes if renda < 5000) # confere as rendas inferiores a 5000 reais
        clientes_entre_5e10 = sum(1 for renda in listaRenda_clientes if 5000 <= renda < 10000) # confere as rendas inferiores a 10000 reais e inferiores a 5000 reais
        clientes_acima_10 = sum(1 for renda in listaRenda_clientes if renda >= 10000) # confere as rendas superiores a 5000 reais
        total_clientes = clientes_ate_5 + clientes_entre_5e10 + clientes_acima_10
        print('Total de clientes cadastrados: {}'.format(total_clientes))

        print('------------------------------------------------') # interface
        print('FAIXA                             PORCENTAGEM')

        percentual_5 = (clientes_ate_5 / total_clientes) * 100
        print('Até R$5.000                        {:.2f}%'.format(percentual_5))
        percentual_5a10 = (clientes_entre_5e10 / total_clientes) * 100
        print('Entre R$5.000 e R$10.000           {:.2f}%'.format(percentual_5a10))
        percentual_10 = (clientes_acima_10 / total_clientes) * 100
        print('Acima de R$10.000                  {:.2f}%'.format(percentual_10))

        print('------------------------------------------------')
        return (" ")

    while True:    # menu GerClientes
        opcao = input(' [1] Para adicionar o CPF e a renda \n [2] Para alterar a renda \n [3] Para remover o CPF e a renda \n [4] Para ver a renda \n [5] Para voltar ao menu \n : ')
        match opcao:
          case '1':   # adicionar o cpf e a renda
            
            print('Para parar a operação aperte o 0 uma vez.\n')
            flag = 1
            while flag == 1:
              cpf = input('Digite o seu CPF (Somente números): ')
              cpf_inteiro = float(cpf)
              if cpf_inteiro == 0:
                break
      
              dois_digitos_verificados = d1(cpf) + d2(cpf)  # juntar os dois digitos

              if dois_digitos_verificados == penultimo_e_ultimo(cpf):  # checar se os dois ulitmos digitos digitados estao iguais ao do calculo
                print('CPF VALIDO')
            
                listaCPF.append(cpf) # adiciona o CPF do cliente na lista de CPF
            
                if cpf in listaCPF:
                  renda_cliente = float(input('Digite sua renda (Somente números): '))
                  listaGeral[cpf] = renda_cliente   # adicionar a renda ao dicionario 
                  listaRenda_clientes.append(renda_cliente) # adiciona a renda na lista de rendas   
            
              else:
                print('CPF INVÁLIDO')

              print('\n')

            print('\n')

            print('------------------------------------') # interface
            print('OPERAÇÃO REALIZADA COM SUCESSO')
            print(clientes(listaRenda_clientes)) 

          case '2':    # alterar a renda
            print('\n')
            
            alterar_renda = input('Digite o seu CPF: ')        #obtem cpf da entrada do usuário
            
            if alterar_renda in listaGeral.keys():
              renda_atualizada = float(input('Nova renda: '))     #obtem nova renda da entrada do usuário
              listaGeral[alterar_renda] = renda_atualizada   #alterar a renda da listaGeral
              posicao = listaCPF.index(alterar_renda)     #achar a posição do cpf que quer ser alterado
              listaRenda_clientes.pop(posicao)      #excluir a renda na listaRenda_clientes na posição que foi definida
              listaRenda_clientes.insert(posicao, renda_atualizada)     #inclui nova renda na listaRenda_clientes na posição que foi definida


              print('\n')
            
              print('------------------------------------') # interface
              print('OPERAÇÃO REALIZADA COM SUCESSO')
              print(clientes(listaRenda_clientes))

            else:
              print('CPF não encontrado')

          case '3':       # remover o cpf e a renda
              cpf_para_apagar = input("Digite o CPF a ser apagado: ")

              #verifica se o CPF está cadastrado
              if cpf_para_apagar in listaCPF:
                  
                  #Obtem a renda (a partir do indice do CPF) na lista geral
                  renda_para_apagar = listaGeral[cpf_para_apagar]

                  #apaga o CPF da listaCPF e a renda da listaRenda
                  listaCPF.remove(cpf_para_apagar)
                  listaRenda_clientes.remove(renda_para_apagar)

                  #remove CPF da listaGeral
                  del listaGeral[cpf_para_apagar]

                  print('\n')
            
                  print('------------------------------------') # interface
                  print('OPERAÇÃO REALIZADA COM SUCESSO')
                  print(clientes(listaRenda_clientes))
                
              else:
                 print("CPF não encontrado")

          case '4':   #ver a renda

            print('\n')
            ver_renda = input('Digite o seu CPF: ')
            if ver_renda in listaGeral:     #checa se CPF está na listaGeral
              print('Renda: ',listaGeral[ver_renda])   # ver a renda do cpf

            else:
              print('CPF não encontrado')

            print('\n')

          case '5':         # voltar pro menu
            print('\n')
            m(modulo)

def m(modulo):
    print("Bem vindo ao sistema SISLOJA!")
    while True:
        modulo = input(
            "Escolha o módulo desejado:\n [1] Para GerEstoque \n [2] Para GerClientes\n [3] Para GerCaixa \n [4] Para sair \nDigite o módulo que deseja: ")
        print("\n")

        match modulo:

            case '2':
              g(clientes) # abre o GerClientes caso a pessoa pressione 2
              
                
            
            case "4":
                print("Saindo") # encerra se a pessoa pressionar 4
                break

    return ("Esse foi o sistema SISLOJA")

m(modulo)
