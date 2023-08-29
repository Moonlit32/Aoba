Bolsa = float(input("Insira o preço da bolsa"))

Vista = Bolsa - (Bolsa/10)
PorDois = Bolsa / 2
DezVezes = (Bolsa/10) + (Bolsa/20)

print("O Valor base da bolsa é", Bolsa, "À Vista, ela custa", Vista, "Reais. Em duas vezes sem juros, ela custa duas parcelas de", PorDois, "Reais. Em dez vezes com um juros de 5%, são 10 parcelas de ", DezVezes, "reais por parcela.")