# Ejercicios: 
# Ejercicio de simulacion de Login que hicimos en condicionales. Transformarlo a funcion

# Ejercicio de detectar si un numero es primo o no. Transformarlo a funcion
#x = 55

def es_primo(x):
    i = 2
    while i < x:
        if x % i == 0:
            print(f"{x} no es primo")
            return False
        i += 1
    else:  # si no hay interrupciones, entra en el "else" y lo aprovechamos para sacar el msg de que es primo
        print(f"{x} es primo")
        return True

#es_primo(x)
#Ejercicio mediante funcion que escriba los numeros primos que hay en un rango de numeros
rango = 65  
def sacar_numeros_primos (rango)   :
    if (rango>=3):
        print ("1, 2, 3 son primos")
    else:   
        print ("1, 2 son primos")

    for x in range (4, rango): 
        if es_primo (x):
           print (x)
sacar_numeros_primos (rango)   

# # Ejercicio 1 -> Escribe una función que reciba dos números y devuelva el mayor de los dos.
# def fun1mayor (a,b):
#     if a < b :
#         return b
#     else:
#         return a
# print(fun1mayor (2,3))

# # Ejercicio 2 -> Escribe una función que reciba dos números y devuelva el menor de los dos.

# def fun2menor (a,b):
#     if a > b :
#         return b
#     else:
#         return a
# print(fun2menor (2,3))

# # Ejercicio 3 -> Escribe una función que reciba un número y devuelva True si es par y False si es impar.

# def fun3 (a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# print (fun3 (77))

# # Ejercicio 4 -> Escribe una función que reciba un número y devuelva True si es impar y False si es par.

# def fun4 (a):
#     if a % 2 == 1:
#         return True
#     else:
#         return False
# print (fun4 (77))

# # Ejercicio 5 -> Escribe una función que reciba un número y devuelva True si es positivo y False si es negativo.
# def fun5 (a):
#     if a >= 0:
#         return True
#     else:
#         return False
# print (fun5 (77))

# # Ejercicio 6 -> Escribe una función que reciba un número y devuelva True si es negativo y False si es positivo.
# def fun6 (a):
#     if a <= 0:
#         return True
#     else:
#         return False
# print (fun6 (-77))

# # Ejercicio 7 -> Escribe una función que reciba un número y devuelva True si es cero y False si no lo es.
# def fun7 (a):
#     if a == 0:
#         return True
#     else:
#         return False
# print (fun7 (-77))

# # Ejercicio 8 -> Escribe una función que reciba un número y devuelva True si es un número entero y False si no lo es.
# def fun8 (a):
#     if type(a) == int:
#         return True
#     else:
#         return False
# print (fun8 (4.5))

# # Ejercicio 9 -> Escribe una función que reciba un número y devuelva True si es un número decimal y False si no lo es.
# def fun9 (a):
#     if type(a) == int or type (a) == float:
#         return True
#     else:
#         return False
# print (fun9 (4.5))

# # Ejercicio 10 -> Escribe una función que reciba un número y devuelva True si es un número positivo y decimal y False si no lo es. 
# def fun10 (a):
#     if type(a) == int or type (a) == float and a > 0:
#         return True
#     else:
#         return False
# print (fun10 (4))
# # Ejercicio 11 -> Escribe una función que reciba un número y devuelva True si es un número negativo y decimal y False si no lo es. 
# def fun11 (a):
#     if type(a) == int or type (a) == float and a < 0:
#         return True
#     else:
#         return False
# print (fun11 (4))
# # Ejercicio 12 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero y False si no lo es.
# def fun12 (a):
#     if type(a) == int and a > 0:
#         return True
#     else:
#         return False
# print (fun12 (4))
# # Ejercicio 13 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero y False si no lo es.
# def fun13 (a):
#     if type(a) == int and a < 0:
#         return True
#     else:
#         return False
# print (fun13 (4))

#  # Ejercicio 14 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero o decimal y False si no lo es. 
# #done
# # Ejercicio 15 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero o decimal y False si no lo es.
# #done
# # Ejercicio 16 -> Escribe una función que reciba un número y devuelva True si es un número entero o decimal y False si no lo es.
# #done
# # Ejercicio 17 -> Escribe una función que reciba un número y devuelva True si es un número entero o decimal y False si no lo es.
# #done
# # Ejercicio 18 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero o decimal y False si no lo es.
# #done

# Escribe una función contar_palabras que reciba una cadena de texto y devuelva un diccionario con el conteo de cada palabra en el texto.
def contar_palabras (cadena):
    cadena_partida = cadena.split()

    resultado = {}

    for palabra in cadena_partida:
        if palabra in resultado:
            resultado[palabra] += 1 
        else:
            resultado[palabra] = 1 

    print(resultado)
    # return thisdict
contar_palabras ("no se si esto si sale")

# Escribe una función frecuencia_caracteres que reciba una cadena de texto y devuelva un diccionario con el conteo de cada carácter en el texto
# Escribe una función analizar_palabras que reciba una cadena de texto y devuelva un diccionario con la longitud de cada palabra como clave y la lista de palabras de esa longitud como valor.
# Escribe una función contar_vocales_consonantes que reciba una cadena de texto y devuelva un diccionario con el conteo de vocales y consonantes en el texto.
          
          