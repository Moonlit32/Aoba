Objeto1 = float(input("Insira o preço do primeiro objeto "))
Objeto2 = float(input("Insira o preço do segundo objeto "))
Objeto3 = float(input("Insira o preço do terceiro objeto "))
Objeto4 = float(input("Insira o preço do quarto objeto "))
Objeto5 = float(input("Insira o preço do quinto objeto "))

Valor = float(input("Insira o valor a ser pago"))

Soma = Objeto1 + Objeto2 + Objeto3 + Objeto4 + Objeto5
Troco = Valor - Soma

if Valor > Soma:
    print("O Total da sua compra foi de", Soma, "Reais. Pagando com", Valor, "Seu troco será de", Troco)
else: print("O Valor a ser pago é insuficiente.")
