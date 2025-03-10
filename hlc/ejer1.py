# (1) Función lambda que calcula el área de un triángulo
area_triangulo = lambda base, altura: (base * altura) / 2

# (2) Función lambda que calcula el cubo de un número entero
al_cubo = lambda numero: numero ** 3

# (3) Función lambda que modifica la salida de una cadena (string)
destacar_valor = lambda valor: f"¡{valor}!"

# Valores de prueba
base = 10
altura = 5
numero = 3
comision_empleado_1 = 15500

# Imprimir resultados de cada función
print(f"Área del triángulo con base {base} y altura {altura}: {area_triangulo(base, altura)}")
print(f"El cubo de {numero} es: {al_cubo(numero)}")
print(f"Comisión destacada: {destacar_valor(comision_empleado_1)}")

# Mensaje con tu nombre
print("Código desarrollado por: Roberto Linares Camarero")
