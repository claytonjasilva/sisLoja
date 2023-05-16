

while True:
  inicio=input("digite estoque ou caixa ou clientes:")
  match inicio: 
   case 'estoque':
    def cod_valido(num):
      soma = 0
      while num != 0:
        soma += num % 10
        num //= 10
      if 30 < soma < 100:
        return 1 #O código é válido
      else:
        return 0 #O código é inválido

     
     
     
    
     
     
      
        
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
            False
                
        
        
        
   case 'caixa':
    def cod_valido(num):#funcao para digitar um codigo valido
      soma = 0
      while num != 0:
          soma += num % 10
          num //= 10
      if 30 < soma < 100:
          return 1 #O código é válido
      else:
          return 0
    def dataf(data1):#funcao para printar a data corretamente
        z=(data1//10000)%10
        if data1>=10000000 and z==1 or z==0 or z==2 or z==3 or z==4 or z==5 or z==6 or z==7           or z==8 or z==9 :
          a=data1//1000000
          b=(data1//10000)%100
          c=data1%10000
        elif data1>=10000000:
          a=data1//1000000
          b=(data1//10000)%10
          c=data1%100000
        else:
          a=data1//100000
          b=(data1//10000)%10
          c=data1%10000
        print("data:",a,'/',b,'/',c)
        return a,b,c
    
    #declaração das variaveis e listas que vão ser usadas.
    i=0
    qtd_item=[]
    valor_item=[]
    x=[]
    y=-1
    total_vendas=int(input("digite o total de vendas:"))
    data=int(input("digite o dia o mes e o ano do dia de hoje(ex:141997):"))
    saldo_inicial=int(input("digite o saldo inicial do dia:"))
    while (total_vendas>i):#loop para cadastrar as vendas de acordo com q quantidade das mesmas.
      i=i+1
      y=y+1
    
    
      while True:#loop para nao se digitar um cpf invalido
          print("--------------------------------------")
          cpf=int(input("digite o cpf do cliente:"))
    
          if cpf == 0 or cpf//100000000<10  :
            print("cpf invalido, digite novamente.")
            False
          else:
            break
     
      flag=True
      while flag==True:#loop para digitacao correta do codigo e explicação
          codigo_item=int(input('Digite o código do item: '))
            
          if cod_valido(codigo_item)==0: #Código inválido
              print('Código inválido.\nA soma dos digitos deve ser entre 30 e 100.')
              codigo_item=0 
          
          elif cod_valido(codigo_item)==1: #Código válido
              flag=False
    
      qtd_item.append(int(input("digite quantos deste item serao adquiridos:")))
    
      valor_item.append(int(input("digite o valor do item:")))
      x.append(qtd_item[y]*valor_item[y])
    
    
    
    
   
    #printa todas as resoluções
    dataf(data)
    print("saldo final do caixa:",saldo_inicial+sum(x))
    print("Valor das vendas ate o momento:",sum(x)/sum(qtd_item))
    print("quantidade de itens vendidos:",sum(qtd_item))
    False
          
  
  
  
   case'clientes':
    def ger_clientes():
        clientes = []
        cpf_antigo = ''
        while True:
          #função pede para o usuario digitar um cpf e verifica se esse cpf é possivel ou impossivel 
            print("--------------------------------------")
            cpf = input("Digite o CPF do cliente (0 para sair): ")
            if cpf == '0':
                break
            
            cpf = cpf.replace(".", "").replace("-", "")

            if len(cpf) != 11:
                print("CPF inválido! Não é possível inserir esse CPF.")
                continue

            if cpf == cpf_antigo:
                print("CPF repetido! Digite um CPF diferente.")
                continue

            cpf_antigo = cpf
          #pede que o usuario digite a renda do cliente (cpf) 
            renda = float(input("Digite a renda do cliente: "))
            cliente = {'cpf': cpf, 'renda': renda}
            clientes.append(cliente)

        num_clientes = len(clientes)
        #caso o primeiro cpf inserido seja igual '0'
        if num_clientes == 0:
            print("Nenhum cliente foi cadastrado.")
            print("--------------------------------------")
            return clientes
          #função que define se a renda dos usuarios cadastrados são superiores aR$ 10.000,00; entre R$ 5.000,00 e R$ 10.000,00; e inferior a R$ 5.000,00. 
        renda_superior_10000 = sum(1 for cliente in clientes if cliente['renda'] > 10000)
        renda_entre_10000_e_5000 = sum(1 for cliente in clientes if 10000 >= cliente['renda'] >= 5000)
        renda_inferior_5000 = sum(1 for cliente in clientes if cliente['renda'] < 5000)
        # printa os valores registrados 
        print("--------------------------------------")
        print("OPERAÇÃO REALIZADA COM SUCESSO")
        print("Clientes cadastrados:")

        for cliente in clientes:
            cpf_formatado = "{}.{}.{}/{}".format(cliente['cpf'][:3], cliente['cpf'][3:6],
                                                 cliente['cpf'][6:9], cliente['cpf'][9:])
            print("CPF:", cpf_formatado, "- Renda:", cliente['renda'])
          
        print("Número de clientes cadastrados:", num_clientes)
        print("Percentual de clientes com renda superior a R$10.000,0: {:.2%}".format(renda_superior_10000 / num_clientes))
        print("Percentual de clientes com renda entre R$10.000,00 e R$5.000,00: {:.2%}".format(renda_entre_10000_e_5000 / num_clientes))
        print("Percentual de clientes com renda inferior a R$5.000,00: {:.2%}".format(renda_inferior_5000 / num_clientes))

        print("--------------------------------------")

        return clientes

    lista_clientes = ger_clientes()
    False

lista_clientes = ger_clientes()
     
  
  