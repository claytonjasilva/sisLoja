# Observações Gerais

## 1. Em relação à submissão
1. Prazos cumpridos

## 2. Observações gerais
1. Seria interessante interessante criar arquivos para cada funcionalidade pedida: gerEstoque.py, gerCliente.py, gerCaixa.py.  
Isso pode ser feito com o uso de arquivos contendo as funções específicas de cada funcionalidade (módulo).
2. Faltou utilizar mais comentários. Os comentários facilitam a compreensão, consequentemente a manutenção do código elaborado
3. Seria importante modularizar mais o código, utilizando funções. Também facilita a manutenção e a construção em equipe.  
Seria interessante criar funções para entrada de dados, para resolver funcionalidades distintas etc.
4. Algumas funcionalidades elaboradas não estão sendo implementadas adequadamente - seria interessante rever e testar função por função o código

## 3. Funcionalidades
### 3.1 Módulo GerCaixa
1. A funcionalidade de `verificação do código` deve ser corrigida. O pedido é de que  
"códigos válidos possuem a soma dos dígitos superior a 30 e inferior a 100".  
O número de código não está sendo verificado corretamente. Por exemplo, o código 1 é aceito.
2. Ajustar a funcionalidade de exclusão. Por exemplo, cadastrado o item de código 46, não é possível exclui-lo posteriormente.
3. Não observei outros desvios de funcionalidade.
### 3.2 Módulo GerCliente
1. Seria interessante não permitir cadastro de cpf iguais. O sistema não está fazendo a filtragem.
2. Não observei outros desvios de funcionalidade.
### 3.3 Módulo GerCaixa
1. O relatório apresentado não atende ao pedido
