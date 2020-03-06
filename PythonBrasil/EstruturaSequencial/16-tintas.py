import math

m2 = float(input("Digite o valor em m² da área total a ser pintada: "))

litros = m2 / 3
galoes = litros / 18
galoes = math.ceil(galoes)
valor = galoes * 80

print(f"Você irá precisar de {round(litros, 2)} litros para pintar uma área de {m2}m².")

if litros <= 18:
    print(f"Você irá precisar de um galão de tinta, no valor de R$80.")
else:
    print(f"Serão necessários {galoes} galões, e o valor total é de R${valor}.")
