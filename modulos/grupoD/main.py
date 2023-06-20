#Auto-Avaliação
#Beatriz - TA
#Isabella - TA
#Hanaah - TA
#Luigi - TA
#Luiza - TA
#Joao - NT

# SISTEMA SISLOJA   

estoque = []
listacodigo = []
listavalores = []
listaquantidade = []
modulo = []
chave = dict()

listaCPF = []
listaRenda_clientes = []
listaGeral = dict()
clientes = []
listacaixa = []

caixa = []
modulo = []

# função do GerEstoque
def f(estoque):
    conjuntoitens = set() # inicializa o conjunto de itens    

    def i(estoque):  # funcao da inclusao do estoque

        quantidade = int(input("Quantos produtos serão incluídos? "))

        for i in range(quantidade):
            soma = 0  # contador da soma dos dígitos do código que o usuário colocará
            while True:
                cod_item = input("Digite o código do item: ")
              
                for digito in cod_item:
                    soma += int(digito)
        
                if soma < 30 or soma > 100:
                    chave[cod_item] = [input("Digite a descrição: "),float(input("Digite o valor: ")),int(input("Digite a quantidade(s) do(s) item(ns): "))] 
                    print("")
                    desc_item = chave[cod_item][0]
                    valor_item = chave[cod_item][1]
                    quantidade_item = chave[cod_item][2]

                    listavalores.append(valor_item)
                    listacodigo.append(cod_item)
                    conjuntoitens.add(cod_item)
                    conjuntoitens.add(desc_item)
                    conjuntoitens.add(valor_item)
                    conjuntoitens.add(quantidade_item)
                    print(conjuntoitens)
                    break
                else:
                    print("Código inválido")
          
        media = sum(listavalores) / len(listavalores) #calcular a media dos valores dos itens
        maior_valor = max([float(i) for i in listavalores]) # procura o maior valor na lista que abriga os valores dos itens
        print('----------------------------------------------------')
        print(f"Valor médio dos itens cadastrados: {media:.2f}")
        for valor_item, cod_item in zip(listavalores, listacodigo): # associa uma lista a outra, achando o elemento correspondente
            if float(valor_item) == maior_valor:
                print(f"Item de maior valor cadastrado: {cod_item} (valor: {maior_valor:.2f})")
                print('-----------------------------------------------------')    

        while True:  # opcao para o usuario retornar a tela principal ou utilizar novamente o modulo estoque
            menu = int(input("\n[0] Para retornar à tela principal \n[1] Para iniciar o estoque novamente."))
            if (menu == 0):
                m(modulo)
            elif (menu == 1):
                f(estoque)

  
    def e(estoque):  # funcao da exclusao do estoque
  
        print("Lista atual: ", chave) # mostra o estoque todo
        while True:
          codigo = input("Digite o código do item que deseja retirar: ")
          if chave[codigo][2] == 0: #verifica se há ou não estoque
            print("NÃO HÁ SALDO EM ESTOQUE")
          else:
            if codigo in chave: #verifica se o codigo está cadastrado anteriormente, não precisando de uma segunda verificação de soma dos digitos
              while True:
                if True:
                 c = input("Você tem certeza que deseja excluir o item?\n[1] Sim \n[2] Não \n")
                
                match c: 
                    case '1':
                      qnt_itens = int(input("Quantidade a ser removida: "))
                      qnt_antiga = chave[codigo][2]
                      nova_qnt = qnt_antiga - qnt_itens
                      chave[codigo][2] = nova_qnt
                           
                                             
                      if True:
                        nova_ex = input("Deseja realizar uma nova exclusão? [1]Sim \n[2]Não: ")
                        match nova_ex:
                          case '1':
                            e(estoque)
        
                          case '2':
                                      
                                      
                            print("Operação realizada com sucesso")
                            print('------------------')
                            print('relatório dos itens excluídos')
                            print('Código     Saldo') 
                            print(codigo, "     ",nova_qnt)
        
                      else:
                       print("CÓDIGO INVALIDO")
                                
              
                      while True:  # opcao para o usuario retornar a tela principal ou utilizar novamente o modulo estoque
                        menu = int(input("\n[0] Para retornar à tela principal \n[1] Para iniciar o estoque novamente."))
                        if (menu == 0):
                         m(modulo)
                        elif (menu == 1):
                          f(estoque)
                        
                      break

                    case '2':
                      m(modulo)
   
    
        else:
            print("Código não cadastrado.")

    # função de alterar itens do estoque
    def a(estoque):
      while True:
        print("Lista atual: ", chave) # mostra o estoque todo
        at_item = input("Digite o código do item que deseja alterar: ")
        if at_item in chave: # verifica que o código solicitado está cadastrado
          
          nova_lista = [input("Digite a descrição: "),float(input("Digite o valor do item: ")),int(input("Digite o saldo em estoque: ")) ] # atualiza
          chave[at_item].pop
          chave[at_item] = nova_lista
          print("Item alterado com sucesso!")
          f(estoque)
        else:
          print("Código não cadastrado, digite um código válido!")
  
    opcoesestoque = input("[1] Para inclusão \n[2] Para exclusão \n[3] Para Alterar item \n: ") # dá opções de ir pra área de inclusão ou exclusão do estoque
    match (opcoesestoque):
       case '1':
         i(estoque)
       case '2':
          e(estoque)

       case '3':
          a(estoque)

