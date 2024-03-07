import os
os.system('cls')


total_A = 0
total_E = 0
total_I = 0
total_O = 0
total_U = 0

var_controlBln = True
while var_controlBln ==True:
    os.system('cls')
    var_opcionStr = int(input('---MENÚ DE OPCIONES---\n\n1. A\n2. E\n3. I\n4. O\n5. U\n6. Finalizar\n-> '))
    if var_opcionStr >= 1 and var_opcionStr <= 5:
        var_cantidadInt = int(input('Ingrese la cantidad->'))
        
    if var_opcionStr == 1:
        total_A = var_cantidadInt
        
    if var_opcionStr == 2:
        total_E = var_cantidadInt
    
    if var_opcionStr ==3:
        total_I =  var_cantidadInt
        
    if var_opcionStr  == 4:
        total_O = var_cantidadInt
        
    if var_opcionStr == 5:
        total_U = var_cantidadInt
        
    if var_opcionStr == 6:
        
            print('<<<<CONTEO>>>>')
            
            print('La cantidad de "A" son: ', total_A)
            print('La cantidad de "E" son: ', total_E)
            print('La cantidad de "I" son: ', total_I)
            print('La cantidad de "O" son: ', total_O)
            print('La cantidad de "U" son: ', total_U)
            var_controlBln = False
          