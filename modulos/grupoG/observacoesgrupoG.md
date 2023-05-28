# Observações Gerais

## 1. Em relação à submissão
1. Atraso no envio por e-mail
2. As interfaces não seguiram exatamente o padrão que foi exigido
3. Os códigos não contêm os nomes dos componentes do grupo, nem a auto-avaliação

## 2. Observações gerais
1. A interface do menu principal não atende ao pedido.
2. Teria sido interessante utilizar arquivos separados para cda função - módulos específicos das funcionalidades.
3. Uso dos comentários poderia ser melhor, facilitando a compreensão, consequentemente manutenção do código elaborado.
4. Organização e modularização do código utilizando funções poderia ter sido melhor. Por exemplo, separar módulos de entrada de dados,   
dos módulos de processamento de funções.  

## 3. Funcionalidades
### 3.1 Módulo GerEstoque
1. Ajustar a transação de exclusão quando o código é inválido. Permaencer na função, solicitando o código correto - não encerrar a transação.
2. Corrigir a função de exclusão. Não está abetendo o saldo de item armazenado em estoque corretamente.
3. Não observei outros desvios de funcionalidade.
### 3.2 Módulo GerCliente
1. Muito interessante que a implementação não permite cadastro de cpf iguais.
2. Não observei outros desvios de funcionalidade.
### 3.3 Módulo GerCaixa
1. O valor do item é *float* 

