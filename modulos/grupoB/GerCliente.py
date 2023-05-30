clientes = []


def ger_clientes():  #modulo Ger Clientes

  #funcao checaCPF
  def checaCpf(x):
    #checa o tamanho do cpf
    if len(str(x)) != 11:
      return 0
    #soma os digitos do cpf e testa para ver se é multiplo de 11
    res = sum(int(i) for i in str(x))
    if (res % 11) == 0:
      return 1
    else:
      return 0

  #  mensagem ao final da operacao
  # x = Numero de clientes cadastrados |
  # y = % de clientes com renda inferior a 5mil |
  # y = % de clientes com renda entre 5mil e 10mil |
  # w = % de clientes com renda superior a 10mil
  def mensagem_cliente(x, y, z, k):
    print('---------------------------------')
    print('OPERAÇÃO REALIZADA COM SUCESSO')
    print('Total de clientes cadastrados: ', x)
    print('----------------------------------------------')
    print('FAIXA                              PORCENTAGEM')
    print(f'Abaixo de R$ 5.000,00                   {y}  ')
    print(f'Entre R$ 5.000,00 e R$ 10.000,00        {z}  ')
    print(f'Acima de R$ 10.000,00                   {k}  ')
    print('----------------------------------------------')
    print('Teclar 0 para retornar à tela principal')

  cont = 0
  x = True
  perc_b = 0
  perc_m = 0
  perc_a = 0

  #loop while que só admite cpf válidos
  while x == True:

    cpf = int(input("Informe o CPF: "))
    if cpf == 0:  # cpf = 0 -> sair da operação
      break

    if checaCpf(cpf) == 1:

      #cpf válido -> coleta a renda do cliente, adiciona o cpf e a renda do cliente na lista 'cliente' e adiciona esta na lista 'clientes'
      cliente = []
      print('cpf válido')
      renda_cliente = float(input("Informe a renda do cliente: "))
      cliente.append(cpf)
      cliente.append(renda_cliente)
      clientes.append(cliente)
      cont += 1

      #calcula a % de cliente por renda
      if renda_cliente < 5000:
        perc_b += 1
      elif renda_cliente < 10000:
        perc_m += 1
      else:
        perc_a += 1

    else:
      print('cpf inválido')

  perc_b = (perc_b / cont) * 100
  perc_m = (perc_m / cont) * 100
  perc_a = (perc_a / cont) * 100

  # ---->            X  |   Y   |  Z    | K
  mensagem_cliente(cont, perc_b, perc_m, perc_a)
