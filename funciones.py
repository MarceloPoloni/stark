from data_heroes import *


# def hero_mas_alto(lista):
#     if not isinstance(lista, list):
#         raise ValueError("ERROR | Se esperaba una lista")
    
#     hero_alto = None
#     altura_mayor = 0

#     for personaje in lista:
#         altura = float(personaje["altura"])
#         if altura > altura_mayor:
#             altura_mayor = altura
#             hero_alto = personaje["nombre"]

#     return f"EL personaje masculino mas alto es: {hero_alto} y mide: {altura_mayor} cms"


def heroe_mas_alto(lista,genero):
    if not isinstance(lista, list):
        raise ValueError("ERROR | Se esperaba una lista")
    
    hero_alto = None
    altura_mayor = 0

    for personaje in lista:
        altura = float(personaje["altura"])
        if altura > altura_mayor:
            altura_mayor = altura
            hero_alto = personaje["nombre"]

    return f"EL personaje {genero} mas alto es: {hero_alto} y mide: {altura_mayor} cms"




def heroe_mas_bajo(lista,genero):
    if not isinstance(lista, list):
        raise ValueError("ERROR | Se esperaba una lista")
    
    hero_bajo = None
    altura_menor = float('inf')
    
    

    for personaje in lista:
        altura = float(personaje ["altura"])
        if altura < altura_menor:
            altura_menor = altura
            hero_bajo = personaje["nombre"]

    return f"EL {genero} más bajo es: {hero_bajo} y mide: {altura_menor} cm"

def promedios_altura(lista,genero):
    if not isinstance(lista, list):
        raise ValueError("ERROR | ¡Se esperaba una lista!")
    
    suma_alturas = 0
    cantidad_personajes = 0

    for personaje in lista:
            altura = float(personaje["altura"])
            suma_alturas += altura
            cantidad_personajes += 1

    promedio = suma_alturas / cantidad_personajes
    return f"El promedio de altura de los {genero} es: {promedio:.2f} cm"

# def contador_ojos (lista:list) -> list:
#     colores_ojos = [] 
#     for personajes in lista:
#         if not personajes ["color_ojos"] in colores_ojos:
#             colores_ojos.append(personajes["color_ojos"])
    
    
#     # return colores_ojos
            
            


def contador_atributos (lista:list, atributo) -> list:
    lista_atributos = [] 
    for personajes in lista:
        if not personajes [atributo] in lista_atributos:
            lista_atributos.append(personajes[atributo])
    return lista_atributos







def heros_por_atributo (lista,atributo):
    for caracteristica in contador_atributos(lista,atributo):
        contador= 0
        for personaje in lista :
            if personaje [atributo] == caracteristica:
                contador +=1
        print (f"existen {contador} superheroes con {atributo} {caracteristica}")

def listar_heros_por_atributo (lista,atributo):
    for caracteristica in contador_atributos(lista,atributo):
        superheroes = []
        for personaje in lista :
            if personaje [atributo] == caracteristica:
                superheroes.append(personaje["nombre"])
        return f"los superheroes con {atributo}  son {superheroes}"
