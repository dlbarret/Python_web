# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:44:50 2024

@author: LENOVO
"""

import random
import mysql.connector
from mysql.connector import Error

censo = []
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOUAEOI"
numero = 0

print("Creando censo...")

for i in range(500_000):
	aumento = random.randint(1,2)
	numero += aumento

	letras = random.sample(alfabeto, 5)
	nombre = "".join(letras)

	edad = random.randint(18,99)

	impuestos = random.choice((True, True, True, False))

	censo.append([numero, nombre, edad, impuestos])

	if len(censo) % 100_000 == 0:
		print("Creados", len(censo), "registros")

print("Censo creado.")
print("Ultimo registro: ", censo[-1])

def busqueda_numero(lista, elemento):
	'''Busca registros por numero. Busqueda binaria'''

	inicio = 0
	final = len(lista) - 1

	while inicio <= final:
		medio = (inicio + final) // 2
		if lista[medio][0] == elemento:
			return lista[medio]
		elif lista[medio][0] < elemento:
			inicio = medio + 1
		elif lista[medio][0] > elemento:
			final = medio - 1
	return None

def busqueda_nombre(lista, elemento):
	'''Busca registros por nombre. Busqueda lineal'''

	encontrados = []

	for registro in lista:
		if registro[1] == elemento:
			encontrados.append(registro)
	if len(encontrados) == 0:
		return None
	else:
		return encontrados

def muestra_registro(registro):

	if registro == None:
		print("No existe registro con ese dato")
	else:
		print("--------------------------------")
		print("Numero:", registro[0]) # Cedula
		print("Nombre", registro[1])
		print("Edad:", registro[2])
		print("Impuestos:", registro[3])



def menu():

	print("--------------------------")
	print("- CENSO DE POBLACION -")
	print("1. Buscar por numero")
	print("2. Buscar por nombre")
	print("3. Salir")

	opcion = ""
	while opcion not in ("1", "2", "3"):
		opcion = input("--> ")
	return opcion


while True:
	op = menu()

	if op == "1":
		try:
			numero=int(input("Introduce numero: "))
		except ValueError:
			print("Introduce un numero entero")
		else:
			registro = busqueda_numero(censo, numero)
			muestra_registro(registro)

	elif op == "2":
		nombre=input("Introduce nombre: ").upper()
		registros = busqueda_nombre(censo,nombre)
		if registros == None:
			print("No existe registro con ese dato")
		else:
			for registro in registros:
				muestra_registro(registro)

	elif op == "3":
		break


# Creacion de tabla

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host='3306',       # 'localhost' o la dirección IP del servidor MySQL
            user='root',      # Tu usuario de MySQL
            password='Laureano123*',  # Tu contraseña de MySQL
            database='Censo_2023' # El nombre de tu base de datos
        )
        return conexion
    except Error as e:
        print("Error al conectar a MySQL", e)
        return None

def crear_tabla(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Censo_2023 (
                Nombre VARCHAR(255),
                Numero INT,
                Edad INT,
                Impuestos BOOLEAN
            )
        """)
        conexion.commit()
    except Error as e:
        print("Error al crear tabla", e)

def insertar_registro(conexion, registro):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO Censo_2023 (Nombre, Numero, Edad, Impuestos) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, registro)
        conexion.commit()
    except Error as e:
        print("Error al insertar registro", e)

# Conectar a MySQL
conexion = conectar_mysql()

# Crear tabla si no existe
if conexion:
    crear_tabla(conexion)

    # Insertar registros
    for registro in censo:
        insertar_registro(conexion, registro)

    # Cerrar conexión
    conexion.close()
    
