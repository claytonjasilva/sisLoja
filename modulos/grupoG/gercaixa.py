def cod_valido(num):
    soma = 0
    while num != 0:
        soma += num % 10
        num //= 10
    if 30 < soma < 100:
        return 1 #O código é válido
    else:
        return 0#funcao para ver a validade do codigo
def dataf(data1):
    z=(data1//10000)%10
    if data1>=10000000 and z==1 or z==0 or z==2 or z==3 or z==4 or z==5 or z==6 or z==7 or z==8 or z==9 :
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
    return a,b,c#funcao para printar a data corretamente
  
  
  
  
  


#declaração das variaveis e listas que vão ser usadas.
l=0
i=0
qtd_item=[]
valor_item=[]
x=[]
y=-1
total_vendas=int(input("digite o total de vendas:"))
data=int(input("digite o dia o mes e o ano do dia de hoje(ex:141997):"))
saldo_inicial=int(input("digite o saldo inicial do dia:"))
while (total_vendas>i):#loop para cadastrar as vendas de acordo com q quantidade das mesmas
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
print("Valor inteiro das vendas ate o momento:",sum(x)/sum(qtd_item))
print("quantidade de itens vendidos:",sum(qtd_item))
