def acomodo(array):
    array.sort()
    return array

def contar_mayores(diccionario):
    count = 0
    for i in diccionario:
        if i.get("edad") < 18:
            pass
        else:
            count = count+1
    print("Existen: ",count," mayores de edad registrados")
    return count