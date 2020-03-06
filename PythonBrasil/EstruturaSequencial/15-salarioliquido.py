valorhora = float(input("Digite o valor da sua hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))

salariobruto = valorhora * horas

IR = (salariobruto / 100) * 11
INSS = (salariobruto / 100) * 8
sindicato = (salariobruto / 100) * 5

descontos = IR + INSS + sindicato

salarioliquido = salariobruto - descontos

print(f"O valor do seu salário bruto é de R${salariobruto}.")
print(f"O valor pago ao INSS é de R${INSS}.")
print(f"O valor pago ao sindicato é de R${sindicato}.")
print(f"O valor do seu salário líquido é de R${salarioliquido}. Você teve R${descontos} de descontos esse mês.")
