def checar_si_existe (data, tipo):
    respuesta = False
    posicion = 1

    for ticket in data:
        if 'producto' in ticket and ticket["producto"] == tipo:
            respuesta = posicion
        
        posicion = posicion + 1

    return respuesta

def asignar_nombres (array_inicial):
    array_final = []
    for dato in array_inicial:
        lo_encontro = checar_si_existe(array_final, dato["tipo"])

        if lo_encontro:
            array_final[lo_encontro-1]['total'] = array_final[lo_encontro-1]['total'] + dato["precio"]
        else:
            array_final.append({
                "producto": dato["tipo"],
                "total": dato["precio"]
            })

    
    return array_final

consumo = [{
    "tipo":"bebida",
    "nombre":"cocacola",
    "precio": 22
}, {
    "tipo":"bebida",
    "nombre":"lacroix",
    "precio": 25
}, {
    "tipo":"botana",
    "nombre":"chetos",
    "precio": 17,
}, {
    "tipo":"bebida",
    "nombre":"lacroix",
    "precio": 25
}, {
    "tipo":"papitas",
    "nombre":"caca",
    "precio": 25,
}, {
    "tipo":"botana",
    "nombre":"caca",
    "precio": 87
}]

print(asignar_nombres(consumo))




# def generar_ticket (consumido):
#     tipo = ""
#     total_bebida = 0
#     total_botana = 0
#     resultado = []    
#     for ticket in consumido:
#         tipo = ticket["tipo"]
#         if tipo == "bebida":
#             total_bebida = total_bebida + ticket["precio"]
#         if tipo == "botana":
#             total_botana = total_botana + ticket["precio"]
#     resultado.append({"tipo": "bebida",
#                       "total": total_bebida})
#     resultado.append({"tipo": "botana",
#                       "total": total_botana})
#     print (resultado)



# def crear_objeto (nombre, edad, peso, estatura):
#     # objeto = {
#     #     "name": nombre,
#     #     "age": edad,
#     #     "weight": peso,
#     #     "height": estatura
#     # }

#     objeto = {}

#     objeto["name"] = nombre
#     objeto["age"] = edad
#     objeto["weight"] = peso
#     objeto["height"] = estatura

#     return objeto

# print(crear_objeto("Bob", 33, 91.5, 1.75))





# def arrojar_info (datos):
#     dinero_monto = 0
#     num_carros = 0
#     nombres = ""
#     index = 0

#     for persona in datos:
#         if index == 0:
#             nombres = nombres + persona["nombre"].title()
#         elif index + 1 == len(datos):
#             nombres = nombres + " y " + persona["nombre"].title()
#         else:
#             nombres = nombres + ", " + persona["nombre"].title()
        
#         dinero_monto = dinero_monto + persona["dinero"]
#         num_carros = num_carros + persona["carros"]

#         index = index + 1

#     # Seccion Carros
#     palabra_carro = "1 carro"
#     if num_carros > 1:
#         palabra_carro = f"{num_carros} carros"
    
#     if num_carros == 0:
#         palabra_carro = "ni un carro :("

#     seccion_carros = f"{palabra_carro}."

#     # Seccion Nombres
#     palabra_personas = "tiene"
#     if len(datos) > 1:
#         palabra_personas = "tienen"

#     seccion_nombres = f"{nombres} {palabra_personas}"

#     # return
#     return f"{seccion_nombres} ${dinero_monto}.00 pesos y {seccion_carros}"
    

# info = [{
#     "nombre":"bob",
#     "dinero": 300,
#     "carros": 0,
# },{
#     "nombre":"bob",
#     "dinero": 300,
#     "carros": 2,
# },{
#     "nombre":"bob",
#     "dinero": 300,
#     "carros": 1,
# }]

# print(arrojar_info(info))













# def dame_info (datos):

#     hijo = datos ["Tony"]["hijos"]["hijo1"]

#     print (hijo)
#     suma_edades = 0
#     empleado = 0
#     for info_plantilla in datos:
#         peso = datos[info_plantilla]["peso"]
#         edad = datos[info_plantilla]["edad"]
#         empleado = empleado + 1
#         suma_edades = suma_edades + edad
#     promedio = suma_edades / empleado    
#     print(promedio)



# info = {
#     "Tony": {
#         "peso":110,
#         "edad":33,
#         "hijos": {
#             "hijo1" : "tonito",
#             "hijo2" : "victoria"
#         }
#     },
#     "Emma": {
#         "peso":75,
#         "edad":27
#             },
#     "Juan": {
#         "peso":70,
#         "edad":32
#     }
# }

# print(dame_info(info))




# def jalar_datos (datos):
#     nombre = datos["nombre"]
#     amigos = 0
#     amiguitos = datos["amigos"]
#     for camaradas in amiguitos:
#         amigos = amigos + 1
#     return f"Hola, soy {nombre} y tengo {amigos} amigos"

# datos = {
#      "nombre": "Jorge Nitales",
#      "amigos": ["Tony", "Emma"]
# }
# print (jalar_datos(datos))




# def arbolito (numero):
#     acumulador = ""
#     for x in range(1, numero + 1):
#         acumulador = acumulador + "*"
#         print (acumulador)
    
#     print("||")
#     print("||")
    
#     return
    
# arbolito(10)



