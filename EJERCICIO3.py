# Ejercicio  3: 
# Registro de Información en un Diccionario.
# Requisitos:
# 1. Solicitar al usuario que ingrese los siguientes datos: nombre, edad, dirección y teléfono.
# 2. Almacenar los datos en un diccionario llamado usuario_info.
# 3. Permitir el ingreso de información para varios usuarios.
# 4. Mostrar la información ingresada para cada usuario en formato clave-valor.

usuarios_info = []  
while True:
    nombre = input("Ingrese un nombre: ")
    edad = input("Ingrese una edad: ")
    direccion = input("Ingrese una dirección: ")
    telefono = input("Ingrese un teléfono: ")
    usuario_info = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
    usuarios_info.append(usuario_info)
    print(usuario_info)
    x = input("¿Desea agregar otro usuario? [s/n]: ").lower()
    if x != "s":
        break
print("\nInformación de todos los usuarios:")
for usuario in usuarios_info:
    print(usuario)
