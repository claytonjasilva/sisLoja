# sisLoja
Contempla projeto da disciplina Programação Estruturada (com uso da linguagem Python) do IBMEC RJ, no contexto da primeira Avaliação Bimestral  (AP1)

## Requisitos 

### 1. Descrição Geral

O sistema sisLoja contempla os seguintes módulos:
1. gerenciar o estoque (GerEstoque); 
2. gerenciar clientes (GerClientes); e 
3. gerenciar o fluxo de caixa (GerCaixa). 

Após o cliente escolher uma opção e realizar a operação selecionada no **módulo principal**, o sistema deverá retornar à tela inicial. 

#### 1.1 Funcionalidades do Módulo GerEstoque

O módulo GerEstoque permite que o usuário possa **incluir** ou **excluir** itens no estoque, selecionando uma das duas opções.  
Portanto, o uso do módulo GerEstoque requer dois tipos de transação:   
- inclusão de itens; ou 
- exclusão de itens.

Em uma transação para **inclusão**, o usuário **pode incluir vários itens ao estoque em uma mesma transação**, informando preliminarmente quantos itens serão incluídos.  
Para incluir cada item no estoque o usuário deverá digitar: 
1.	o código do item (cod_item) – um número inteiro; 
2.	uma descrição do item (desc_item); e
3.	o valor do item, em reais (valor_item).   

**Todos os itens deverão ser armazenados em uma lista nomeada listaEstoque**.  
Após realizada toda a transação de inclusão, **o sistema apresenta um relatório da transação com a média dos valores dos itens cadastrados; e o código do item de maior valor com o seu respectivo valor.**  

Em um acesso para **exclusão**, o usuário poderá excluir vários componentes, item por item, digitando o código do item a ser excluído.   
Após o usuário digitar o código do item a ser excluído o sistema deverá **emitir uma mensagem: “TEM CERTEZA QUE DESEJA EXCLUIR O ITEM?”.**   
Se o usuário digitar **não**, a transação será finalizada. Caso o usuário digite **sim**, o sistema deverá:
1.	verificar se o código é válido (códigos válidos possuem a soma dos dígitos superior a 30 e inferior a 100). 
2.	Se o código for inválido, o sistema deverá apresentar uma mensagem “CÓDIGO INVÁLIDO” (códigos não cadastrados devem ser tratados como códigos inválidos) e encerrar a transação; e
3.	se o código for válido, o sistema deverá ler a quantidade de itens a excluir e, se houver saldo em estoque, deverá excluir o item solicitado e apresentar uma mensagem “OPERAÇÃO REALIZADA COM SUCESSO”.
4.	Caso não haja saldo em estoque, o sistema deverá apresentar uma mensagem “NÃO HÁ SALDO EM ESTOQUE” e encerrar a transação.
5.	Após a exclusão bem sucedida de um item apresentar uma mensagem perguntando se o usuário deseja excluir um novo item. 
Após realizada toda a transação de exclusão de todos os itens, o sistema deverá apresentar um relatório com a relação dos itens excluídos e o respectivo saldo em estoque. 

