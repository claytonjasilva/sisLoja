#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TA



#escolha da opção pelo usuário
ListaEstoque = []
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
      op = input("Escolha a operação: \n1) Inclusão de itens \n2) Exclusão de itens \n----------------------------\n")
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
            print('\n')
            desc_item=input("Digite o nome do item: ")
            print('\n')
            unidades=int(input("Quantas unidades deseja adicionar ao estoque: "))
            print('\n')
            valor_item=float(input("Digite o valor do item: "))
            print('------------------------------------')
             # Verifica se o item já está na lista e, em caso afirmativo, soma as unidades
            encontrado = False
            for item in ListaEstoque:
              if item[0] == cod_item:
                item[3] += unidades
                encontrado = True
                break

            #Se o item não foi encontrado na lista, adiciona-o
            if not encontrado:
              item_info = [cod_item, desc_item, valor_item, unidades]
              ListaEstoque.append(item_info)
            #soma os valores dos itens
            soma_valores = soma_valores + valor_item*unidades   
            cont = cont + unidades
    
            #separa o maior valor e o codigo correspondente
            if valor_item > maior_valor:          
              maior_valor = valor_item
              maior_cod = cod_item
          
          #Exibe a lista preenchida pelo usuário
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
            indice = 0                  #indice da lista estoque 
            soma = 0                    #variavel para verificar o codigo
            saldo_suficiente=False
            for digito in str(item_excluir):
              soma += int(digito)
            #valida o codigo segundo a definição dada no arquivo do trabalho
            if soma>30 and soma< 100:
              # verifica se o código do item está na lista de estoque
              if not any(item_excluir == item[0] for item in ListaEstoque):
                print("------------------")
                print("Código inválido")
                print("------------------")
                break
              #qntd a excluir de unidades
              qtd_excluir=int(input("Quantas unidades desse item devem ser excluidas?: "))
              print('\n')
              while indice < len(ListaEstoque):
                #verifica se o item esta na lista
                if item_excluir == ListaEstoque[indice][0]:
                  #confirmação para excluir o item
                  excluir = input("Tem certeza que deseja excluir (sim) (nao) \n")
                  print('\n')
                  if excluir == "sim":
                    #tomar a ação com base no numero de unidades que serão excluidas
                      if ListaEstoque[indice][3] < qtd_excluir:
                        print("Saldo insuficiente!. Transação encerrada.")
                        break
                      ListaEstoque[indice][3]-=qtd_excluir
                      print("OPERAÇÃO REALIZADA COM SUCESSO")
                    #itens excluidos serão adicionados à ListaExcluidos
                      info_exclusao = [item_excluir, qtd_excluir]
                      ListaExcluidos.append(info_exclusao)
                      if ListaEstoque[indice][3] != 0:
                        print("Itens restantes: ",ListaEstoque)
                        break
                      if ListaEstoque[indice][3]==0: 
                        saldo_suficiente=True
                        ListaEstoque.remove(ListaEstoque[indice])
                        print("Itens restantes: ",ListaEstoque)
                        break
                  elif excluir == "nao":
                    print("Transação encerrada")
                    break
                elif indice < len(ListaEstoque):
                  indice = indice + 1
                  continue
                else:
                  #caso o codigo digitado nao esteja na lista
                  indice=-1
                indice=indice+1
              if indice == len(ListaEstoque) and len(ListaEstoque) == 0 and not saldo_suficiente or indice==-1:
                print("------------------")
                print("Código inválido")
                print("------------------")
                break
            else:
              #caso a soma dos digitos nao esteja entre 30 e 100
              print("------------------")
              print("Código inválido")
              print("------------------")
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
          return False # Essa parte do trecho de código é responsável por validar o primeiro dígito verificador do número do CPF. Aqui está um detalhamento do que cada linha faz:
      
        digitos += str(digito_verif1)
        digito_verif2 = calcular_digito_verificador(digitos)
        if int(cpf[10]) != digito_verif2:
          return False
      
        return True
      
      
      listaClientes = []
      rendas_superiores_10k = 0
      rendas_entre_5k_e_10k = 0
      rendas_inferiores_5k = 0 #Esta parte do trecho de código inicializa três variáveis: listaClientes, rendas_superiores_10k e rendas_entre_5k_e_10k e rendas_inferiores_5k. Veja para que serve cada variável.
      
      while True:
        print('<-------------------------------------------->\n')
        cpf = input(" Digite o CPF do cliente (ou 0 para sair): ")
        if cpf == '0':
          break
      
        if not validar_cpf(cpf):
          print('\n')
          print("      CPF inválido. Tente novamente.   ")
          continue # Esta parte do codigo e responsavel por repetir a entrada do cpf caso ele esteja errado.
          
        print('\n')
        renda = float(input(" Digite a renda do cliente: "))
        listaClientes.append({'cpf': cpf, 'renda': renda}) #Esta parte do trecho de código é um loop que permite ao usuário inserir informações sobre os clientes. Veja como funciona.
      
        if renda > 10000:
          rendas_superiores_10k += 1
        elif renda >= 5000:
          rendas_entre_5k_e_10k += 1
        else:
          rendas_inferiores_5k += 1 #Essa parte do trecho de código é responsável por categorizar a renda do cliente em diferentes faixas. Veja como funciona:
      
      total_clientes = len(listaClientes)
      print('<-------------------------------------------->\n')
      print("OPERAÇÃO REALIZADA COM SUCESSO\n")
      print('<-------------------------------------------->\n')
      print(f"Total de clientes cadastrados: {total_clientes}\n")
      print('<-------------------------------------------->\n')
      print(f"Percentual de clientes com renda superior a R$ 10.000,00:{(rendas_superiores_10k/total_clientes)*100:.2f}%\n")
      print('<-------------------------------------------->\n')
      print(f"Percentual de clientes com renda entre R$ 5.000,00 e R$ 10.000,00: {(rendas_entre_5k_e_10k/total_clientes)*100:.2f}%\n")
      print('<-------------------------------------------->\n')
      print(f"Percentual de clientes com renda inferior a R$ 5.000,00: {(rendas_inferiores_5k/total_clientes)*100:.2f}%\n")
      print('<-------------------------------------------->\n') # Esta parte do trecho de código calcula e exibe as estatísticas relacionadas aos rendimentos dos clientes. Veja o que cada linha faz:
    case "3":
      while True: # inicio do loop
        while True:
            print(' ------------------------------------------------- ')
            data = input(" | Digite a data da movimentação (DD/MM/AAAA) |: ") #Entrada da data
            data = data.replace("/", "").replace(" ", "")  # Remover separadores "/" e espaços em branco se estiverem presentes
            if len(data) < 8:
                print(" Data inválida. Digite a data no formato DD/MM/AAAA. \n")
                continue  # Retorna ao início do loop interno
            else:
                # Separar dia, mês e ano
                dia = data[:2]  # Extrai os dois primeiros caracteres da string data
                mes = data[2:4]  # Extrai os dois caracteres seguintes da string data
                ano = data[4:]  # Extrai os caracteres restantes a partir do quarto índice
                break
              
    # Entrada de dados do saldo inicial e de total de vendas
        print('\n')
        saldo_inicial = float(input(" | Digite o saldo inicial do caixa no dia: |> "))
        print('\n')
        total_vendas = int(input(" | Digite o número total de vendas realizadas: |> "))
      
        vendas = []
        print('\n')
        cpf = input(" | Digite o CPF do cliente: |> ")
        print('\n')
        cod_item = input(" | Digite o código do item: |> ")
        print('\n')
        quant_item = int(input(" | Digite a quantidade de itens: |> "))
        print('\n')
        valor_un = float(input(" | Digite o valor unitário do item: |> "))#Entrada de dados do cpf e codigo de item, quantidade de itense valor unitario do item.
    
        tot_venda = quant_item * valor_un #calcula o total de vendas
      
        vendas.append({
            'cpf': cpf,
            'cod_item': cod_item,
            'quant_item': quant_item,
            'valor_un': valor_un,
            'tot_venda': tot_venda
        })#Neste passo,está anexando um dicionário à lista de vendas. Cada dicionário representa uma venda e contém as seguintes informações:
      
        saldo_final = saldo_inicial
        for venda in vendas:
            saldo_final += venda['tot_venda'] # calcula o saldo final (saldo_final) com base no saldo inicial (saldo_inicial) e nos valores totais das vendas armazenados na lista de vendas.
      
    
        valor_total_vendas = sum(venda['tot_venda'] for venda in vendas)#calcula o valor total de todas as vendas armazenadas na lista de vendas.
      
        valor_medio_vendas = valor_total_vendas / total_vendas if total_vendas > 0 else 0 #calcula o valor médio das vendas por transação.
    
        total_itens_vendidos = sum(venda['quant_item'] for venda in vendas) #calcula o número total de itens vendidos em todas as transações de vendas.
    
        print('\n')
        print(' ---------------------------------------------- ')
        print(f" Data da movimentação: {dia}/{mes}/{ano} ")
        print('\n')
        print(f" Saldo final do caixa: R$ {saldo_final:.2f} ")
        print('\n')
        print(f" Valor médio das vendas no dia: R$ {valor_medio_vendas:.2f} ")
        print('\n')
        print(f" Total de itens vendidos: {total_itens_vendidos} ")
        print(' ----------------------------------------------- ') # imprime, data da movimentação, saldo final, valor médio total com as porcentagens 
    
        opcao = input(" Deseja repetir a entrada de informações? (S/N): ") #Pergunta se quer repetir a ação
        if opcao.lower() != 's':
            break # finaliza o codigo
  