# Parte feita por Isabella (TA) e Luigi (TA)
# OBS: João Gois (NT)

# SISTEMA SISLOJA
estoque = []
listacodigo = []
listavalores = []
listaquantidade = []
modulo = []
chave = dict()

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

