# Leer el valor de la compra
valor_compra = float(input("Ingrese el valor de la compra: "))

# Verificar si el valor de la compra es mayor o igual a 50.000 pesos
if valor_compra >= 50000:
    # Leer el color de la balota
    color_balota = input("Ingrese el color de la balota (roja, verde, azul, amarilla, negra): ")

    # Evaluar el color de la balota y calcular el descuento
    if color_balota == "roja":
        descuento = 0.10
    elif color_balota == "verde":
        descuento = 0.15
    elif color_balota == "azul":
        descuento = 0.20
    elif color_balota == "amarilla":
        descuento = 0.50
    elif color_balota == "negra":
        descuento = 1.00
    else:
        print("Color de balota no válido")
        descuento = 0.00

    # Calcular el valor a pagar con el descuento
    valor_descuento = valor_compra * descuento
    valor_a_pagar = valor_compra - valor_descuento

    # Imprimir el resultado
    print("Valor de la compra: $", valor_compra)
    print("Color de la balota: ", color_balota)
    print("Descuento aplicado: ", descuento * 100, "%")
    print("Valor del descuento: $", valor_descuento)
    print("Valor a pagar: $", valor_a_pagar)

else:
    print("El valor de la compra es inferior a 50.000 pesos.")
    print("Valor a pagar: $", valor_compra)