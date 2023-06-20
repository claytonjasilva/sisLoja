#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TP

def soma_digito(n):
  soma = 0
  while n >= 1:
    digito = n % 10 
    n = n // 10
    soma = soma + digito
  return soma

def codigo_invalido():
  print("------------------")
  print("Código inválido")
  print("------------------")


#escolha da opção pelo usuário
ListaEstoque = dict()
while True:
  print("----------------------------")
  print("Sistema de Gestão da SisLoja")
  print("Escolha uma opção: \n 1) GerEstoque \n 2) GerClientes \n 3) GerCaixa")
  print("----------------------------")
  opcao = input()
  #opções
  match opcao:
    case "1":                             #GerEstoque
      print("\n----------------------------")
      op = input("Escolha a operação: \n1) Inclusão de itens \n2) Exclusão de itens \n3) Alteração de itens \n----------------------------\n")
      
      match op:
        case "1":                        #Inclusão
          soma_valores = 0               #variavel que soma os valores dos itens
          cont = 0                       #conta os itens adicionados
          maior_valor = 0                #armazena o maior valor inserido
          maior_cod = 0                  #armazena o codigo do item de maior valor
          print("\n-------------------------------")
          #quantidade de itens a ser adicionados por transação
          quantidade=int(input("Quantos itens diferentes deseja adicionar? ""\n-------------------------------\n")) 
          
          #Loop que pede ao usuário os dados dos itens e os adiciona na lista
          for i in range(quantidade):
            
            #Pede ao usuário o código do item, seu nome, seu valor e o numero de unidades que vão ficar estocadas
            print('------------------------------------')
            print('\n')
            cod_item=int(input("Digite o código do item: "))
            if soma_digito(cod_item) < 30 or soma_digito(cod_item) > 100:
              codigo_invalido()
              continue
            print('\n')
            desc_item=input("Digite o nome do item: ")
            print('\n')
            unidades=int(input("Quantas unidades deseja adicionar ao estoque: "))
            print('\n')
            valor_item=float(input("Digite o valor do item: "))
            print('------------------------------------')
             # Verifica se o item já está na lista e, em caso afirmativo, soma as unidades
            if str(cod_item) in ListaEstoque.keys():
              ListaEstoque[str(cod_item)][2] = ListaEstoque[str(cod_item)][2] + unidades

            #Se o item não foi encontrado na lista, adiciona-o
            else:
              ListaEstoque[str(cod_item)] = [desc_item, valor_item, unidades]
            #soma os valores dos itens
            soma_valores = soma_valores + valor_item*unidades   
            cont = cont + unidades
    
            #separa o maior valor e o codigo correspondente
            if valor_item > maior_valor:          
              maior_valor = valor_item
              maior_cod = cod_item
          
          #Exibe a lista preenchida pelo usuário
          if soma_valores != 0 or cont != 0:    #caso não tenha incluido nada vai dar erro de divisão por zero sem essa linha
            print("Relatorio:")
            media_valores = soma_valores / cont
            print("------------------------------------------------")
            print("Média dos valores dos itens cadastrados:R$",media_valores)
            print("Código do item de maior valor: ",maior_cod,", Valor:R$",maior_valor)
            print("------------------------------------------------")
            print("Teclar 0 para voltar para a tela principal\n ")
            x=input()


      
        #exclusão  
        case "2":
          ListaExcluidos = []        #lista dos itens que foram excluidos
          while True:
            print(ListaEstoque)
            #Pede o codigo e a quantidade a excluir
            print('\n')
            item_excluir = int(input("Digite o código do item que deseja excluir: "))
            print('\n')
            soma = 0                    #variavel para verificar o codigo
            saldo_suficiente=False
            
            if soma_digito(item_excluir) < 30 or soma_digito(item_excluir) > 100:
              codigo_invalido()
              break
              # verifica se o código do item está na lista de estoque
            if str(item_excluir) not in ListaEstoque.keys():
                codigo_invalido()
                break
              #qntd a excluir de unidades
            qtd_excluir=int(input("Quantas unidades desse item devem ser excluidas?: "))
            print('\n')
                  #confirmação para excluir o item
            excluir = input("Tem certeza que deseja excluir (sim) (nao) \n")
            print('\n')
            
            if excluir == "sim":
                    #tomar a ação com base no numero de unidades que serão excluidas
                      if ListaEstoque[str(item_excluir)][2] < qtd_excluir:
                        print("Saldo insuficiente!. Transação encerrada.")
                        break
                      ListaEstoque[str(item_excluir)][2]-=qtd_excluir
                      print("OPERAÇÃO REALIZADA COM SUCESSO")
                    #itens excluidos serão adicionados à ListaExcluidos
                      info_exclusao = [item_excluir, qtd_excluir]
                      ListaExcluidos.append(info_exclusao)
            elif excluir == "nao":
                    print("Transação encerrada")
                    break
              
            print('\n')  
            continuar = input("Deseja excluir outro item? (sim) (nao) \n")
            if continuar == "sim":
              indice = 0
              continue
            elif continuar == "nao":
              break 

          #lista o codigo do item que foi excluido e ao lado o saldo restante do mesmo no estoque
          print('\n')
          print("Relatório de itens excluídos:")  
          print("{:<10} {:<10}".format("ITEM","SALDO"))
          print("------------------------------------------------")
          for item_excluir in ListaExcluidos:
            print("{:<10} {:<10}".format(item_excluir[0],       item_excluir[1]))
            print("------------------------------------------------")
          input("Digite 0 para retornar ao menu\n")


      
        case "3":
          while True:
            print(ListaEstoque)
            item_alterar = input("Digite o código do item que deseja alterar: ")
            if str(item_alterar) not in ListaEstoque.keys():
              codigo_invalido()
              break
            desc_item=input("Digite o novo nome do item: ")
            print('\n')
            unidades=int(input("Digite a novo valor de unidades: "))
            print('\n')
            valor_item=float(input("Digite o novo valor do item: "))
            ListaEstoque[item_alterar] = [desc_item, valor_item, unidades]
            print("Alteração efetuada com sucesso.")
            print(ListaEstoque)
            print('\n')
            print("----------------------------")
            print("Relatorio de item alterado")
            print("{:<10} {:<10}   {:<10} {:<10}".format("ITEM","DESCRICAO","VALOR","SALDO"))
            print("{:<10} {:<10}   {:<10} {:<10}".format(item_alterar,       ListaEstoque[item_alterar][0],       ListaEstoque[item_alterar][1],       ListaEstoque[item_alterar][2]))
            print("-----------------------------")
            break


    case "2":
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
      
          
      
      

    case "3":
      class Venda:
          def __init__(self, data, codigo_cliente, codigo_item, quantidade):
              self.data = data
              self.codigo_cliente = codigo_cliente
              self.codigo_item = codigo_item
              self.quantidade = quantidade
      
      class Caixa:
          def __init__(self):
              self.vendas = []  # Inicializa a lista de vendas vazia
      
          def cadastrar_venda(self, data, codigo_cliente, codigo_item, quantidade):
              venda = Venda(data, codigo_cliente, codigo_item, quantidade)
              self.vendas.append(venda)  # Adiciona a venda à lista de vendas
      
          def calcular_quantidade_vendida(self, data):
              quantidade_total = 0
              for venda in self.vendas:
                  if venda.data == data:
                      quantidade_total += venda.quantidade  # Soma a quantidade de vendas para a data especificada
              return quantidade_total
      
          def calcular_saldo(self):
              saldo = 0
              for venda in self.vendas:
                  saldo += venda.quantidade  # Considerando o valor unitário dos itens como 1 para simplificar
              return saldo
      
          def calcular_valor_medio_vendas(self):
              if not self.vendas:
                  return 0
              valor_total_vendas = sum(venda.quantidade for venda in self.vendas)
              valor_medio = self.calcular_saldo() / len(self.vendas)  # Calcula o valor médio das vendas
              return valor_medio
      
          def exibir_relatorio_movimentacao(self, data):
              saldo = self.calcular_saldo()
              valor_medio = self.calcular_valor_medio_vendas()
              total_vendas = self.calcular_quantidade_vendida(data)
      
              # Exibe o cabeçalho do relatório de movimentação
              print("----------------------------------------------------------")
              print("RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA")
              print(f"Data da movimentação: {data}")
              print(f"Saldo: R$ {saldo:.2f}")
              print(f"Valor médio das vendas: R$ {valor_medio:.2f}")
              print(f"Total das vendas: {total_vendas} unidades")
              print("----------------------------------------------------------")
      
              input("Teclar 0 para retornar à tela principal")
      
          def exibir_tela_principal(self):
              while True:
                # Solicita os dados da venda para cadastrar
                  print("-------- TELA PRINCIPAL --------")
                  print("1. Cadastrar venda")
                  print("2. Gerar relatório de movimentação")
                  print("0. Sair")
                  opcao = input("Escolha uma opção: ")
      
                  if opcao == "1":
                      # Solicita os dados da venda para cadastrar
                      data_venda = input("Digite a data da venda: ")
                      codigo_cliente = input("Digite o código do cliente: ")
                      codigo_item = input("Digite o código do item: ")
                      quantidade = int(input("Digite a quantidade: "))
      
                      # Chama o método cadastrar_venda para adicionar a venda à lista de vendas
                      self.cadastrar_venda(data_venda, codigo_cliente, codigo_item, quantidade)
                      print("Venda cadastrada com sucesso!")
      
                  elif opcao == "2":
                      # Solicita a data para gerar o relatório de movimentação
                      data_relatorio = input("Digite a data para gerar o relatório: ")
      
                      # Chama o método exibir_relatorio_movimentacao para exibir o relatório
                      self.exibir_relatorio_movimentacao(data_relatorio)
      
                  elif opcao == "0":
                      # Sai do loop e encerra o programa
                      break
      
                  else:
                      print("Opção inválida. Por favor, escolha novamente.")
      
      
      # Exemplo de uso
      caixa = Caixa()
      caixa.exibir_tela_principal()
      