# def generar_respuesta (datos):
#     respuesta = ""
#     if datos % 2 == 0:
#         respuesta = respuesta + "foo"

#     if datos % 2 == 1:
#         respuesta = respuesta + "bar"

#     if datos % 5 == 0:
#         respuesta = respuesta + "lol"   

#     if datos % 3 == 0:
#         respuesta = respuesta + "oxo"
    
    
#     return respuesta

# def foobar (array):
#     array_regreso = []
#     for dato in array:
#         array_regreso.append(generar_respuesta(dato))
#     return array_regreso


# mi_array = [3, 8, 2, 30, 13]
# print(foobar(mi_array))





# def prueba(numeros_a):
#     for numero_mamalon in numeros_a:
#         print(numero_mamalon % 2)
#         if numero_mamalon % 2 == 1:
#             print("impar")
#         else:
#             print("par")





# def jalar_datos (objeto):
#     nombre = objeto["nombre"]
#     perros = objeto["perros"]
#     gatos = objeto["gatos"]
#     ratones = objeto["ratones"]
#     mascotas = perros + gatos + ratones

#     return f"que onda, soy {nombre} y tengo {mascotas} mascotas"


# datos = {
#     "nombre": "Jorge Nitales",
#     "perros": 2,
#     "gatos": 3,
#     "ratones": 1 
# }
# print (jalar_datos(datos))



# def datitos (obj):
#     nombre = obj["nombre"]
#     edad = obj["edad"]
#     return f"que pedo, me llamo {nombre} y tengo {edad}"

# datos = {
#     "nombre": "emma",
#     "edad": 33 
# }
# print (datitos(datos))






# def devolver_pares (pares):
#     lista = []
#     for numerito in pares:
#         if numerito % 2 == 0:
#             lista.append(numerito)
#     return lista
                
            


# print (devolver_pares([23, 45, 3, 4, 2]))




# hazme una funcion que recibe 1 parametro de tipo array de numeros y devuelveme todos los que son pares
# pares_only([23, 45, 3, 4, 2])
# [4, 2]


# import datetime
 
# def tiempo ():
#     hora = datetime.datetime.now()
#     return hora

# print (tiempo())




# from random import randrange

# def lista_random (numero):
#     lista = []
#     for x in range(1, numero + 1):
#         lista.append(randrange(100))
#     return lista

# print(lista_random(5))    



# haz una fuincion que recibe 1 numero, y que me regresa esa cantidad de numero aleatorios entre 1 y 100
# mi_funcion(4)
# respuesta: [23,65,41,2]






# def sumar(num_1, num_2):
#     respuesta = num_1 + num_2
#     return respuesta

# def multiplicar(num_1, num_2):
#     respuesta = num_1 * num_2
#     return respuesta

# print(multiplicar(3,4))

# def numero_lista(numerito):
#     lista = []

#     for i in range(1, numerito + 1):
#         lista.append(i)

#     return lista
    



# haz una fuincion que recibe 1 numero, y que me regresa esa cantidad contando desde el 1 hasta el numero que recibiste
# mi_funcion(4)
# respuesta: [1,2,3,4]
# mi_funcion(2)
# respuesta: [1,2]


# haz una fuincion que recibe 1 numero, y que me regresa esa cantidad de numero aleatorios entre 1 y 100
# mi_funcion(4)
# respuesta: [23,65,41,2]




# def duplicar_cantidad (numdub):
#     mi_array_favorito = []
#     suma = 0
#     for por2 in numdub:
#         por2 = por2 * 2
#         mi_array_favorito.append(por2)
#         suma = suma + por2 * 2
#     return suma



    



# mi_array_NOfavorito=[1,6,3,23,22]
# print(duplicar_cantidad(mi_array_NOfavorito))

# Hazme una funcion que duplique todos los valores del array
# ejemplo del input: [1,6,3,23,22]
# respuesta: [2,12,6,46,44]



# crear un array vacio:
# mi_array_favorito = []

# como agregarle elementos:
# mi_array_favorito.append(5)
# mi_array_favorito.append(8)

# print(mi_array_favorito)
# [5, 8]


# def mayornum(numeros):
#     max = 0
#     for num in numeros:
#         if num > max:
#             max = num
#     return max



# arraybob = [1,6,3,67,23,57,22]
# print(mayornum(arraybob))









# def pruebaimpares(valeverga):
#     contador = 0
#     for numeromamalon in valeverga:
#         if numeromamalon % 2:  
#             contador = contador + 1
#     return contador





# miarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(pruebaimpares(miarray))







# def prueba(numeros_a):
#     for numero_mamalon in numeros_a:
#         print(numero_mamalon % 2)
#         if numero_mamalon % 2 == 1:
#             print("impar")
#         else:
#             print("par")
    

# miarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prueba(miarray)






# def suma(numeros):
#     total = 0
#     for mi_numerito in numeros:
#         if isinstance(mi_numerito, int):
#             total = mi_numerito + total            
#         else: 
#             return "hay numeros invalidos"
#     return total


# miarray = [1, 5, 4, 20, 1]
# print(suma (miarray))






# def suma(num_1, num_2):
#     if isinstance(num_1, int) and isinstance(num_2, int):
#         return num_1 + num_2
 
#     return "valores invalidos"
    

# print(suma(1, "tres"))

# numeros = [1, 2, 3]
# for num in numeros: