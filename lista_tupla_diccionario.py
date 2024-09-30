# Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Zapatos", "cantidad": 3, "precio": 50.0},
    {"fecha": "2024-01-02", "producto": "Camisa", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-03", "producto": "Pantalones", "cantidad": 2, "precio": 30.0},
    {"fecha": "2024-01-04", "producto": "Sombrero", "cantidad": 4, "precio": 15.0}
]

# Cálculo de Ingresos Totales
ingresos_totales = 0.0

for venta in ventas:
    ingresos_venta = venta["cantidad"] * venta["precio"]
    ingresos_totales += ingresos_venta

print(f"Ingresos totales generados: ${ingresos_totales:.2f}")


ventas_por_producto = {}
precios_por_producto = {}
ingresos_por_dia = {}

# Calcular la cantidad total vendida por producto
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio_unitario = venta["precio"]
    fecha = venta["fecha"]
     # Actualizar cantidad vendida por producto
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad
    # Actualizar precios por producto
    if producto in precios_por_producto:
        total_precio, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (total_precio + (precio_unitario * cantidad), total_cantidad + cantidad)
    else:
        precios_por_producto[producto] = (precio_unitario * cantidad, cantidad)
    # Actualizar ingresos por día
    ingresos_venta = cantidad * precio_unitario
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos_venta
    else:
        ingresos_por_dia[fecha] = ingresos_venta

# Identificar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# Mostrar resultados
print("Ventas por producto:", ventas_por_producto)
print(f"El producto más vendido es '{producto_mas_vendido}' con una cantidad total de {cantidad_mas_vendida}.")

# Cálculo del precio promedio por producto
precio_promedio_por_producto = {}
for producto, (suma_precios, total_cantidad) in precios_por_producto.items():
    precio_promedio = suma_precios / total_cantidad
    precio_promedio_por_producto[producto] = precio_promedio

# Mostrar precios promedio
print("Precio promedio por producto:")
for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"{producto}: ${precio_promedio:.2f}")


# Mostrar ingresos por día
print("Ingresos por día:")
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: ${ingresos:.2f}")

