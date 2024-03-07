
numeroInt = int(input('Ingresa un número entero positivo: '))

if numeroInt <= 0:
    print('El número ingresado debe ser positivo. Intenta nuevamente.')
else:
    print('Tabla de multiplicar del: ',numeroInt)
    for i in range(1, 11):
        resultado = numeroInt * i
        print(f"{numeroInt} x {i} = {resultado}")