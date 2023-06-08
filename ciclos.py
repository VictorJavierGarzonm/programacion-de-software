#Victor Javier Garzon Muñoz  #8/05/2023  
#271106

#17

number= float(input("ingrese el primer numero"))

if number>0:
  print("el numero es positivo")
elif number==0:
  print("el numero es cero")
else:
  print("el numero es negativo")

# 19
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))
if number1 >= number2 and number1 >= number3:
    mayor = number1
elif number2 >= number1 and number2 >= number3:
    mayor = number2
else:
    mayor = number3


if number1 <= number2 and number1 <= number3:
    menor = number1
elif number2 <= number1 and number2 <= number3:
    menor = number2
else:
    menor = number3
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)

#20
name = input("escriba su nombre: ")
normal_hours = int(input("escriba cuantas horas trabaja normalmente: "))
extra_hours = int(input("escriba cuantas horas extra trabaja: "))
salary_hour = 4
salary_normal = normal_hours * salary_hour
salary_extra = extra_hours * (salary_hour * 2)

total_salary = salary_normal + salary_extra 
#21
a = int(input("escriba el primer numero: "))
b = int(input("escriba el segundo numero: "))
if a < b:
  result = a + b
else:
  result = a - b
  print("El resultado es: ", result)

#22
a = float(input("escriba el primer numero: "))
b = float(input("escriba el segundo numero: "))
if b == 0:
    print("No es posible dividir por cero")

elif a == b:
    print("El cociente de la division es: 1")
  
else:
    xquo = a / b
    print("El cociente de la division es: ", xquo)

#23
numdia = int(input("escriba un numero del 1 al 7: "))
if numdia ==1:
    print("Lunes")
elif numdia ==2:
    print("Martes")
elif numdia ==3:
    print("Miercoles")
elif numdia ==4:
    print("Jueves")
elif numdia ==5:
    print("Viernes")
elif numdia ==5:
    print("Viernes")
elif numdia ==6:
    print("Sabado")
elif numdia ==7:
    print("Domingo")
else:
    print("El numero ingresado no es valido")

#24
side1 = float(input("escriba la longitud del primer lado: "))
side2 = float(input("escriba la longitud del segundo lado: "))
side3 = float(input("escriba la longitud del tercer lado: "))
if side1 == side2 and side2 == side3:
  print("El triangulo es equilatero")
else:
  print("El triangulo no es equilatero")

#25
number1 = int(input("escriba el primer numero: "))
number2 = int(input("escriba el segundo numero: "))
if number1 < 0 or number2 < 0: 
  result = number1 + number2
  print("El resultado es: ", result)
else:
  result = number1 * number2
  print("El resultado es: ", result)

#26

day = int(input("escriba el día de nacimiento (1-31): "))
month = int(input("escriba el mes de nacimiento (1-12): "))
if day == 1:
    if day < 20:
        sign = "Capricornio"
    else:
        sign = "Acuario"
elif month == 2:
    if day < 19:
        sign = "Acuario"
    else:
        sign = "Piscis"
elif month == 3:
    if day < 21:
        sign = "Piscis"
    else:
        signo = "Aries"
elif month == 4:
    if day < 20:
        sign = "Aries"
    else:
        sign = "Tauro"
elif month == 5:
    if day < 21:
        sign = "Tauro"
    else:
        sign = "Géminis"
elif month == 6:
    if day < 21:
        sign = "Géminis"
    else:
        sign = "Cáncer"
elif month == 7:
    if day < 23:
        sign = "Cáncer"
    else:
        sign = "Leo"
elif month == 8:
    if day < 23:
        sign = "Leo"
    else:
        sign = "Virgo"
elif month == 9:
    if day < 23:
        sign = "Virgo"
    else:
        signo = "Libra"
elif month == 10:
    if day < 23:
        sign = "Libra"
    else:
        sign = "Escorpio"
elif month == 11:
    if day < 22:
        sign = "Escorpio"
    else:
        sign = "Sagitario"
elif month == 12:
    if day < 22:
        sign = "Sagitario"
    else:
        sign = "Capricornio"
        print("Tu signo es:", sign)


#27
base = int(input("escriba el valor de la base: "))
high = int(input("escriba el valor de la altura: "))
if base == high:
  figure = "Cuadrado"

else:
  figure = "Rectangulo"

perimeter = 2 * (base * high)
surface = base * high
print("El cuadrilatero es un: ", figure)
print("El perimetro es: ", perimeter)
print("La superficie es: ", surface)

#28
sellingprice=int(input())
if sellingprice >= 100:
    discount = sellingprice * 0.05
elif sellingprice < 200:
    discount = sellingprice * 0.10
else:
    discount = sellingprice * 0.15

final_price = sellingprice - discount
print("El descuento realizado es de ", discount)
print("El precio final con descuento es de ", final_price)


# 29

year = int(input("escriba un año para determinar si es bisiesto: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "es un año bisiesto")
else:
  print("no es un año bisiesto")