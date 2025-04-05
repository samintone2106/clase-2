import random

# Lista de caracteres permitidos para la contraseña
caracteres_permitidos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Solicitar la longitud de la contraseña al usuario con validación
while True:
    try:
        longitud_contrasena = int(input("Introduce la longitud de la contraseña (número entero positivo): "))
        if longitud_contrasena <= 0:
            print("Por favor, introduce un número mayor que 0.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

# Generar la contraseña
contrasena_generada = ""
for _ in range(longitud_contrasena):
    contrasena_generada += random.choice(caracteres_permitidos)

# Mostrar la contraseña generada
print("Contraseña generada:", contrasena_generada)
