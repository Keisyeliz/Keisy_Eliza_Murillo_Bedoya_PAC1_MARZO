
while True:
    temperaturaFlt = float(input("Ingrese una temperatura: "))
    var_unidad = input("Ingrese la unidad de medida (C/F): ")
    
    if var_unidad== "C":
        fahrenheit = (temperaturaFlt * 9/5) + 32
        print('La temperatura',temperaturaFlt,'°C', 'equivale a :', fahrenheit,'°F')

    elif var_unidad== "F":
        celsius = (temperaturaFlt - 32) * 5/9
        print('La temperatura ',temperaturaFlt,'°F', 'equivale a ',celsius,'°C')
    else:
        print('Unidad de medida inválida')
    print('Proceso finalizado')
