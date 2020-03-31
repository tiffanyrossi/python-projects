lado1 = float(input("Digite a medida do menor lado: "))
lado2 = float(input("Digite a medida do maior lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

if lado1 + lado3 >= lado2:
    if lado1 == lado2 and lado2 == lado3:
            print("Triângulo equilátero")
    else:
        if lado1 == lado2 or lado2 == lado3:
                print("Triângulo isósceles")
        else:
            if lado1 != lado2 and lado2 != lado3:
                print("Triângulo escaleno")
else:
    print("Não é um triângulo.")