# ejercicio 1
# Validación de entrada y búsqueda en una Lista.
# Implementar un programa que valide la entrada de un número entero y verifique su presencia en
# una lista.
# Requisitos:
# 1. Solicitar al usuario que ingrese un número entero del 0 al 9.
# 2. Mientras el número ingresado no esté en el rango especificado, repetir la solicitud.
# 3. Verificar si el número se encuentra en una lista predefinida de números.
# 4. Notificar al usuario si el número está o no en la lista.
# Concepto útil: Utilizar la sintaxis [valor] in [lista] para comprobar la presencia de un valor en una
# lista.

lista = [1,3,5,7,9]
x = int(input("Ingrese un número del 0 al 9: "))
while(x<0 or x>9):
    x = int(input("Ingrese un número del 0 al 9: "))
if(x in lista):
    print(f"El número {x} se encuentra en la lista")
else:
    print(f"El número {x} se encuentra en la lista")
print(f"Lista de números: {lista}")



