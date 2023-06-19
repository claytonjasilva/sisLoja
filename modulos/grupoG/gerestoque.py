#GerEstoque

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

operacao=input('Digite (i) para incluir um item, (e) para excluir e (a)para alterar um item(s) para sair.\n ')
listasaldo=[]
listacod=[]
listaval=[]
listadesc=[]
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

        listacod.append(str(cod_item))
        saldo_item=int(input('Digite a quantidade desse item que será incluso: \n'))
        listasaldo.append(saldo_item)
        desc_item=input('Digite a descrição do item: \n')
        listadesc.append(desc_item)
        valor_item=float(input('Digite o valor do item, em reais: \n'))
        listaval.append(valor_item)
    
        #Calculando a média
        total_valor+=valor_item
        media=total_valor/total_itens

        #Estabelecendo o código com o maior valor
        if valor_item>mvalor:
          mvalor=valor_item
          mcodigo=cod_item

        #Atualizando a listaEstoque
       
        
      #Printando
      print('------------------------------\n')
      print('valor medio dos itens cadastrados é: ',media,'\n')
      print('Item de maior valor cadastrado é: ',mcodigo,'e vale: ', mvalor,'\n')
      print('------------------------------\n')
      operacao=input('Digite (i) para incluir um item, (e) para excluir,(a) para alterar um item ou (0) para sair. \n')
  
  #Exclusão
    case 'e':
      sopa=True
      
      while sopa==True: 
        cod_excl=input('Digite o código a ser excluído: \n')
        
      
        if cod_excl not in listacod:
          print('O código é inválido. Transação encerrada.\n') #Verificando se o código é válido
          sopa=False
          abacate=False

        else:
          indice=listacod.index(cod_excl)
          
          alerta=input('Tem certeza que deseja excluir o item? S ou N: \n') #Alerta
        
          match alerta:
          
            case'S': #Usuário escolhe sim
            
              itens_excl=int(input('Digite quantos itens devem ser excluídos: \n'))
              listasaldo[indice]-=itens_excl
  
              
                  
                  
                    
                        
              if listasaldo[indice]<0:
                print ('O código é inválido pois não há saldo suficiente. Operação encerrada.\n')
                listasaldo[indice]+=itens_excl
              
                sopa=False
                operacao=input('Digite (i) para incluir um item, (e) para excluir,(a) para alterar um item ou (0) para sair. \n')
              else:
                print('------------------------------------\n')
                print('Relatorio de itens excluídos\n')
                print('item     saldo')
                for i in range (total_itens):
                  print(listacod[i],'     ',listasaldo[i],'\n')
                print('------------------------------------\n')
                desejo=input('Deseja excluir outro item? S ou N: \n')
                if desejo=='N':
                  
                  sopa=False
                  print('Transação encerrada.\n')
                  operacao=input('Digite (i) para incluir um item, (e) para excluir,(a) para alterar um item ou (0) para sair. \n')
                  sopa=False
                
              
            
          
            case'N': #Usuário escolhe não
              print('Operação encerrada.\n')
             
              operacao=input('Digite (i) para incluir um item, (e) para excluir,(a) para alterar um item ou (0) para sair. \n')
          
              sopa=False
              
    
    case 's':
      print('Saiu do programa.\n')
      abacate=False
    case 'a':
      altera=0
      altera=input('digite o codigo q deseja alterar: ')
      if altera not in listacod:
        print('codigo invalido')
      else:  
        indice=listacod.index(altera)
        listasaldo[indice]=int(input('digite o novo saldo: \n'))
        listaval[indice]=int(input('digite o novo valor: \n'))
        listadesc[indice]=input('digite a nova descricao: \n')
        print('------------------------------------------------')
        print('Item          Descrição          Valor         Saldo')
        print(listacod[indice],'      ',listadesc[indice],'              ',listaval[indice],'                 ',listasaldo[indice])
        print('------------------------------------------------\n\n') 
        operacao=input('Digite (i) para incluir um item, (e) para excluir,(a) para alterar um item ou (0) para sair. \n')
