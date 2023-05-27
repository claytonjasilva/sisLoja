# Observações Gerais

## 1. Em relação à submissão
1. Prazos cumpridos
2. **Excluir** os arquivos que não fazem parte da entrega do repositório

## 2. Observações gerais
1. Uso adequado dos arquivos, criados como módulos específicos das das funcionalidades
2. Uso adequado dos comentários, facilitando a compreensão, consequentemente do código elaborado
3. Modulrização do código utilizando funções muito boa. A única sugestão é no sentido de separar módulos de entrada de dados,   
dos módulos de processamento. Por exemplo, seria mais fácil de manter o código se no módulo `gerestoque.py` fosse criada uma função para  
incluir uma função para incluir separa da função para exluir, assim por diante.  

## 3. Funcionalidades
### 3.1 Módulo GerCaixa
1. A funcionalidade de `verificação do código` deve ser corrigida. O pedido é de que  
"códigos válidos possuem a soma dos dígitos superior a 30 e inferior a 100".  
A implementação é de número de código superior a 100 e inferior a 30.
2. Quanto à funcionalidade de `exclusão de item`. Após um item ser criado com uma quantidade armazenada em estoque,  
a quantidade deve ser reduzida até 0, em cada exclusão. Se o usuário tentar excluir um item com 0 de estoque o sistema deve apresentar  
a mensagem “NÃO HÁ SALDO EM ESTOQUE”.  
3. Não observei outros desvios de funcionalidade.
### 3.2 Módulo GerCliente
1. Seria interessante não permitir cadastro de cpf iguais. O sistema não está fazendo a filtragem.
2. Não observei outros desvios de funcionalidade.



