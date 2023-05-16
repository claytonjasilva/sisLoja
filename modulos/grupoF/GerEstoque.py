#Grupo: Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva - TA
# Ricardo Castro - TP
# João Victor Carneiro - NT
#Criando Lista de Estoque
estoque = {}

#Função para verificar o código
def soma_cod(codigo):
    soma = sum(int(digito) for digito in str(codigo))
    if soma < 30 or soma > 100:
        print("Código inválido")
        return False
    return True

#Função incluir itens
def incluir_item():
    num_itens = int(input("Quantos itens deseja incluir? "))
    for i in range(num_itens):
        cod_item = int(input("Digite o código do item: "))
        if not soma_cod(cod_item):
            continue
        desc_item = input("Digite a descrição do item: ")
        valor_item = float(input("Digite o valor do item em reais: "))
        estoque[cod_item] = (desc_item, valor_item)
    print("Itens incluídos com sucesso!")
  
#Função para excluir itens
def excluir_item():
    cod_item = int(input("Digite o código do item que deseja excluir: "))
    if cod_item in estoque:
        confirmacao = input("Você tem certeza que deseja excluir esse item? (sim/não): ")
        if confirmacao.lower() == "sim":
            del estoque[cod_item]
            print("Item excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Item não encontrado no estoque.")

#Função para imprimir a lista do estoque
def imprimir_lista():
    print("\n=== Lista de Itens no Estoque ===")
    for cod_item, (desc_item, valor_item) in estoque.items():
        print(f"Código: {cod_item} | Descrição: {desc_item} | Valor: R${valor_item:.2f}")

#Função calculadora da média dos valores dos itens em estoque
def calcular_media_valores():
    valores = [valor for _, (_, valor) in estoque.items()]
    if valores:
        media = sum(valores) / len(valores)
        print(f"A média dos valores dos produtos em estoque é: R${media:.2f}")
    else:
        print("Não há itens no estoque.")

#Função que busca o item de maior preço
def encontrar_item_mais_caro():
    if estoque:
        cod_item_mais_caro = max(estoque, key=lambda cod_item: estoque[cod_item][1])
        desc_item_mais_caro, valor_item_mais_caro = estoque[cod_item_mais_caro]
        print(f"O item mais caro em estoque é: Código: {cod_item_mais_caro} | Descrição: {desc_item_mais_caro} | Valor: R${valor_item_mais_caro:.2f}")
    else:
        print("Não há itens no estoque.")

#Função do menu
def menu():
    while True:
        print("\n=== Gerenciamento de Estoque ===")
        print("1- Incluir item(s) no estoque")
        print("2- Excluir item do estoque")
        print("3- Imprimir lista de itens")
        print("4- Calcular média dos valores dos produtos em estoque")
        print("5- Encontrar item mais caro em estoque")
        print("0- Fechar o programa")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            incluir_item()
        elif opcao == "2":
            excluir_item()
        elif opcao == "3":
            imprimir_lista()
        elif opcao == "4":
            calcular_media_valores()
        elif opcao == "5":
            encontrar_item_mais_caro()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")

menu()
