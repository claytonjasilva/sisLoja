# Observações Gerais

## 1. Observações gerais
1. Uso dos comentários poderia ser melhor, facilitando a compreensão, consequentemente manutenção do código elaborado.
2. Certificar-se o motivo pelo qual não estão conseguindo fazer o upload para o GitHub - importante!
3. Interface do menu principal atende ao pedido.
4. Seria interessante criar uma interface de orientação para o usuário, por exemplo, na mensagem    
'Você deseja incluir ou excluir um item? (1) incluir (2) excluir'
5. Teria sido interessante utilizar módulos específicos das funcionalidades.
6. Organização e modularização do código utilizando funções poderia ter sido melhor. Por exemplo, separar módulos de entrada de dados,   
dos módulos de processamento de funções.  

## 3. Funcionalidades
### 3.1 Módulo GerEstoque
1. A função de inclusão não está determinando o código inválido.
2. Após a transação de inclusão do gerenciamento do estoque a mensagem é para retornar a tela principal.
3. Ajustar a transação de exclusão - não verifica se existe saldo em estoque.
4. Além disso, testa o código do item - issodeveria ser realizado na inclusão.
### 3.2 Módulo GerCliente
1. A implementação permite cadastro de cpf iguais com rendas diferentes - ajustar.
### 3.3 Módulo GerCaixa
1. Seria inmportante apresentar um padrão para entrada de data.
2. Observe a mensagem de erro...   
`NameError: name 'tot_venda' is not defined`

