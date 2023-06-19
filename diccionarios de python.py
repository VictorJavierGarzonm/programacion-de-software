#diccionario 1

print("cuenta palabras")
def count(lista_palabras):
  contador={}
  for palabra in lista_palabras:
    if palabra in contador:
      
   else:contador[palabra] =1

  return contador

lista=["hellow","java","java","java","java","php","php"]
resultado=count(lista)
print("el resultado es",resultado)


#diccionario 2

print("calcula promedio")
def calculo_notas(notas_finales):
  notas_totales=0
  estudiantes= len(notas_finales)

for notas in notas_finales,values():
  notas_totales += sum(notas)

promedio = notas_totales/estudiantes
return promedio

alumnos={
  "ivan":[80,78,67].
  "andrea":[90,78,89],
"brayan":[78,68,100]}

promedio=calculo_notas(alumnos)
print("el promedio final de los alumnos es",promedio)

#diccionario 3

print("filtracion")

def filtro(diccionario, valor):
  value={}
  for llave, val in diccionario.items():
    if val==valor:
      value[llave]=val
      return value
diccionario={"A",2,"B",2,"Z",3,"X",4,"M":4}

valor=4
resultado = filtro(diccionario, valor)
print("el resultado es:",resultado)

#diccionario 4


print("combinacion de  diccionario")
def combinar_diccionarios(diccionario1,diccionario2)
diccionario_combinado ={}
for clave, valor in diccionario1.items():
  if clave in diccionario2:
    diccionario_combinado[clave]=valor+diccionario2[clave]

else: diccionario_combinado[clave]=valor

for clave, valor in diccionario2.items():
  if clave not in diccionario1:
    diccionario_combinado[clave]=valor

return diccionario_combinado

diccionario1={"A":1,"B":2,"C":3}
diccionario2={,"B":3,"C":4,"D":5}

resultado =combinar_diccionarios(diccionario1,diccionario2)

print("el resultado es",resultado)


#diccionario5

print("palabras frecuntes")
def contar (texto):
  contador={}
  palabra=texto,lower().split()

for palabra in palabras:
  if palabra in contador:
    contador[palabra] +=1
  else:
    contador[palabra]=1

return contador

palabrass="hello hellow HELLOW java JAVA"
resultado= contar(palabrass)