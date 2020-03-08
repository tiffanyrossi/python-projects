p1 = float(input("Digite o preço do produto 1: "))
p2 = float(input("Digite o preço do produto 2: "))
p3 = float(input("Digite o preço do produto 3: "))

if p1 < p2 and p1 < p3:
    print(f"Você deve comprar o produto 1.")
else:
    if p2 < p1 and p2 < p3:
        print(f"Você deve comprar o produto 2.")
    else:
        print(f"Você deve comprar o produto 3.")
