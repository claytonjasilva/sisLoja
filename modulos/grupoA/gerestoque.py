import os

itens_excluidos = [] #Inicializa uma lista para o relatorio de itens excluidos
    
def menu_estoque(listaEstoque):
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa o console
    adicionados = 0
    
    print("-----------------------------\n")
    print("GERENCIAMENTO DE ESTOQUE")
    print("Escolha a opção desejada: \n")
    print("Incluir itens (1)\n")
    print("Excluir itens (2)\n")
    print("-----------------------------\n")
    estoque = int(input("O que deseja fazer? "))
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa o console

    if estoque == 1:
        adicionados = 0
        somadosvalores=0
        print("-----------------------------\n")
        print("Opção selecionada: incluir itens\n")
        numitens = int(input("Quantos itens serão inclusos ao estoque? "))
        #faz serem adicionados a quantidade de diferentes itens solicitada
        while adicionados < numitens:
            print("\n-----------------------------\n")
            #Pergunta o codigo do item e verifica se é valido
            cod_item = int(input("Código do item: "))
            while cod_item > 100 or cod_item < 30:
              print ("CODIGO INVÁLIDO")
              cod_item = int(input("Código do item: "))
            print ("CODIGO VÁLIDO")
            #Pergunta os demais parametros necessarios para o relatorio
            desc_item = str(input("Digite uma breve descrição do item: "))
            saldo = int(input("Quantos desse item serão adicionados ao estoque: "))
            valor_item = float(input("Digite o valor do item: "))
            # Cria uma variavel para armazenar todas as informaçoes anteriormente informadas
            estoque_item = {"numItens": numitens,
                            "codigo": cod_item,
                            "descricao": desc_item,
                            "saldo": saldo,
                            "valor": valor_item
                                              }
            #adciona a variavel com todas as informaçoes na lista Estoque
            listaEstoque.append(estoque_item)
            #Determina o total dos valores dos itens inclusos 
            somadosvalores = somadosvalores + valor_item
            adicionados += 1
        print("\n-----------------------------\n")
        print("Os itens foram adicionados com sucesso!\n")
        print("-" * 30, "\n")
        #Media do valor dos itens 
        media =  somadosvalores / adicionados
        # Encontrar o item de maior valor
        cod_maior_valor = ""
        maior_valor = 0
        for item in listaEstoque:
            if item["valor"] > maior_valor:
                maior_valor = item["valor"]
                cod_maior_valor = item["codigo"]

        #Interface do relatorio dos itens
        print("O item de maior valor é o de código:", cod_maior_valor)
        print ("e seu valor é de", maior_valor)
        print("\n")
        print("A media de valor dos itens adicionados é:", media, "\n")
        print("-" * 30, "\n")
        voltar = int(input("Tecle 0 para retornar à tela principal "))
        if voltar != 0:
            print("Ação inválida")
            voltar = int(input("Tecle 0 para voltar ao menu principal"))

    elif estoque == 2:
        print("-----------------------------")
        print("Opção selecionada: excluir itens\n")
    
        itens_excluidos = [] #limpa a lista de itens excluidos
        while True:
            cod_item_excluir = int(input("Código do item a ser excluído: "))
            print("\n-----------------------------\n")
            print("\nTem certeza que deseja excluir esse item? \n")
            resp = str(input("Digite sim ou não: ")).lower()
    
            if resp == 'sim':
                indice_item = -1
                for i, item in enumerate(listaEstoque):
                    if item["codigo"] == cod_item_excluir:
                        indice_item = i
                if indice_item != -1:
                    item_excluido = listaEstoque.pop(indice_item)
                    itens_excluidos.append(item_excluido)
                    print(f"O item {cod_item_excluir} foi excluído com sucesso!")
                else:
                    print(f"O item {cod_item_excluir} não foi encontrado no estoque.")
     
                novoiten = str(input("\nDeseja excluir um novo item? (sim/não): ")).lower()
    
                while novoiten == "sim":
                    cod_item_excluir = int(input("Código do item a ser excluído: "))
                    print("Tem certeza que deseja excluir esse item?", cod_item_excluir)
                    resp = str(input("Digite sim ou não: ")).lower()
    
                    if resp == 'sim':
                        indice_item = -1
                        for i, item in enumerate(listaEstoque):
                            if item["codigo"] == cod_item_excluir:
                                indice_item = i
                        if indice_item != -1:
                            item_excluido = listaEstoque.pop(indice_item)
                            itens_excluidos.append(item_excluido)
                            print(f"O item {cod_item_excluir} foi excluído com sucesso!")
                        else:
                            print(f"O item {cod_item_excluir} não foi encontrado no estoque.")
        
                        novoiten = str(input("Deseja excluir um novo item? (sim/não): ")).lower()
                    elif resp == 'não':
                        novoiten = 'não'
                    else:
                        print("Opção inválida! Digite 'sim' ou 'não'.")
                        novoiten = str(input("Deseja excluir um novo item? (sim/não): ")).lower()
            elif resp == 'nao':
              break
            else:
              return
            #Relatorio dos itens excluidos
            print("-----------------------------\n")
            print("Itens excluídos:")
            for item in itens_excluidos:
                print("Código:", item["codigo"],"     ","Saldo:", item["saldo"],"\n")
            print("\n-----------------------------\n")
            break
        #Voltar para o menu principal (sisloja)
        voltar = int(input("Tecle 0 para retornar à tela principal: "))
        if voltar != 0:
          print("Ação inválida")
          voltar = int(input("Tecle 0 para voltar ao menu principal: "))
        else:
          from main import sisloja

#Alex Euzebio (202301134358) TA
#Emily Fernandes (@02303146681) TA
#Erik Marcio Fernandes (202301135745) TA
#Guilherme Duran Duran Gea (202302447171) TA
#Maria Castello (202303180391) TA
#Pedro Augusto Beserra da Silva (202304222223) TA