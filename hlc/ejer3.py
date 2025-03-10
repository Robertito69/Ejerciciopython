'''
La función filter() comprueba que los elementos de una serie (ej. una lista) cumplen una condición, 
y devuelve un iterador compuesto por tales elementos.
'''

lista_numerica = [17, -24, 7, 40, -23, 51, 70, 82, -96, 102]

# (1) Filtro que selecciona los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numerica))
print(f"Números pares: {numeros_pares}")

# (2) Filtro que selecciona los números pares mayores a 0
numeros_pares_positivos = list(filter(lambda x: x % 2 == 0 and x > 0, lista_numerica))
print(f"Números pares positivos: {numeros_pares_positivos}")

# Mensaje con tu nombre
print("Hecho por: Roberto Linares Camarero")
