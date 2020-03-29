turno = input("Qual seu turno? Digite M = Matutino, V = Vespertino, N = Noturno: ")
turno = (turno.upper())

if turno == "M":
    print("Bom dia!")
else:
    if turno == "V":
        print("Boa tarde!")
    else:
        if turno == "N":
            print("Boa noite!")
        else:
            print("Valor inválido!")
