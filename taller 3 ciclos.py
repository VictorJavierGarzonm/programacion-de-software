#Imprimir los números impares entre 0 y 100.
for _ in range (1,101,2):
  print("-",_)
#Imprimir los números pares entre 0 y 100

for _ in range(2,101,2):
  print("_",_)
#Escribir un programa en Python que imprima por pantalla los números del 1 al 3

for _ in range(1,4,1):
  print("-",_)

#Escribir un programa en Python que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla

for _ in range(10,0,-1):
  print("-",_)


#Escribir un programa en Python que imprima en pantalla los cuadrados de los números del 1 al 30.

print("numeros al cuadrado de 1 al 30")
for _ in range (1,31):
  print("-",_*_)
#Escribir un programa en Python que sume los cuadrados de los cien primeros números

sum = 0
for _ in range(101):
  sum+= _**2
  print("_",sum)

#Escribir un programa en Python que lea un número entero desde teclado y realice lasuma de los cien números siguientes, mostrando el resultado en pantalla

number=int(input("numero:"))
sum = 0 
for _ in range (number, (number + 101)):
  sum +=_
  print("el resultado es",sum)

#Halle el número factorial de un número ingresado por el usuario. Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius. El programa finalizará cuando lea un valor de temperatura igual a 999
while True:
 fahrenheit = float(input("Temp:"))
 if fahrenheit == 999:
     break
     celcius = (5/9)*(fahrenheit -32 )
     print("-",celcius)

#Imprima los números primos hasta un número ingresado por el usuario.

print("Numeros primos")


number_limit = int(input("Ingrese un número: "))

print(f"Números primos hasta {number_limit}:")

for i in range(2, number_limit + 1):
    es_primo = True
    for divisor in range(2, int(i ** 0.5) + 1):
        if i % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(i)

#Muestre en pantalla la tabla de multiplicar que el usuario desee
number = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del número {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#. Ingresar un conjunto de números positivos. Calcular y escribir su promedio sabiendo que se ingresará un valor menor que 0 para indicar el fin del conjunto de números

edicion = 0
total = 0
while True:
  x99=int(input("ingrese un numero al azar"))
  y98= int(input("ingrese otro numero al azar"))
  if x99 == 0 or y98 ==0:
    print("se acabo")
    break
  total = y98 + x99
  edicion +=1
  if edicion >=0:
    average = total / edicion
    print(" el promedio de la suma es",average)

else:
  print("ingrese un numero positivo ")

#Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente.

number19=int(input("ingrese un numero"))
number16=int(input("ingrese otro numero"))
if number19>= number16:
  print("el primer numero debe ser menor ")

else: 
  for number in range (number19,number16 + 1):
    print("-",number)


  #Realizar un algoritmo que muestre los valores de todas las piezas del dominó de forma ordenada: 0-0 0-1 1-1

x2=int(input("ingrese un numero:"))
y2=int(input("ingrese otro numero"))

for y in range (x2 + 1):
  for r in range (y,y2+1):
    print(f"{y}-{r}")