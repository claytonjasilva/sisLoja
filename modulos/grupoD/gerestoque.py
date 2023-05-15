# SISTEMA SISLOJA
estoque = []
listacodigo = []
listavalores = []
listaquantidade = []
modulo = []
listaCPF = []
listaRenda_clientes = []
caixa = []
clientes = []



# função do GerEstoque
def f(estoque):

    def i(estoque):  # funcao da inclusao do estoque

        quantidade = int(input("Quantos produtos serão incluídos? "))
        soma = 0

        for i in range(quantidade):

            while True:
              cod_item = input("Digite o codigo do item: ")
              for digito in cod_item:
                soma += int(digito)
              if soma >= 30 and soma <= 100:
                desc_item = input("digite a descrição do item: ")
                valor_item = float(input("Digite o valor em reais do item: "))
                print("")
                estoque.append((cod_item, desc_item, valor_item))
                listavalores.append(valor_item)
                listacodigo.append(cod_item)
                break

              else:
                print("Codigo invalido")
                
          
        media = sum(listavalores) / len(listavalores) #calcular a media dos valores dos itens
        maior_valor = max([float(i) for i in listavalores])
        print('----------------------------------------------------')
        print(f"Valor médio dos itens cadastrados: {media:.2f}")
        print(maior_valor)
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
        soma = 0
  
        print("Lista atual: ", estoque)
        codigo = input("Digite os código dos itens que deseja retirar, separados por vírgula: ")
        for digito in codigo:
          soma += int(digito)
        while True:
            if soma >= 30 and soma <= 100:
              c = input("Voce tem certeza que deseja excluir o item?\n[1] Sim \n[2] Não \n")
              match c:
                  case '1':
                      exclusao = False      
              
                      for item in estoque:
                          if item[0] == codigo:
                              item_removido = item
                              estoque.remove(item)
                              exclusao = True
                      
                              break                   
                    
                      if exclusao:
                        nova_ex = input("Deseja realizar uma nova exclusão?: ")
                        match nova_ex:
                            case '1':
                              e(estoque)

                            case '2':
                              
                              
                              print("Operação realizada com sucesso")
                              print('------------------')
                              print('relatório dos itens excluídos')
                              print('Código     Saldo') 
                              print(item_removido[0], "     ",item_removido[2])

                      else:
                        print("CÓDIGO INVALIDO")
                        
      
                      while True:  # opcao para o usuario retornar a tela principal ou utilizar novamente o modulo estoque
                          menu = int(input("\n[0] Para retornar à tela principal \n[1] Para iniciar o estoque novamente."))
                          if (menu == 0):
                              m(modulo)
                          elif (menu == 1):
                              f(estoque)
                  case '2':
                      m(modulo)
              break
      
        
            else:
              print("Codigo invalido digite novamente")
              e(estoque)
    opcoesestoque = input("[1] Para inclusão \n[2] Para exclusão \n : ")
    match (opcoesestoque):
       case '1':
         i(estoque)
       case '2':
          e(estoque)

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
            
            case "4":
                print("Saindo")
                break

    return ("Esse foi o sistema SISLOJA")


m(modulo)
