from data_heroes import *
from funciones_programa import*
from funciones import *

label_m = "Masculino"
label_f = "Femenino"
lista_masc =  [masculinos for masculinos in lista_personajes if masculinos ["genero"] == "M"]
lista_fem = [femeninos for femeninos in lista_personajes if femeninos ["genero"] == "F"] 



#a y b
# print (lista_fem , end= (" "))
# print(" ")
# print("-----------------------------------------------------------------------")
# print (lista_masc, end= (" "))




# c y d superheroe  mas alto 
# print (hero_mas_alto(lista_masc, "Masculino"))
# print(hero_mas_alto(lista_fem,"Femenino"))

#  e y f superheroe mas bajo

# print (hero_mas_bajo(lista_masc, label_m))
# print (hero_mas_bajo(lista_fem, label_f))

# promedios de altura
# print (promedio_altura(lista_fem,label_f))
# print(promedio_altura(lista_masc,label_m))


# colores ojos

# print (contador_atributos(lista_personajes,"color_ojos"))
# print (contador_atributos(lista_personajes,"color_pelo"))
# print (contador_atributos(lista_personajes,"inteligencia"))


# print("------------------------")

# print (heros_por_atributo(lista_personajes,"color_ojos"))
# print (heros_por_atributo(lista_personajes,"color_pelo"))
# print (heros_por_atributo(lista_personajes,"inteligencia"))

# print (listar_heros_por_atributo(lista_personajes,"color_ojos"))
# print (listar_heros_por_atributo(lista_personajes,"color_pelo"))
# print (listar_heros_por_atributo(lista_personajes,"inteligencia"))




while True:
        match menu():
                case "1":
                        mostrar_nombres (lista_personajes)
                case "2":
                        mostrar_nombres_altura(lista_personajes)
                case "3":
                        hero_mas_alto(lista_personajes)
                        hero_mas_bajo(lista_personajes) 
                case "4":
                        promedio_altura(lista_personajes)
                case "5":
                        hero_mas_liviano(lista_personajes) 
                        hero_mas_pesado(lista_personajes)
                case "6":
                        print (lista_masc, end= (""))
                        print (hero_mas_alto(lista_masc))
                        print (hero_mas_bajo(lista_masc))
                        print(promedio_altura(lista_masc))
                case "7":
                        print (lista_fem , end= (" "))
                        print(hero_mas_alto(lista_fem))
                        print (hero_mas_bajo(lista_masc))
                        print (promedio_altura(lista_fem))
                        
                case "8":
                        print (contador_atributos(lista_personajes,"color_ojos"))
                case "9":
                        print (contador_atributos(lista_personajes,"color_pelo"))
                case "10":
                        print (heros_por_atributo(lista_personajes,"inteligencia"))
                case "11":
                        print (listar_heros_por_atributo(lista_personajes,"color_ojos"))
                case "12":        
                        print (listar_heros_por_atributo(lista_personajes,"color_pelo"))
                case"13":
                        print (listar_heros_por_atributo(lista_personajes,"inteligencia"))
                case "14":
                        break
        pausar()
                        
                        

                        
                        
                        
                        
                        
                        
        
