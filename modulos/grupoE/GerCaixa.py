#Alunos / Matrícula:
#Guilherme Vallim Araujo / 202303551622: TA
#Gustavo Pessanha Rezende / 202303488467: TA
#Pedro Henrique Abdalla Ramos / 202304077754: TA
#Victor Alvarenga Hwang / 202208766005: TA
#Gabriel Mendonça de Medeiros / 202302855458: TA
#Gabriela Borsoi Cohen / 202208431021: TP


class Venda:
    def __init__(self, data, codigo_cliente, codigo_item, quantidade):
        self.data = data
        self.codigo_cliente = codigo_cliente
        self.codigo_item = codigo_item
        self.quantidade = quantidade

class Caixa:
    def __init__(self):
        self.vendas = []  # Inicializa a lista de vendas vazia

    def cadastrar_venda(self, data, codigo_cliente, codigo_item, quantidade):
        venda = Venda(data, codigo_cliente, codigo_item, quantidade)
        self.vendas.append(venda)  # Adiciona a venda à lista de vendas

    def calcular_quantidade_vendida(self, data):
        quantidade_total = 0
        for venda in self.vendas:
            if venda.data == data:
                quantidade_total += venda.quantidade  # Soma a quantidade de vendas para a data especificada
        return quantidade_total

    def calcular_saldo(self):
        saldo = 0
        for venda in self.vendas:
            saldo += venda.quantidade  # Considerando o valor unitário dos itens como 1 para simplificar
        return saldo

    def calcular_valor_medio_vendas(self):
        if not self.vendas:
            return 0
        valor_total_vendas = sum(venda.quantidade for venda in self.vendas)
        valor_medio = self.calcular_saldo() / len(self.vendas)  # Calcula o valor médio das vendas
        return valor_medio

    def exibir_relatorio_movimentacao(self, data):
        saldo = self.calcular_saldo()
        valor_medio = self.calcular_valor_medio_vendas()
        total_vendas = self.calcular_quantidade_vendida(data)

        # Exibe o cabeçalho do relatório de movimentação
        print("----------------------------------------------------------")
        print("RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA")
        print(f"Data da movimentação: {data}")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Valor médio das vendas: R$ {valor_medio:.2f}")
        print(f"Total das vendas: {total_vendas} unidades")
        print("----------------------------------------------------------")

        input("Teclar 0 para retornar à tela principal")

    def exibir_tela_principal(self):
        while True:
          # Solicita os dados da venda para cadastrar
            print("-------- TELA PRINCIPAL --------")
            print("1. Cadastrar venda")
            print("2. Gerar relatório de movimentação")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                # Solicita os dados da venda para cadastrar
                data_venda = input("Digite a data da venda: ")
                codigo_cliente = input("Digite o código do cliente: ")
                codigo_item = input("Digite o código do item: ")
                quantidade = int(input("Digite a quantidade: "))

                # Chama o método cadastrar_venda para adicionar a venda à lista de vendas
                self.cadastrar_venda(data_venda, codigo_cliente, codigo_item, quantidade)
                print("Venda cadastrada com sucesso!")

            elif opcao == "2":
                # Solicita a data para gerar o relatório de movimentação
                data_relatorio = input("Digite a data para gerar o relatório: ")

                # Chama o método exibir_relatorio_movimentacao para exibir o relatório
                self.exibir_relatorio_movimentacao(data_relatorio)

            elif opcao == "0":
                # Sai do loop e encerra o programa
                break

            else:
                print("Opção inválida. Por favor, escolha novamente.")


# Exemplo de uso
caixa = Caixa()
caixa.exibir_tela_principal()
