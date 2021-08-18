import pytest
import app

lista = [1, 2, 3, 5, 55, 75, 9]
datos = [
	{"nombre":"Yuridia", "edad": 21},
    {"nombre":"Fatima", "edad": 21},
	{"nombre":"Avinadi", "edad": 22},
	{"nombre":"Diego", "edad": 17},
	{"nombre":"Carmen", "edad": 15},
	{"nombre":"Fernanda", "edad": 25},
	{"nombre":"Javier", "edad": 26},
	]

def test_Order():
	assert app.Orden(lista) == [1, 2, 3, 5, 55, 75, 9]

def test_MayorEdad():
	assert app.EdadMayr(datos) == 2