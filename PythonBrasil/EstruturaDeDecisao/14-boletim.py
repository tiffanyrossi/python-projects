print(f"====== BOLETIM ======")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

if media <= 4:
    conceito = "E"
if media > 4 and media <= 6:
    conceito = "D"
if media > 6 and media <= 7.5:
    conceito = "C"
if media > 7.5 and media <= 9:
    conceito = "B"
if media > 9:
    conceito = "A"

if conceito == "A" or conceito == "B" or conceito == "C":
    aprovacao = "APROVADO"
else:
    aprovacao = "REPROVADO"

print("------------------------")
print(f"Nota 1:     {n1}")
print(f"Nota 2:     {n2}")
print(f"Média:      {media}")
print(f"Conceito:   {conceito}")
print(f"Aprovação:  {aprovacao}")