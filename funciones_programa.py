import json 
import os
from os import system




def mostrar_nombres(lista:list) -> None:
    for el in lista :
        print (el ["nombre"], end= ", ")
        


def mostrar_nombres_altura(lista:list) -> None:
    for el in lista :
        altura = float(el["altura"])
        print (f" {el ["nombre"]} - {altura:.2f}- ", end= ", ")
        




def hero_mas_alto(lista_personajes):
    if not isinstance(lista_personajes, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    hero_alto = None
    altura_mayor = 0

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if altura > altura_mayor:
            altura_mayor = altura
            hero_alto = personaje["nombre"]

    return f"EL personaje más alto es: {hero_alto} y mide: {altura_mayor} cms"


def hero_mas_bajo(lista_personajes):
    if not isinstance(lista_personajes, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    hero_bajo = None
    altura_menor = float('inf')
    
    

    for personaje in lista_personajes:
        altura = float(personaje ["altura"])
        if altura < altura_menor:
            altura_menor = altura
            hero_bajo = personaje["nombre"]

    return f"EL personaje más bajo es: {hero_bajo} y mide: {altura_menor} cm"




def promedio_altura(lista_personajes):
    if not isinstance(lista_personajes, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    suma_alturas = 0
    cantidad_personajes = 0

    for personaje in lista_personajes:
            altura = float(personaje["altura"])
            suma_alturas += altura
            cantidad_personajes += 1

    promedio = suma_alturas / cantidad_personajes
    return f"El promedio de altura de los superhéroes es: {promedio:.2f} cm"






def hero_mas_liviano(lista_personajes):
    if not isinstance(lista_personajes, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    hero_mas_liviano = None
    peso_menor = float('inf')
    
    

    for personaje in lista_personajes:
        peso = float(personaje ["peso"])
        if peso < peso_menor:
            peso_menor = peso
            hero_mas_liviano = personaje["nombre"]

    return f"EL personaje más liviano es: {hero_mas_liviano} y pesa: {peso_menor} kilos"


def hero_mas_pesado(lista_personajes):
    if not isinstance(lista_personajes, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    hero_mas_pesado = None
    peso_mayor = 0
    
    

    for personaje in lista_personajes:
        peso = float(personaje ["peso"])
        if peso > peso_mayor:
            peso_mayor= peso
            hero_mas_pesado = personaje["nombre"]

    return f"EL personaje más pesado es: {hero_mas_pesado} y pesa: {peso_mayor} kilos"

def pausar ():
    return system("pause")

def limpiar_pantalla ():
    return system ("cls")


def menu():
    limpiar_pantalla()
    print("\nMenú Principal")
    print("1) imprime lista de superheroes ")
    print("2) imprime superheroes con su altura")
    print("3) muestra el heroe mas alto y mas bajo ")
    print("4) muestra el promedio de altura")
    print("5) muestra el superheroe mas pesado y mas liviano")
    print("6) muestra los superheroes masculinos, quien es el mas alto ,el mas bajo y el promedio de altura")
    print("7) muestra los superheroes femeninos , quien es la mas alta,la mas baja y el promedio de altura")
    print("8) muestra cuántos superhéroes tienen cada tipo de color de ojos")
    print("9) muestra cuántos superhéroes tienen cada tipo de color de pelo")
    print("10) muestra cuántos superhéroes tienen cada tipo de inteligencia")
    print("11) lista de superheroes agrupados por color de ojos ")
    print("12) lista de superheroes agrupados por color de pelo")
    print("13) lista de superheroes agrupados por inteligencia")
    print("14) salir")
    return input("Seleccione una opción: ")
    

def get_path_actual (nombre_archivo):
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)



def json_read (path: str) -> str:
    # print (path)
    with open (get_path_actual(path), "r", encoding="UTF-8") as archivo:
        contenido = json.load(archivo)
        # print (contenido)
        return contenido


