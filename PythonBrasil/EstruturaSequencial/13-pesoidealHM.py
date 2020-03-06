h = float(input("Qual a sua altura? "))
g = (input("Qual o seu gênero? Responda com F ou M: "))


if g == "H":
    p = (72.7 * h) - 58
    print("Seu peso ideal é", p,"kg.")
else:
    p = (62.1 * h) - 44.7
    print("Seu peso ideal é", p,"kg.")
