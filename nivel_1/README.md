Sistema de PDV (Ponto de Venda) - Nível 1

O que o código faz:

O programa funciona como um sistema de caixa que registra múltiplas vendas em sequência, calcula descontos automaticamente baseado na idade do cliente e no valor da compra, exibindo um resumo do relatório financeiro ao encerrar o expediente.

Como ele funciona: 
1 -> O porgrama inicia um laço de repetiçao contínuo pedindo o valor da compra
2 -> Ele verifica se o valor é negativo, e se for ele exibe uma mensagem de erro e pede pra inserir o valor novamente
3 -> Se você colocar "0", o programa vai encerrar e mostrar o resumo
4 -> Ele solicita a idade do cliente e valida se é negativo ou nao, se for negativo, pede novamente pra inserir
5 -> Regra 1 (Idade) -> Vai verificar se a idade é maior ou igual a 65 anos, se nao for nao aplica nada, se for, da 20% de desconto no valor que voce inseriu
6 -> Regra 2 (Valor) -> Vai verificar se o valor (considerando o desconto da idade, se houver) é maior do que 100 para aplicar um desconto extra de 10%
7 -> Guarda o par "valor_original" e "valor_final" dentro da lista "compras" usando ".append()" e exibe o valor final daquela venda na tela
8 -> Quando encerrar com "0", vai percorrer a lista "compras" com um laço for para contar a quantidade de vendas, somar o total bruto e calcular o total de descontos concedidos, exibindo o final total do dia ;)

Execução: 

Pra voce executar, rode:
python pdv.py