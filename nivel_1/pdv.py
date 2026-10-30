compras = []

while True:
    valor_original = float(input("Digite o valor da compra em reais (0 para encerrar): "))

    while valor_original < 0:
        print("Erro: o valor da compra não pode ser negativo.")
        valor_original = float(input("Digite o valor da compra em reais (0 para encerrar): "))

    if valor_original == 0:
        break

    idade = int(input("Digite a idade do cliente: "))

    while idade < 0:
        print("Erro: a idade não pode ser negativa.")
        idade = int(input("Digite a idade do cliente: "))

    valor_final = valor_original

    if idade >= 65:
        valor_final = valor_final * 0.80

    if valor_final > 100:
        valor_final = valor_final * 0.90

    compras.append([valor_original, valor_final])
    print("Valor final da compra: R$ {:.2f}".format(valor_final))

quantidade_compras = 0
total_bruto = 0
total_final = 0

for compra in compras:
    quantidade_compras = quantidade_compras + 1
    total_bruto = total_bruto + compra[0]
    total_final = total_final + compra[1]

total_descontos = total_bruto - total_final

print("\nResumo do dia")
print("Quantidade total de compras: {}".format(quantidade_compras))
print("Total bruto: R$ {:.2f}".format(total_bruto))
print("Total de descontos concedidos: R$ {:.2f}".format(total_descontos))
print("Total final: R$ {:.2f}".format(total_final))