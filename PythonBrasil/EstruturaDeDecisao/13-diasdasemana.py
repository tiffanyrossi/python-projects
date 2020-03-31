numero = int(input("Digite um número: "))

if numero == 1:
    dia = "Domingo"
if numero == 2:
    dia = "Segunda"
if numero == 3:
    dia = "Terça"
if numero == 4:
    dia = "Quarta"
if numero == 5:
    dia = "Quinta"
if numero == 6:
    dia = "Sexta"
if numero == 7:
    dia = "Sábado"
if numero > 7:
    dia = "Valor inválido"
    
print(f"{dia}")