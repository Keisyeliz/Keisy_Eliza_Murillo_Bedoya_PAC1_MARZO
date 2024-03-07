# Diccionario para almacenar la cantidad de productos por categoría
productos_por_categoria = {
   "Ferretería": 0,
   "Aseo": 0,
   "Seguridad": 0,
   "Alimentos": 0,
   "Electrodomésticos": 0
}

# Diccionario para almacenar los descuentos por categoría
descuentos = {
   "Ferretería": 0.1,
   "Aseo": 0.05,
   "Seguridad": 0.15,
   "Alimentos": 0.08,
   "Electrodomésticos": 0.12
}

total_recaudado = 0

while True:
   categoria = input("Ingrese la categoría del producto (Ferretería, Aseo, Seguridad, Alimentos, Electrodomésticos) o 'TERMINAR' para finalizar: ").capitalize()

   if categoria == "Terminar":
       break

   if categoria not in productos_por_categoria:
       print("Categoría inválida. Inténtelo nuevamente.")
       continue

   precio = float(input("Ingrese el precio del producto: "))

   descuento = descuentos[categoria]
   precio_con_descuento = precio - (precio * descuento)

   productos_por_categoria[categoria] += 1
   total_recaudado += precio_con_descuento

   print(f"El precio final con descuento es: {precio_con_descuento:.2f}")

print("\nResumen de Ventas:")
for categoria, cantidad in productos_por_categoria.items():
   print(f"Cantidad de productos de {categoria}: {cantidad}")

print(f"\nTotal recaudado: {total_recaudado:.2f}")