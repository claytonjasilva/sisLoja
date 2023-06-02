# Observações Gerais

## 1. Em relação à submissão
1. Prazos cumpridos

## 2. Observações gerais
1. Uso adequado dos arquivos, criados como módulos específicos das funcionalidades
2. Bom uso de comentários. Comnentários facilitam a compreensão, consequentemente manutenção do código elaborado
3. Boa modularização do código utilizando funções.  

## 3. Funcionalidades
### 3.1 Módulo GerEstoque
1. A funcionalidade de exclusão está adequada.
2. A funcionalidade de exclusão não considera os lançamentos efetuados. Seria importante uma mensagem de que não há itens em estoque,
ou de que o tiem não está cadastrado.
3. Quanto à funcionalidade de `exclusão de item`. Após um item ser criado com uma quantidade armazenada em estoque,  
a quantidade deve ser reduzida até 0, em cada exclusão. Se o usuário tentar excluir um item com 0 de estoque o sistema deve apresentar  
a mensagem “NÃO HÁ SALDO EM ESTOQUE”.  
3. Não observei outros desvios de funcionalidade.
### 3.2 Módulo GerCliente
1. Seria interessante não permitir cadastro de cpf iguais. O sistema não está fazendo a filtragem.
2. Não observei outros desvios de funcionalidade.
### 3.3 Módulo GerCaixa
1. Não está lendo o número de compras para cpf válido.



