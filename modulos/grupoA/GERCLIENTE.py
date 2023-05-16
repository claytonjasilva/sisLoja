#Gercliente que funciona isoladamente

import re
import os
listacpf = []
cpf = ""

def validar_cpf(cpf):
  cpf = re.sub('[^0-9]', '', cpf)  # remove caracteres não numéricos
  if len(cpf) != 11:
    return False
  if cpf in (str(i) * 11 for i in range(10)):
    return False
  # cálculo do primeiro dígito verificador
  soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
  resto = (soma * 10) % 11
  if resto in (10, 11):
    resto = 0
  if resto != int(cpf[9]):
    return False
  # cálculo do segundo dígito verificador
  soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
  resto = (soma * 10) % 11
  if resto in (10, 11):
    resto = 0
  if resto != int(cpf[10]):
    return False
  return True


def cadastrar_cliente():
  os.system('cls' if os.name == 'nt' else 'clear')  # limpa o console
  listaClientes = []
  while True:
    cpf = input("Digite o CPF do cliente (0 para sair): ")
    if cpf == "0":
      break
    if not validar_cpf(cpf):
      print("CPF inválido!")
      continue
    renda_cliente = float(input("Digite a renda do cliente: R$ "))
    listaClientes.append((cpf, renda_cliente))
  if not listaClientes:
    print("SisLoja")
  print("OPERAÇÃO REALIZADA COM SUCESSO")
  total = len(listaClientes)
  abaixo5k = len([c for c in listaClientes if c[1] < 5000])
  entre5k10k = len([c for c in listaClientes if 5000 <= c[1] < 10000])
  acima10k = len([c for c in listaClientes if c[1] >= 10000])
  print(f"Total de clientes cadastrados: {total}")
  print("----------------------------------------------")
  print("FAIXA", " " * 25, "PORCENTAGEM")
  print(f"Abaixo de R$ 5.000,00 {abaixo5k/total:.0%}")
  print(f"Entre R$ 5.000,00 e R$ 10.000,00 {entre5k10k/total:.0%}")
  print(f"Acima de R$ 10.000,00 {acima10k/total:.0%}")
  print("----------------------------------------------")
  voltar = int(input("Tecle 0 para retornar à tela principal: "))
  if voltar != 0:
    print("Ação inválida")
    voltar = int(input("Tecle 0 para voltar ao menu principal: "))
  else:
    print("SisLoja")


cadastrar_cliente ()

#Alex Euzebio (202301134358) TA
#Emily Fernandes (@02303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA
