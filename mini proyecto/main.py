import os

productos = [
    {"nombre": "anillo de oro", "precio": 15000, "cantidad": 10},
    {"nombre": "anillo de plata", "precio": 5000, "cantidad": 15},
    {"nombre": "collar de perlas", "precio": 70000, "cantidad": 5},
    {"nombre": "anillo de diamante", "precio": 50000, "cantidad": 8}
]

carrito = []

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux o Mac

def mostrar_mensaje_error():
    input("Opción no válida. Presiona Enter para continuar...")
    limpiar_pantalla()

def mostrar_productos():

    print("--------------------------/Menú de productos/---------------------------")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto["nombre"]} - precio ${producto["precio"]} - disponibles {producto["cantidad"]}")

def agregar_al_carrito():
    mostrar_productos()

    try:
        opcion = int(input("Seleccione el producto que desea agregar al carrito: "))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
            producto = productos[opcion-1]
            if cantidad > producto["cantidad"]:
                print("No hay suficientes existencias en stock")
            else:
                producto["cantidad"] -= cantidad
                carrito.append({"nombre": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad})
                print(f"Felicidades, has añadido {cantidad} {producto["nombre"]} exitosamente")
    except ValueError:
        print("Entrada inválida, por favor ingrese un número")
    except Exception as e:
        print(f"Se ha presentado un error: {e}")

def mostrar_carrito():
    if carrito:
        print("--------------------------/Carrito/---------------------------")
        for item in carrito:
            print(f"{item['nombre']} - precio ${item['precio']} - cantidad {item['cantidad']}")
    else:
        print("El carrito está vacío")

def finalizar_compra():
    if carrito:
        total = sum(item["precio"] * item["cantidad"] for item in carrito)
        print(f"El total de tu compra es: ${total}")
        print("Gracias por tu compra")
        carrito.clear()
    else:
        print("El carrito está vacío")

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
                break
            else:
                mostrar_mensaje_error()
        except ValueError:
            print("Entrada invalida, por favor ingrese un número")
        except Exception as e:
            print(f"Se ha presentado un error: {e}")

main()