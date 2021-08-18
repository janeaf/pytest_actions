def Order(lista):
    print("Orden de numero enteros forma acendente")
    lista.sort()
    return lista

def EdadMayr(datos):
    print("Total de mayores de edad")
    persona = 0
    for i in datos:
        if i.get("edad") >=18:
            persona = persona +1
    
    print("Existe ", persona, "Mayor de edad")
    return persona