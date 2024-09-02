import os

#se crea una lista con los productos de la joyeria -------- Diccionario con nombre, precio y cantidad 
productos = [
    {"nombre": "anillo de oro", "precio": 15000, "cantidad": 10},
    {"nombre": "anillo de plata", "precio": 5000, "cantidad": 15},
    {"nombre": "collar de perlas", "precio": 70000, "cantidad": 5},
    {"nombre": "anillo de diamante", "precio": 50000, "cantidad": 8}
]

carrito = []

#esta funcion sirve para mostrar los productos disponibles de la joyeria
def mostrar_productos():

    print("--------------------------/Menú de productos/---------------------------")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto["nombre"]} - Precio: ${producto["precio"]} - Disponibles: {producto["cantidad"]}")


#esta funcion sirve para agregar los productos de la lista al carrito
def agregar_al_carrito():
    mostrar_productos()
    try:
        opcion = int(input("Seleccione el número del producto que desea agregar al carrito: "))
        if 1 <= opcion <= len(productos):
            producto = productos[opcion - 1]
            #sirve para mirar si el producto esta agotado
            if producto['cantidad'] == 0:
                print(f"Lo sentimos, {producto['nombre']} está agotado.")
                return
            cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' que desea comprar: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                #sirve para mirar si la cantidad que pide el usuario es mayor a la cantidad disponible
            elif cantidad > producto['cantidad']:
                print(f"No hay suficientes existencias de {producto['nombre']}. Disponibles: {producto['cantidad']}")
            else:
                # Verificar si el producto ya está en el carrito y de ser asi solo aumenta la cantidad 
                for i in carrito:
                    if i['nombre'] == producto['nombre']:
                        i['cantidad'] += cantidad
                        print(f"Se han añadido {cantidad} unidades más de {producto['nombre']} al carrito.")
                        break
                else:
                    #agrega el producto si no estaba en el carrito
                    carrito.append({
                        "nombre": producto['nombre'],
                        "precio": producto['precio'],
                        "cantidad": cantidad
                    })
                    print(f"{cantidad} unidades de {producto['nombre']} han sido añadidas al carrito.")
        else:
            print("Opción inválida. Por favor, seleccione un número válido del menú.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")


def mostrar_carrito():
    if carrito:
        total = sum(i["precio"] * i["cantidad"] for i in carrito) #realiza el total de la compra
        print("--------------------------/Carrito/---------------------------")
        #sirve para mostrar los producto agregados al carrito
        for i in carrito:
            print(f"{i['nombre']} - precio ${i['precio']} - cantidad {i['cantidad']}")
        print(f"El total de tu compra es:  ${total}")
    else:
        print("El carrito está vacío")

#muestra los productos agregados al carrito y su total y le pregunta al usuario si desea realizar su compra o no 
def finalizar_compra():
    if carrito:
        mostrar_carrito()
        confirmacion = input("¿Desea confirmar la compra? (s/n): ").strip().lower()
        if confirmacion == 's':
            #ajusta la cantidad disponible en el inventario despues de la compra
            for i in carrito:
                for producto in productos:
                    if producto['nombre'] == i['nombre']:
                        producto['cantidad'] -= i['cantidad']
            print("compra finalizada exitosamente ¡Gracias por su compra!")
            carrito.clear()#pone el carrito en blanco para dejarlo listo para otra compra
        else:
            print("La compra ha sido cancelada")
    else:
        print("No hay productos en el carrito, Agreguelos antes de finalizar la compra.")

#menu que tiene le muestra al usuario las opciones que puede escoger para realizar su compra
def main():
    while True:   
        print("--------------------------/////---------------------------")
        print("1. Mostrar productos disponibles")
        print("2. Añadir productos al carrito")
        print("3. Mostrar carrito")
        print("4. Finalizar compra")
        print("5. Salir de la compra")

        try:

            selection = int(input("Introduce el número de la opción a la cual quieres ingresar: "))

            if selection == 1:
                mostrar_productos()
            elif selection == 2:
                agregar_al_carrito()
            elif selection == 3:
                mostrar_carrito()
            elif selection == 4:
                finalizar_compra()
            elif selection == 5:
                print("Saliendo.......")
                break
        except ValueError:
            print("Entrada invalida, por favor ingrese un número")
        except Exception as e:
            print(f"Se ha presentado un error: {e}")

main()
