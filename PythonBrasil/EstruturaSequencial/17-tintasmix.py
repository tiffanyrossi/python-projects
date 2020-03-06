import math

m2 = float(input("Digite o valor em m² da área total a ser pintada: "))

litros = m2 / 6
litros_sobra = litros + ((litros / 100) * 10)

latas = math.ceil(litros_sobra / 18)
valor_latas = latas * 80.00

print(f"Caso o cliente compre apenas latas de 18 litros, serão necessárias {latas} latas, no valor total de R${valor_latas}.")

galoes = math.ceil(litros_sobra / 3.6)
valor_galoes = galoes * 25.00

print(f"Caso o cliente compre apenas galões de 3.6 litros, serão necessários {galoes} galões, no valor total de R${valor_galoes}.")

latas_mix = int(litros_sobra // 18)
galoes_mix = math.ceil((litros_sobra % 18) / 3.6)

valor_mix = (galoes_mix * 25.00) + (latas_mix * 80.00)

print(f"Caso o cliente queria comprar um mix de galões e latas, serão necessários {latas_mix} latas e {galoes_mix} galões, no valor total de R${valor_mix}.")
