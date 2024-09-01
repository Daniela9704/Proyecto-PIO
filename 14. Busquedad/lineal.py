def busquedad_lineal(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return "Dato no encontrado"
    

#ejemplo lista
lista = [5,8,2,1,4,7,3,6,9]
x = 5
resultado = busquedad_lineal(lista,x)
print(f"Elementos encontrados en el indice: {resultado}")