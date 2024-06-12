from data_heroes import lista_personajes
from funciones_programa import *
from json_abrir import *



#b) muestra por pantalla todos los nombres de los heroes
mostrar_nombres (json_read("data_heroes.json"))
print("---------------------------------------")

# c)muestra altura con el nombre

mostrar_nombres_altura(lista_personajes)
print("---------------------------------------")
# d) muestra heroe mas alto
hero_mas_alto(lista_personajes)
print("---------------------------------------")

# e) muestra el heroe mas bajo
hero_mas_bajo(lista_personajes) 
print("---------------------------------------")

# f) recorre lista y saca promedio
promedio_altura(lista_personajes)
print("---------------------------------------")


# h) calcula el mas pesado y el mas liviano
hero_mas_pesado(lista_personajes)
print("---------------------------------------")

hero_mas_liviano(lista_personajes) 