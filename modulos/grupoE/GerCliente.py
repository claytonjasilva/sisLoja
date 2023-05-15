#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TA




def validar_cpf(cpf):
  # Remover caracteres não numéricos
  cpf = ''.join(filter(str.isdigit, cpf))

  # Verificar se o CPF tem 11 dígitos
  if len(cpf) != 11:
    return False

  # Verificar se todos os dígitos são iguais
  if cpf == cpf[0] * 11:
    return False

  # Validar dígitos verificadores
  def calcular_digito_verificador(digitos):
    soma = 0
    for i, digito in enumerate(digitos):
      soma += int(digito) * (len(digitos) + 1 - i)
    resto = soma % 11
    if resto < 2:
      return 0
    else:
      return 11 - resto

  digitos = cpf[:9]
  digito_verif1 = calcular_digito_verificador(digitos)
  if int(cpf[9]) != digito_verif1:
    return False # Essa parte do trecho de código é responsável por validar o primeiro dígito verificador do número do CPF. Aqui está um detalhamento do que cada linha faz:

  digitos += str(digito_verif1)
  digito_verif2 = calcular_digito_verificador(digitos)
  if int(cpf[10]) != digito_verif2:
    return False

  return True


listaClientes = []
rendas_superiores_10k = 0
rendas_entre_5k_e_10k = 0
rendas_inferiores_5k = 0 #Esta parte do trecho de código inicializa três variáveis: listaClientes, rendas_superiores_10k e rendas_entre_5k_e_10k e rendas_inferiores_5k. Veja para que serve cada variável.

while True:
  print('<-------------------------------------------->\n')
  cpf = input(" Digite o CPF do cliente (ou 0 para sair): ")
  if cpf == '0':
    break

  if not validar_cpf(cpf):
    print('\n')
    print("      CPF inválido. Tente novamente.   ")
    continue # Esta parte do codigo e responsavel por repetir a entrada do cpf caso ele esteja errado.
    
  print('\n')
  renda = float(input(" Digite a renda do cliente: "))
  listaClientes.append({'cpf': cpf, 'renda': renda}) #Esta parte do trecho de código é um loop que permite ao usuário inserir informações sobre os clientes. Veja como funciona.

  if renda > 10000:
    rendas_superiores_10k += 1
  elif renda >= 5000:
    rendas_entre_5k_e_10k += 1
  else:
    rendas_inferiores_5k += 1 #Essa parte do trecho de código é responsável por categorizar a renda do cliente em diferentes faixas. Veja como funciona:

total_clientes = len(listaClientes)
print('<-------------------------------------------->\n')
print("OPERAÇÃO REALIZADA COM SUCESSO\n")
print('<-------------------------------------------->\n')
print(f"Total de clientes cadastrados: {total_clientes}\n")
print('<-------------------------------------------->\n')
print(f"Percentual de clientes com renda superior a R$ 10.000,00: {(rendas_superiores_10k/total_clientes)*100:.2f}%\n")
print('<-------------------------------------------->\n')
print(f"Percentual de clientes com renda entre R$ 5.000,00 e R$ 10.000,00: {(rendas_entre_5k_e_10k/total_clientes)*100:.2f}%\n")
print('<-------------------------------------------->\n')
print(f"Percentual de clientes com renda inferior a R$ 5.000,00: {(rendas_inferiores_5k/total_clientes)*100:.2f}%\n")
print('<-------------------------------------------->\n') # Esta parte do trecho de código calcula e exibe as estatísticas relacionadas aos rendimentos dos clientes. Veja o que cada linha faz:
