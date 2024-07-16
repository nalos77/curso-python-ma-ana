# # exercicis
# # Exercici 1
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena en majúscules.
cadena = input('Escribeme lo que quieras que te lo devuelvo en mayusculas:')
print (cadena.upper())

# # Exercici 2
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena en minúscules.
cadena = input('Escribeme lo que quieras que te lo devuelvo en minusculas:')
print (cadena.lower())

# # Exercici 3
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena amb la primera lletra en majúscules.
cadena = input('Escribeme lo que quieras que te la devuelvo con la primera letra en mayusculas:')
print (cadena.capitalize())

# # Exercici 4
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena amb la primera lletra de cada paraula en majúscules.
cadena = input('Escribeme lo que quieras que te la devuelvo con la primera letra de cada palabra en mayusculas:')
print (cadena.capitalize())

# # Exercici 5
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena amb les majúscules convertides en minúscules i viceversa.
cadena = input('Escribeme lo que quieras que te la devuelvo con las mayusculas cambiadas a minusculas y viceversa:')
print (cadena.swapcase())

# # Exercici 6
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena on un subcadena és reemplaçada per una altra subcadena.
cadena = input('Escribeme lo que quieras que te la devuelvo con las palabras "planta" remplazado por "biomasa":')
print (cadena.replace("planta","biomasa"))

# # Exercici 7
# # Escriu un programa que demani a l'usuari una cadena i mostri una llista de paraules a partir de la cadena.
cadena = input('escribeme una cadena con espacios y te la devuelvo como lista con sus componentes separados')
print (cadena.split)

# # Exercici 8
# # Escriu un programa que demani a l'usuari una llista de paraules i mostri la cadena a partir de la llista de paraules.

cadena = []
cadena.append("Hola")
cadena.append("que")
cadena.append("tal")
print(cadena)

resultado = " ".join(cadena)
print(resultado)

# # Exercici 9
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena sense espais en blanc al principi i al final.
cadena = input('escribeme una cadena con espacios a los lados y te los quito')
print (cadena.strip)

# # Exercici 10
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena sense espais en blanc al principi.
cadena = input('escribeme una cadena con espacios a los lados y te quito los del principio')
print (cadena.lstrip)

# # Exercici 11
# # Escriu un programa que demani a l'usuari una cadena i mostri la cadena sense espais en blanc al final.
cadena = input('escribeme una cadena con espacios a los lados y te quito los del final')
print (cadena.rstrip)


# Exercici 12
# Escriu un programa que demani a l'usuari una cadena i mostri True si la cadena comença amb una subcadena.
cadena = input('escribeme una cadena y si empieza por "Hola" te digo true')
print (cadena.startswith("Hola"))

# Exercici 13
# Escriu un programa que demani a l'usuari una cadena i mostri True si la cadena acaba amb una subcadena.
cadena = input('escribeme una cadena y si termina por "Hola" te digo true')
print (cadena.endswith("Hola"))

# Exercici 14
# Escriu un programa que demani a l'usuari una cadena i mostri la primera posició d'una subcadena en una cadena.
cadena = input('escribeme una cadena y si tiene  "Hola" te digo en que posicion de la cadena empieza esa subcadena')
print (cadena.find("Hola"))

# Exercici 15
# Escriu un programa que demani a l'usuari una cadena i mostri la darrera posició d'una subcadena en una cadena.
cadena = input('escribeme una cadena y si tiene  "Hola" te digo la ultima posicion de la cadena en la que empieza esa subcadena')
print (cadena.rfind("Hola"))

# Exercici 18
# Escriu un programa que demani a l'usuari una cadena i mostri el nombre de vegades que una subcadena apareix en una cadena.
cadena = input('escribeme una cadena y si tiene  "Hola" te digo la cantidad de veces que aparece')
print (cadena.count("Hola"))


# Exercici 19
# Escriu un programa que demani a l'usuari una cadena i mostri True si la cadena és alfanumèrica.
cadena = input('escribeme una cadena y si es toda alphanumerica te devuelvo true')
print (cadena.isalnum())

# Exercici 20
# Escriu un programa que demani a l'usuari una cadena i mostri True si la cadena és alfabètica.
cadena = input('escribeme una cadena y si es todo caracteres te devuelvo true')
print (cadena.isalpha())

