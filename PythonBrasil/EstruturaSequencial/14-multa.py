print("Olá, João Papo-de-Pescador!")
peso = float(input("Quantos quilos você pescou hoje? "))

if peso <= 50:
    print("Muito bem! Sem multas hoje.")
else:
    excesso = peso - 50
    multa = excesso * 4
    print("Você pescou", excesso, "kg além do limite. O valor da multa a ser paga é de R$", multa)
