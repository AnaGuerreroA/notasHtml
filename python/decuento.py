
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el descuento del producto: "))

#create method that calculate the discount of a product list and show the final price
def calculaDescuento(lista):
    for i in lista:
        print("El precio final del producto es: ", aplicaDescuento(i[0], i[1]))
        
def aplicaDescuento(precio, descuento):
    precio_final = precio - (precio * (descuento / 100))
    return precio_final

precio_final = aplicaDescuento(precio, descuento)
print("El precio final es: ", precio_final)

