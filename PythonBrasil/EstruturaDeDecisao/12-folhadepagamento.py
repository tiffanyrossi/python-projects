print(f"====== FOLHA DE PAGAMENTO ======")

valor = float(input("Digite o valor da sua hora de trabalho: "))
horas = float(input("Digite o número de horas trabalhadas em um mês: "))

salariobruto = valor * horas

if salariobruto <= 900:
    impostoderenda = 0
else:
    if salariobruto > 900 and salariobruto <= 1500:
        impostoderenda = 5
    else:
        if salariobruto > 1500 and salariobruto <= 2500:
            impostoderenda = 10
        else:
            impostoderenda = 2500

descontoIR = (salariobruto / 100) * impostoderenda
descontoINSS = (salariobruto / 100) * 10
valorFGTS = (salariobruto / 100) * 11

descontos = descontoIR + descontoINSS
salarioliquido = salariobruto - descontos

print(f"Salário bruto:          R${salariobruto} ")
print(f"    (-) IR (5%):        R${descontoIR}")
print(f"    (-) INSS (10%):     R${descontoINSS}")
print(f"    FGTS (11%):         R${valorFGTS}")
print(f"    Total de descontos: R${descontos}")
print(f"    Salário líquido:    R${salarioliquido}")