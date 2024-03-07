
while True:
    temperaturaFlt = float(input("Ingrese una temperatura: "))
    unidad = input("Ingrese la unidad de medida (C/F): ")

    if unidad.upper() == "C":
        fahrenheit = (temperaturaFlt * 9/5) + 32
        print(f"{temperaturaFlt}°C equivale a {fahrenheit}°F")
    elif unidad.upper() == "F":
        celsius = (temperaturaFlt - 32) * 5/9
        print(f"{temperaturaFlt}°F equivale a {celsius}°C")
    else:
        print("Unidad de medida inválida")
    print('Proceso finalizado')