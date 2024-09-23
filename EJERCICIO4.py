# Ejercicio  4: 
# Gestión de Inventario de Instrumentos Musicales
# La fábrica tiene una lista de sucursales, cada una con su nombre y una lista de instrumentos a la
# venta. De cada instrumento se conoce el ID alfanumérico, precio y tipo (Percusión, Viento o
# Cuerda).
# Requisitos:
# 1. Método listarInstrumentos(): Mostrar todos los datos de cada instrumento en la consola.
# 2. Método instrumentosPorTipo(tipo): Devolver una lista de instrumentos cuyo tipo coincida
# con el parámetro tipo.
# 3. Método borrarInstrumento(id): Recibir un ID y eliminar el instrumento asociado de la
# sucursal correspondiente.
# 4. Método porcInstrumentosPorTipo(sucursal): Recibir el nombre de una sucursal y retornar
# los porcentajes de instrumentos por tipo

class Sucursal:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.instrumentos = instrumentos  
    
    def listarInstrumentos(self):
        print(f"\nInstrumentos en la sucursal {self.nombre}:")
        for instrumento in self.instrumentos:
            print(f"ID: {instrumento['id']}, Precio: {instrumento['precio']}, Tipo: {instrumento['tipo']}")
    
    def instrumentosPorTipo(self, tipo):
        return [inst for inst in self.instrumentos if inst['tipo'].lower() == tipo.lower()]
    
    def borrarInstrumento(self, id_instrumento):
        self.instrumentos = [inst for inst in self.instrumentos if inst['id'] != id_instrumento]
    
    def porcInstrumentosPorTipo(self):
        total = len(self.instrumentos)
        if total == 0:
            return "No hay instrumentos en la sucursal"
        tipos = {'percusión': 0, 'viento': 0, 'cuerda': 0}
        for inst in self.instrumentos:
            if inst['tipo'] in tipos:
                tipos[inst['tipo']] += 1
        porcentajes = {tipo: (cantidad / total) * 100 for tipo, cantidad in tipos.items()}
        return porcentajes

sucursales = []

while True:
    nombreSucursal = input("Ingrese el nombre de la Sucursal: ")
    instrumentos = []  
    
    while True:
        id = input("Ingrese el ID del instrumento: ")
        precio = input("Ingrese el precio: ")
        tipo = input("Ingrese el tipo de instrumento [Percusión | Viento | Cuerda]: ").lower()
        while tipo not in ["percusión", "viento", "cuerda"]:
            tipo = input("Tipo inválido. Ingrese el tipo de instrumento [Percusión | Viento | Cuerda]: ").lower()
        instrumento = {"id": id, "precio": precio, "tipo": tipo}
        instrumentos.append(instrumento)
        continuar = input(f"¿Desea cargar otro instrumento en la sucursal {nombreSucursal}? [s/n]: ").lower()
        if continuar != 's':
            break
    sucursal = Sucursal(nombreSucursal, instrumentos)
    sucursales.append(sucursal)
    opcion = input("¿Desea cargar instrumentos en otra sucursal? [s/n]: ").lower()
    if opcion != 's':
        break
print("\nInformación de las sucursales:")
for sucursal in sucursales:
    sucursal.listarInstrumentos()

            
