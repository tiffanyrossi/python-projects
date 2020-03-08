letra = input("Digite uma letra: ")
letra = (letra.upper())

if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
