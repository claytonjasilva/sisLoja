#Grupo:
# Felipe Tavares Nunes de Oliveira - 202302467326 - TA
# Arthur Camaz Pinto - 202302532888 - TA
# Rafael Neiva Marques de Lima - 202208386334 - TA
# Ricardo Castro - NT
# João Victor Carneiro - NT
estoque = {}

def ger_estoque():
    def soma_cod(codigo):
        soma = sum(int(digito) for digito in str(codigo))
        if soma <= 30 or soma >= 100:
            print("Código inválido")
            return False
        return True

    def incluir_item():
        num_itens = int(input("Quantos itens deseja incluir? "))
        for _ in range(num_itens):
            cod_item = input("Digite o código do item: ")
            if not soma_cod(cod_item):
                continue
            desc_item = input("Digite a descrição do item: ")
            valor_item = float(input("Digite o valor do item em reais: "))
            saldo_item = int(input("Digite o saldo em estoque: "))
            estoque[cod_item] = {"descrição": desc_item, "valor": valor_item, "saldo": saldo_item}

            # Função para calcular média dos valores dos produtos em estoque
            valores = [estoque[cod]["valor"] for cod in estoque]
            media = sum(valores) / len(valores)
            print(f"A média dos valores dos produtos em estoque é: R${media:.2f}")

            # Função para encontrar item mais caro em estoque
            cod_item_mais_caro = max(estoque, key=lambda cod: estoque[cod]["valor"])
            desc_item_mais_caro = estoque[cod_item_mais_caro]["descrição"]
            valor_item_mais_caro = estoque[cod_item_mais_caro]["valor"]
            print(f"O item mais caro em estoque é: Código: {cod_item_mais_caro} | Descrição: {desc_item_mais_caro} | Valor: R${valor_item_mais_caro:.2f}")

    def excluir_item():
        cod_item = input("Digite o código do item que deseja excluir: ")
        if cod_item in estoque:
            confirmacao = input("Você tem certeza que deseja excluir esse item? (sim/não): ")
            if confirmacao.lower() == "sim":
                del estoque[cod_item]
                print("Item excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
        else:
            print("Item não encontrado no estoque.")

    def alterar_item():
        cod_item = input("Digite o código do item que deseja alterar: ")
        if cod_item in estoque:
            print("Dados atuais do item:")
            print(f"Código: {cod_item} | Descrição: {estoque[cod_item]['descrição']} | Valor: R${estoque[cod_item]['valor']:.2f} | Saldo em estoque: {estoque[cod_item]['saldo']}")
            print("Digite os novos dados do item:")
            desc_item = input("Nova descrição: ")
            valor_item = float(input("Novo valor em reais: "))
            saldo_item = int(input("Novo saldo em estoque: "))
            estoque[cod_item]['descrição'] = desc_item
            estoque[cod_item]['valor'] = valor_item
            estoque[cod_item]['saldo'] = saldo_item
            print("Item alterado com sucesso!")
        else:
            print("Item não encontrado no estoque.")

    def imprimir_lista():
        print("\n=== Lista de Itens no Estoque ===")
        for cod_item, item in estoque.items():
            desc_item = item["descrição"]
            valor_item = item["valor"]
            saldo_item = item["saldo"]
            print(f"Código: {cod_item} | Descrição: {desc_item} | Valor: R${valor_item:.2f} | Saldo em estoque: {saldo_item}")

    while True:
        print("\n=== Gerenciamento de Estoque ===")
        print("1- Incluir item(s) no estoque")
        print("2- Excluir item do estoque")
        print("3- Alterar item no estoque")
        print("4- Imprimir lista de itens")
        print("0- Fechar o programa")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            incluir_item()
        elif opcao == "2":
            excluir_item()
        elif opcao == "3":
            alterar_item()
        elif opcao == "4":
            imprimir_lista()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")

ger_estoque()
