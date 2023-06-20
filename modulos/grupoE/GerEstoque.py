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
