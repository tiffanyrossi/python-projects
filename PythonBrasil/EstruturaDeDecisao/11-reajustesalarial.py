salario = float(input("Digite o seu salário: "))

if salario <= 280:
    percentual = 20

if salario > 280 and salario <= 700:
    percentual = 15

if salario > 700 and salario <= 1500:
    percentual = 10

if salario > 1500:
    percentual = 5

aumento = (salario / 100) * percentual
novosalario = salario + aumento

print(f"Seu salário atual é R${salario}.")
print(f"O seu aumento foi de {percentual}%, totalizando R${aumento}.")
print(f"Seu salário reajustado é R${novosalario}")
