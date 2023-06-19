#Lista 1

print("suma de numeros de una lista")
def suma_numeros(lista):
  suma=sum(lista)
  return suma

numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
resultado=suma_numeros(numeros)
print("el resultado es",resultado)

#lista 2

print("el promedio de los numeros de la lista")
def valor_promedio(lista):
  suma=sum(lista)
  promedio=len(lista)
  conversion= suma/promedio

  return conversion
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
resultado=valor_promedio(numeros)
print("el promedio de los numeros es:",resultado)

#lista 3

print("eliminar numeros duplicados")
numero=[1,2,3,4,5,6,7,8,9,10]
lista_f=list(set(numeros))
print("lista sin duplicados:",lista_f)

#lista 4

print("lista desordenada")
numeros_lista=[1,4,2,8,5,3,9,7,6,10]
numeros_lista.sort()
print("lista ordenada;"numeros_lista)


#lista 5
print("palabra mas larga")
def palabra_larga(lista):
  palabra=max(lista,key=len)
  return palabra

lista_palabra=["hola","adios","banana","hey","cun","odioso"]
palabra=palabra_larga(lista_palabra)
print("la mas larga es:",palabra)
