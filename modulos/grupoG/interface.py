
while True:
  inicio=input("Digite estoque ou caixa ou clientes: ")
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

       #inclusao
        case'i':
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
              sopa==False
              abacate==False

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
    l=0
    i=0
    qtd_item=[]
    valor_item=[]
    x=[]
    y=-1
    total_vendas=int(input("digite o total de vendas:"))
    data=int(input("digite o dia o mes e o ano do dia de hoje(ex:141997):"))
    saldo_inicial=float(input("digite o saldo inicial do dia:"))
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
    
      valor_item.append(float(input("digite o valor do item:")))
      x.append(qtd_item[y]*valor_item[y])
      print('--------------------------------------')
      print("CADASTRO DA VENDA")
      dataf(data)
      print("codigo do cliente:",cpf)
      print("codigo do item:",codigo_item)
      print("total de vendas:",qtd_item[l])
      l+=1
    
    
    
   
    #printa todas as resoluções
    print("--------------------------------------")
    print("RELATORIO DA MOVIMENTACAO FINANCERIA:")  
    dataf(data)
    print("saldo final do caixa:",saldo_inicial+sum(x))
    print("Valor das vendas ate o momento:",sum(x)/sum(qtd_item))
    print("quantidade de itens vendidos:",sum(qtd_item))
    False
          
  
  
  
   case'clientes':
    def cadastrar_cliente(clientes):
        conjunto_clientes = set()  

        while True:
            print("--------------------------------------")
            cpf = input("Digite o CPF do cliente (0 para sair): ")
    
            if cpf == '0':
                break
    
            cpf = cpf.replace(".", "").replace("-", "")
    
            if len(cpf) != 11:
                print("CPF inválido! Não é possível inserir esse CPF.")
                continue
    
            if cpf in clientes:
                print("CPF repetido! Digite um CPF diferente.")
                continue
    
            renda = input("Digite a renda do cliente: ")
    
            renda = float
    
            cliente = {'cpf': cpf, 'renda': renda}
            clientes[cpf] = cliente
    
            cpf_formatado = "{}.{}.{}/{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
            conjunto_clientes.add((cpf_formatado, renda))

        print("--------------------------------------")
        print("OPERAÇÃO REALIZADA COM SUCESSO")
        print("Clientes cadastrados:")
        for cpf, renda in conjunto_clientes:
            print("CPF:", cpf, "- Renda:", renda)
        print("Número de clientes cadastrados:", len(clientes))
        print("--------------------------------------")
    
        return conjunto_clientes
    

    def alterar_renda(clientes):
        cpf = input("Digite o CPF do cliente que deseja alterar a renda: ")
        cpf = cpf.replace(".", "").replace("-", "")
    
        if cpf in clientes:
            while True:
                nova_renda = input("Digite a nova renda de {}: ".format(cpf))
    
                try:
                    nova_renda = float(nova_renda)
                except ValueError:
                    print("Valor de renda inválido! Digite um número válido.")
                    continue
    
                clientes[cpf]['renda'] = nova_renda
                print("A renda foi atualizada com sucesso!")
                print("A renda de {} agora é {}".format(cpf, nova_renda))
                break
    
        else:
            print("CPF não cadastrado. Digite outro CPF válido.")


    def exibir_clientes(clientes):
        conjunto_clientes = set()
    
        for cliente in clientes.values():
            cpf_formatado = "{}.{}.{}/{}".format(cliente['cpf'][:3], cliente['cpf'][3:6], cliente['cpf'][6:9], cliente['cpf'][9:])
            conjunto_clientes.add((cpf_formatado, cliente['renda']))
    
        return conjunto_clientes
    
    def main():
        clientes = {}
        while True:
            print("1. Cadastrar cliente")
            print("2. Exibir clientes cadastrados")
            print("3. Alterar renda de cliente")
            print("0. Sair")
            opcao = input("Digite o número da opção desejada: ")
    
            if opcao == '1':
                conjunto_clientes = cadastrar_cliente(clientes)
                print("Conjunto de clientes cadastrados:")
                for cpf, renda in conjunto_clientes:
                    print("CPF:", cpf, "- Renda:", renda)
            elif opcao == '2':
                conjunto_clientes = exibir_clientes(clientes)
                print("Conjunto de clientes cadastrados:")
                for cpf, renda in conjunto_clientes:
                    print("CPF:", cpf, "- Renda:", renda)
            elif opcao == '3':
                alterar_renda(clientes)
            elif opcao == '0':
                break
            else:
                print("Opção inválida! Digite um número válido.")
    
            print()
    
    
    if __name__ == "__main__":
        main()
    
    