#--------------------------------------------------------------------------------------

# GerClientes
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
            
# ---------------------------------------------------------------------------

# funcao do gercaixa
def c(caixa):
    print(estoque) # mostra o estoque
    print(listaCPF) # mostra a lista de CPFs cadastrados

    while True: #opcoes do gercaixa 
        print("[1] Transação de Movimentação Financeira")
        print("[2] Cadastrar Venda")
        print("[3] Quantidade de Vendas em Determinado Dia")
        print("[0] Retornar à tela principal")
        opcao = input("Escolha uma opção: ") 

        if opcao == "1": # Transação de Movimentação financeira
            data = input("\nData [dd/mm/aaaa]: ")
            saldo_inicial = float(input("Saldo inicial do caixa no dia: "))
            N = int(input("Número total de vendas no dia: "))

            for i in range(N): # repete o pedido de dados para cada venda feita
                cpf = input("CPF: ")
                cod_item = int(input("Código do item: "))
                quant_item = int(input("Quantidade de itens: "))
                valor_un = float(input("Valor do item: "))

                listacaixa.append({'data': data, 'cpf': cpf, 'cod_item': cod_item, 'quant_item': quant_item, 'valor_un': valor_un}) # adiciona os dados da compra em uma lista do caixa

          # faz a soma dos valores das vendas para calcular a média do valor
            tot_venda = 0 
            for venda in listacaixa:
                tot_venda += venda['quant_item'] * venda['valor_un']
            med_venda = tot_venda / N
            saldo_final = saldo_inicial + tot_venda

            print("\n")
            print("----------------------------------------")
            print("RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA")
            print("Data da movimentação:", data)
            print("Saldo: R$", saldo_final)
            print("Valor médio das vendas: R$", med_venda)
            print("Total das vendas:", N, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "2": # Transação para cadastrar uma nova venda
            def cadastro_vendas(data, cpf, cod_item, quant_item):
                cad_venda = {
                    'data': data,
                    'cpf': cpf,
                    'cod_item': cod_item,
                    'quant_item': quant_item
                }
                listacaixa.append(cad_venda) #adiciona o dicionario de cadastros na lista do caixa

            data = input("Data da venda [dd/mm/aaaa]: ")
            cpf = input("CPF: ")
            cod_item = int(input("Código do item: "))     
            quant_item = int(input("Quantidade de itens: "))

            cadastro_vendas(data, cpf, cod_item, quant_item) # pega os dados do cadastro e inclui no dicionario de cadastros

            print("\n")
            print("----------------------------------------")
            print("CADASTRO DA VENDA")
            print("Data da movimentação:", data)
            print("Código do cliente:", cpf)
            print("Código do item:", cod_item)
            print("Total das vendas:", quant_item, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "3": # Determina a quantidade de vendas em determinado dia
            def quantidade_vendida_dia(data): # Funcao para determinar a quantidade de itens vendidos no dia
                quant_total = 0
                for venda in listacaixa: # varre as vendas na lista do caixa
                    if venda['data'] == data: # procura as vendas determinantes de uma data
                        quant_total += venda['quant_item'] # pega a quantidade de vendas e retorna a soma
                return quant_total
            data = input("Data [dd/mm/aaaa]: ")
            quantidade = quantidade_vendida_dia(data)
            print("\n")
            print("----------------------------------------")
            print("Quantidade de vendas no dia", data, ":", quantidade, "unidades")
            print("----------------------------------------")
            print("\n")

        elif opcao == "0": # Retorna ao menu principal
            m(modulo) # menu principal
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    while True:  # opcao para o usuario retornar a tela principal ou utilizar novamente o modulo caixa
        menu = int(input("[0] Para retornar à tela principal \n[1] Para iniciar o caixa novamente.\n"))
        if (menu == 0):
            m(modulo)
        elif (menu == 1):
            c(caixa)


# ---------------------------------------------------------------------------


# Função menu
def m(modulo):
    print("Bem vindo ao sistema SISLOJA!")
    while True:
        modulo = input(
            "Escolha o módulo desejado:\n [1] Para GerEstoque \n [2] Para GerClientes\n [3] Para GerCaixa \n [4] Para sair \nDigite o módulo que deseja: ")
        print("\n")

        match modulo:

            case '1':
                f(estoque)
            case "2":
                g(clientes)
            case "3":
                c(caixa)

            case "4":
                print("Saindo")
                break

    return ("Esse foi o sistema SISLOJA")


m(modulo)