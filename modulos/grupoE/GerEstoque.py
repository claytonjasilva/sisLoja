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
