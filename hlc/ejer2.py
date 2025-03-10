''' Función map() y lambda. '''

# Enteros de 0 a 4
lista_numerica = [x for x in range(5)]

# (1) Con map() y lambda creamos una nueva lista de potencias de 2 elevado a los exponentes de lista_numerica
lista_cuadrados = list(map(lambda x: 2 ** x, lista_numerica))

print(f"Lista de potencias de 2: {lista_cuadrados}")

# (2) Con lambda elevamos al cuadrado cada elemento de lista_cuadrados
lista_al_cuadrado = list(map(lambda x: x ** 2, lista_cuadrados))

print(f"Lista elevada al cuadrado: {lista_al_cuadrado}")

# Mensaje con tu nombre
print("Hechopor: Roberto Linares Camarero")
