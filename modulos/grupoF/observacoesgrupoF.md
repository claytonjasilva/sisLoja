# Observações Gerais

## 1. Em relação à submissão
1. Prazos cumpridos

## 2. Observações gerais
1. Faltou uma função `modulo_principal.py`. 
2. Seria interessante criar arquivos, cada um dos quais com as funções relativas às funcionalidades de gestão de caixa, de clientes e de estoque.  
3. Uso adequado dos comentários, facilitando a compreensão, consequentemente do código elaborado
4. Modularização do código utilizando funções muito boa.   
5. As interfaces não seguiram o padrão pedido.  

## 3. Funcionalidades
### 3.1 Módulo GerEstoque
1. A funcionalidade de `verificação do código` deve ser corrigida. O pedido é de que  
"códigos válidos possuem a soma dos dígitos superior a 30 e inferior a 100".  
A implementação é de número de código superior a 100 e inferior a 30.
2. Erro na função `soma_cod`. Ela sempre retorna *True*.
3. A função `incluir_item` computa os itens de código inválidos também na inclusão. Além disso, não usa recebe a quantidade de itens    
para abater na transação de exclusão. Importante utilizar aqui uma lista, outro tipo de sequência, ou dicionário.
5. Quanto à funcionalidade de `exclusão de item`. Após um item ser criado com uma quantidade armazenada em estoque,  
a quantidade deve ser reduzida até 0, em cada exclusão. Se o usuário tentar excluir um item com 0 de estoque o sistema deve apresentar  
a mensagem “NÃO HÁ SALDO EM ESTOQUE”.  
3. As opções de calcular média e encontrar o item mais caro já deve ser chamada dentro da função de `incluir_item`.
4. Não observei outros desvios de funcionalidade.
### 3.2 Módulo GerCliente
1. Seria interessante não permitir cadastro de cpf iguais. O sistema não está fazendo a filtragem.
2. Não observei outros desvios de funcionalidade.
3. De modo similar ao módulo anterior, a apresentação do relatório deve ser feita logo após o cadastro dos clientes.
### 3.3 Módulo GerCaixa
1. Seria interessante apresentar um formato desejado para a entrada de data. Por exemplo, se o usuário digita "27/05/2023", o sistema entende como data inválida.




