import pytest
import aplicacion as ar

array = [5,3,4,2,1]
diccionario = [
    {"nombre":"Nazareth","edad":21},
    {"nombre":"Yulissa","edad":16},
    {"nombre":"Mariel","edad":30}]

def test_pruebas():
    assert ar.acomodo(array) == [1,2,3,4,5]

def test_contar_mayores():
    assert ar.contar_mayores(diccionario) == 2