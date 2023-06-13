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
            cod_item = int(input("Digite o código do item: "))
            if not soma_cod(cod_item):
                continue
            desc_item = input("Digite a descrição do item: ")
            valor_item = float(input("Digite o valor do item em reais: "))
            estoque[cod_item] = {"descrição": desc_item, "valor": valor_item, "quantidade": 1}

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
        cod_item = int(input("Digite o código do item que deseja excluir: "))
        if cod_item in estoque:
            if estoque[cod_item]["quantidade"] == 0:
                print("NÃO HÁ SALDO EM ESTOQUE")
            else:
                confirmacao = input("Você tem certeza que deseja excluir esse item? (sim/não): ")
                if confirmacao.lower() == "sim":
                    estoque[cod_item]["quantidade"] = 0
                    del estoque[cod_item]
                    print("Item excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")
        else:
            print("Item não encontrado no estoque.")

    def imprimir_lista():
        print("\n=== Lista de Itens no Estoque ===")
        for cod_item, item in estoque.items():
            desc_item = item["descrição"]
            valor_item = item["valor"]
            quantidade_item = item["quantidade"]
            print(f"Código: {cod_item} | Descrição: {desc_item} | Valor: R${valor_item:.2f} | Quantidade: {quantidade_item}")

    while True:
        print("\n=== Gerenciamento de Estoque ===")
        print("1- Incluir item(s) no estoque")
        print("2- Excluir item do estoque")
        print("3- Imprimir lista de itens")
        print("0- Fechar o programa")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            incluir_item()
        elif opcao == "2":
            excluir_item()
        elif opcao == "3":
            imprimir_lista()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")

ger_estoque()
