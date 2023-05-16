#Função para verificar se o código é válido
def cod_valido(num):
    soma = 0
    while num != 0:
        soma += num % 10
        num //= 10
    if 30 < soma < 100:
        return 1 #O código é válido
    else:
        return 0 #O código é inválido

#Escolha de opção

operacao=input('Digite (i) para incluir um item, (e) para excluir e (s) para sair. ')
listaEstoque=[]
abacate=True
cont=0
i=0
while abacate==True:
  match operacao:
  
    #Inclusão
    case 'i':
      mvalor=0
      mcodigo=0
      total_valor=0
      total_itens=0
      
      
      qtd_itens=int(input('Digite quantos itens, no total, serão inclusos: \n'))
      total_itens+=qtd_itens
      listasaldo=['o']*qtd_itens
      
      #Loop para a quantidade de itens
      for i in range(qtd_itens): 

        #Loop caso o código não seja válido
        flag=True
        while flag==True:
          cod_item=int(input('Digite o código do item: \n'))
        
          if cod_valido(cod_item)==0: #Código inválido
            print('Código inválido.\nA soma dos digitos deve ser entre 30 e 100.\n')
            cod_item=0 
        
          elif cod_valido(cod_item)==1: #Código válido
            flag=False

        
        saldo_item=int(input('Digite a quantidade desse item que será incluso: \n'))
        desc_item=input('Digite a descrição do item: \n')
        valor_item=float(input('Digite o valor do item, em reais: \n'))
        
      
        listasaldo[cont]=saldo_item
        cont+=1 
        
        #Calculando a média
        total_valor+=valor_item
        media=total_valor/total_itens

        #Estabelecendo o código com o maior valor
        if valor_item>mvalor:
          mvalor=valor_item
          mcodigo=cod_item

        #Atualizando a listaEstoque
        item = {'Código': cod_item, 'Descrição': desc_item, 'Valor': valor_item, 'Saldo': saldo_item}
        listaEstoque.append(item)
        
        
      #Printando
      print('---------------------------------------------------')
      print('A média dos valores dos itens cadastrados é: ',media,'\n')
      print('O maior valor posto é do item de código: ',mcodigo,'e vale: ', mvalor)
      print('---------------------------------------------------')
      operacao=input('Digite (i) para incluir um item, (e) para excluir e (s) para sair. \n')
  
  #Exclusão
    case 'e':
      codigos_excluidos=[]
      sopa=True
      while sopa==True: 
        cod_excl=int(input('Digite o código a ser excluído: \n'))
      
      
        if cod_valido(cod_excl)==0:
          print('O código é inválido. Transação encerrada.\n') #Verificando se o código é válido
          sopa=False
          abacate=False

        else:
        
          alerta=input('Tem certeza que deseja excluir o item? S ou N: \n') #Alerta
        
          match alerta:
          
            case'S': #Usuário escolhe sim
            
              itens_excl=int(input('Digite quantos itens devem ser excluídos: \n'))
            
              item_encontrado=False
            
              for item in listaEstoque:
                        if item['Código'] == cod_excl:
                            item_encontrado = True
                            qtd_retirada = min(item['Saldo'], itens_excl)
                            item['Saldo'] -= qtd_retirada
                            listasaldo[listaEstoque.index(item)] -= qtd_retirada
                            codigos_excluidos.append((cod_excl,'         ', qtd_retirada,)) 
                            if item['Saldo']==0:
                                listaEstoque.remove(item)
                            break

              if item_encontrado==False:
                print ('O código é inválido pois não há saldo. Operação encerrada.\n')
                abacate=False
                sopa=False
              else:
                print('Operação relizada com sucesso: ', listaEstoque,'\n')
                desejo=input('Deseja excluir outro item? S ou N: \n')
                if desejo=='N':
                  abacate=False
                  sopa=False
                  print('Transação encerrada.\n')
                  print('Após as operações, o saldo do estoque está assim: ', listaEstoque,'\n')
                  
                  print('---------------------------------------')
                  print('RELATÓRIO DE ITENS EXCLUÍDOS \n')
                  print(' ITEM          SALDO RETIRADO \n')
                  for cod_excl in codigos_excluidos:
                    print(cod_excl)
                    print('\n')
                  print('----------------------------------------')
            
            case'N': #Usuário escolhe não
              
              
              
              print('Operação encerrada.\n')
              
              abacate=False
              sopa=False
              
                           


  
    case 's':
      print('Saiu do programa.\n')
      abacate=False