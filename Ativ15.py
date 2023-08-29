Anos = float(input("Insira quantos anos completos de vida você tem"))
Meses = float(input("Quantos meses de vida sobraram"))
Dias = float(input("Quantos dias de vida sobraram"))

Ano_Total = Anos * 365
Mes_Total = Meses * 30

Idade = Dias + Mes_Total + Ano_Total

print("Você tem", Anos, "anos, ", Meses, "meses e", Dias, "dias de idade. Convertido em dias, isso são", Idade, "dias de idade.")