#algortimo para definir 2 variables 
valor_compra=int(input("Digite el valor para la valor_compra: "))
descuesto=0.05 
print("valor de la compra es: ",valor_compra)

valor_descuento= valor_compra*descuesto
print("el descuento de la compra es: ",valor_descuento)

valor_total= valor_compra-(valor_compra*descuesto)
print("el valor total despues de aplicar el descuento: ",valor_total)