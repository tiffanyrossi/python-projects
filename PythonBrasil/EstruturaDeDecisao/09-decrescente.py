n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
n3 = int(input("Digite um terceiro número: "))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

intermediario = n1
if n2 > menor and n2 < maior:
    intermediario = n2
if n3 > menor and n3 < maior:
    intermediario = n3

print(f"{maior}")
print(f"{intermediario}")
print(f"{menor}")

