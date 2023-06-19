import os

itens_excluidos = []  # Inicializa uma lista para o relatório de itens excluídos

def atualizar_estoque(listaEstoque, cod_item, quantidade):
    for item in listaEstoque:
        if item["codigo"] == cod_item:
            item["saldo"] -= quantidade
            break


def verificar_soma(cod_item):
    soma = sum(int(digito) for digito in str(cod_item))
    if 30 < soma < 100:
        return True
    else:
        return False

def menu_estoque(listaEstoque):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console
    adicionados = 0
    print("-----------------------------\n")
    print("GERENCIAMENTO DE ESTOQUE")
    print("Escolha a opção desejada: \n")
    print("Incluir itens (1)\n")
    print("Excluir itens (2)\n")
    print("Alterar item (3)\n")
    print("-----------------------------\n")
    estoque = int(input("O que deseja fazer? "))
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o console

    if estoque == 1:
        adicionar(listaEstoque)

    elif estoque == 2:
        excluir(listaEstoque)

    elif estoque == 3:
        alterar(listaEstoque)

def adicionar(listaEstoque):
    adicionados = 0
    somadosvalores = 0
    print("-----------------------------\n")
    print("Opção selecionada: incluir itens\n")
    numitens = int(input("Quantos itens serão inclusos ao estoque? "))

    while adicionados < numitens:
        print("\n-----------------------------\n")
        while True:
            cod_item = str(input("Código do item: "))
            try:
                valor = str(cod_item)
                if verificar_soma(valor):
                    print("A soma dos dígitos é válida.")
                    break
                else:
                    print("A soma dos dígitos não está no intervalo desejado. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um valor inteiro.")

        desc_item = str(input("Digite uma breve descrição do item: "))
        saldo = int(input("Quantos desse item serão adicionados ao estoque: "))
        atualizar_estoque(listaEstoque, cod_item, saldo)

        valor_item = float(input("Digite o valor do item: "))

        novo_item = True

        for item in listaEstoque:
            if item["codigo"] == cod_item:
                item["saldo"] += saldo
                novo_item = False
                break

        if novo_item:
            estoque_item = {
                "codigo": cod_item,
                "descricao": desc_item,
                "valor": valor_item,
                "saldo": saldo
            }
            listaEstoque.append(estoque_item)

        somadosvalores += valor_item
        adicionados += 1

    print("\n-----------------------------\n")
    print("Os itens foram adicionados com sucesso!\n")
    print("-" * 30, "\n")

    media = somadosvalores / adicionados

    cod_maior_valor = ""
    maior_valor = 0

    for item in listaEstoque:
        if item["valor"] > maior_valor:
            maior_valor = item["valor"]
            cod_maior_valor = item["codigo"]

    for item in listaEstoque:
        if item["valor"] > maior_valor:
            maior_valor = item["valor"]
            cod_maior_valor = item["codigo"]

    for item in listaEstoque:
        if item["codigo"] == cod_maior_valor:
            descricao_item = item["descricao"]
            valor_item = item["valor"]
            saldo_item = item["saldo"]
            break

    print("O item de código '{}' refere-se à lista: ['{}', {}, {}]".format(cod_maior_valor, descricao_item, valor_item, saldo_item))
    print("\n")
    print("A média de valor dos itens adicionados é:", media, "\n")
    print("-" * 30, "\n")
    print(listaEstoque)

    voltar = int(input("Tecle 0 para retornar à tela principal: "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal: "))

    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal: "))
    else:
        return listaEstoque

def excluir(listaEstoque):
    print(listaEstoque)
    print("-----------------------------")
    print("Opção selecionada: excluir itens\n")
    itens_excluidos = []  # Limpa a lista de itens excluídos
    while True:
        cod_item_excluir = str(input("Código do item a ser excluído: "))
        print("\n-----------------------------\n")
        print("\nTem certeza que deseja excluir esse item? \n")
        resp = input("Digite sim ou não: ").lower()

        if resp == 'sim':
            print(listaEstoque)
            indice_item = -1
            for i, item in enumerate(listaEstoque):
                if item["codigo"] == cod_item_excluir:
                    indice_item = i
                    break
            if indice_item != -1:
                quantidade_excluir = int(input("Quantas unidades deseja excluir? "))
                if quantidade_excluir <= item["saldo"]:
                    item_excluido = listaEstoque[indice_item]
                    item_excluido["saldo"] -= quantidade_excluir
                    if item_excluido["saldo"] == 0:
                        listaEstoque.pop(indice_item)
                    itens_excluidos.append(item_excluido)
                    print(f"{quantidade_excluir} unidades do item {cod_item_excluir} foram excluídas com sucesso!")
                else:
                    print("Quantidade inválida. Não há saldo suficiente para exclusão.")
            else:
                print(f"O item {cod_item_excluir} não foi encontrado no estoque.")

        novoiten = input("\nDeseja excluir um novo item? (sim/não): ").lower()

        if novoiten != 'sim':
            print(listaEstoque)
            break

    # Relatório dos itens excluídos
    print("-----------------------------\n")
    print("Itens excluídos:")
    for item in itens_excluidos:
        print("Código:", item["codigo"], "     ", "Saldo:", item["saldo"], "\n")
    print("\n-----------------------------\n")

    # Voltar para o menu principal (sisloja)
    voltar = int(input("Tecle 0 para retornar à tela principal: "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal: "))
    else:
        return listaEstoque





def alterar(listaEstoque):
    print(listaEstoque)
    print("-----------------------------")
    print("Opção selecionada: alterar item\n")
    while True:
        cod_item_alterar = input("Código do item a ser alterado: ")
        print("\n-----------------------------\n")

        item_alterado = None
        for item in listaEstoque:
            if item["codigo"] == cod_item_alterar:
                item_alterado = item
                break

        if item_alterado is not None: 
            print("Item encontrado:")
            print("Código:", item_alterado["codigo"])
            print("Descrição:", item_alterado["descricao"])
            print("Valor:", item_alterado["valor"])
            print("Saldo:", item_alterado["saldo"])
            print("\n")

            nova_descricao = input("Digite a nova descrição do item: ")
            novo_valor = float(input("Digite o novo valor do item: "))
            novo_saldo = int(input("Digite o novo saldo em estoque: "))

            item_alterado["descricao"] = nova_descricao
            item_alterado["valor"] = novo_valor
            item_alterado["saldo"] = novo_saldo

            print("O item foi alterado com sucesso!")
            print("-----------------------------\n")

        else:
            print(f"O item {cod_item_alterar} não foi encontrado no estoque.")

        novo_item = input("\nDeseja alterar outro item? (sim/não): ").lower()
        if novo_item != 'sim':
            break

    # Relatório dos itens alterados
    print("-----------------------------\n")
    print("Itens alterados:")
    for item in listaEstoque:
        print("Código:", item["codigo"], "     ", "Descrição:", item["descricao"], "     ", "Valor:", item["valor"], "     ","Saldo:", item["saldo"], "\n")
        print("\n-----------------------------\n")

    # Voltar para o menu principal (sisloja)
    voltar = int(input("Tecle 0 para retornar à tela principal: "))
    if voltar != 0:
        print("Ação inválida")
        voltar = int(input("Tecle 0 para voltar ao menu principal: "))
    else:
        return listaEstoque


from main import sisloja

#Alex Euzebio (202301134358) TA
#Emily Fernandes (@02303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA
