def busquedad_Binaria(lista, x):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:

        mitad = inicio + (fin - inicio) // 2

        if lista[mitad] == x:
            return mitad
        elif lista[mitad] < x:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    return "Dato no encontrado"

#ejemplo lista
lista = [1,2,3,4,5,6,7,8,9,10]
x = 9
resultado = busquedad_Binaria(lista,x)
print(f"Elementos encontrados en el indice: {resultado}")