# # detectar si un numero es par o impar
# x = "hol2"
# if x < 0 :
#     x = x * (-1)
#     if x % 2 == 0:
#         print("El numero es par")
#     elif x % 2 != 0:
#         print("El numero es impar") 
# elif x == 0 :
#     print("El numero es 0 y par")
# elif x % 2 == 0:
#     print("El numero es par")
# elif x % 2 != 0:
#     print("El numero es impar")    

# else:
#     if type(x) != int :
#         print("No me has introducido un número")

# ordenar 3 numeros de mayo a menor
    # lista = [7,4,3]
# lista.sort(reverse=True)
# print(lista)

# Ejercicio 1 -> Escribe un programa que pida al usuario un número entero e imprima si es positivo, negativo o cero.
# take input from user
# input_a = input()

# # # print data type
# print(type(input_a))

# # # type cast into integer
# input_a = int(input_a)

# # # print data type
# print(type(input_a))
input_a = 98

if input_a == 0:
    print(input_a, "es el cero")
elif input_a < 0:
    print(input_a, "es negativo")
else:
    print(input_a, "es positivo")


# Ejercicio 2 -> Introducir el color del semáforo y mostrar si puede pasar, extremar la precaución o no pasar.
input_b = "green"
if input_b == "green":
    print(input_b, "puedes pasar")
elif input_a == "yellow":
    print(input_b, "cuidado cambio de color frena")
else:
    print(input_b, "no puedes pasar")
# Ejercicio 3 -> Mostrar si un número es par o impar
x = 0
if x % 2 == 0:
    print("numero par")
else :
    print("numero impar")


# Ejercicio 4 -> Introducir 3 números. Indicar si el tercero es la suma de los dos primeros o no.
x = int(input())
y = int(input())
z = int(input())
if x + y == z:
    print(x,"+", y, "es igual a", z)
else:
    print(x,"+", y, "no es igual a", z)

# Ejercicio 5 -> Introducir un precio a pagar y el dinero disponible y mostrar si le falta dinero, indicarle cuanto, si le sobra indicar cuánto y si esta justo mostrar gracias por la compra
precio = int(input())
saldo = int(input())

if saldo == precio:
    print("gracias por la compra")
elif saldo < precio:
    print("falta dinero para realizar la compra:",(precio - saldo))
else:
    print("sobra dinero para realizar la compra:",(saldo - precio))

# Ejercicio 6 -> Introducir 3 números. Ordenar descendentemente.
num1 = int(input())
num2 = int(input())
num3 = int(input()) 
lista = [num1,num2,num3]
lista.sort(reverse=True)
print(lista)

# Ejercicio 7 -> Comprobar la letra del DNI:
# letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
# Para la calcular la letra divide tu número de dni entre 23 y el resto es la posicion de la lista anterior: Ejemplo: 11223344 % 23 = 8 -> letra P

dni_completo = input()
  
letra_dni = dni_completo[8]
numero_dni = int(dni_completo[:8])
print(numero_dni%23)
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
if letras[numero_dni%23] == letra_dni :
    print("la letra conincide")
else:
    print("la letra no conincide")

