ipi = float(input("Digite a porcentagem do IPI: "))
codigo1 = int(input("Digite o código da peça 1: "))
valor1 = float(input("Digite o valor unitário da peça 1: "))
quant1 = int(input("Digite a quantidade de peças 1: "))
codigo2 = int(input("Digite o código da peça 2: "))
valor2 = float(input("Digite o valor unitário da peça 2: "))
quant2 = int(input("Digite a quantidade de peças 2: "))

total = (valor1 * quant1 + valor2 * quant2) * (ipi / 100 + 1)

print("Valor total a ser pago:", total)