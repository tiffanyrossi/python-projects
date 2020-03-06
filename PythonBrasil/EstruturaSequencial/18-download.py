MB = int(input("Informe o tamanho do arquivo (em MB): "))
Mbps = int(input("Informe a velocidade da internet (em Mbps): "))

segundos = round(MB / (Mbps / 8))

if segundos < 60:
    print(f"O seu download será concluído em aproximadamente {segundos} segundos.")
else:
    minutos = round(segundos / 60)
    print(f"O seu download será concluído em aproximadamente {minutos} minutos.")
