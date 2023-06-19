#tupla 1

print("producto de elementos")
lista=(1,2,3,4,5,6,7,8,9,)
tupla=1
for producto in lista:
  tupla *= producto 
print("el resultado es",tupla)

#tupla 2
print("mayor y minino")
def tener_ma_mi(tupla):
  maximo=max(tupla)
  minimo=min(tupla)
  return maximo, minimo
  lista=(1,2,3,4,5,6,7,)
  maximo,minimo= tener_ma_mi(lista)

print("el valor mayor es:",maximo)
print("el minimo es:",minimo

#tupla 3

print("elementos repetidos")

def contar_repetidas(tupla):
repetidas={}
for elemento in tupla:
  if elemento in repetidas:
  repetidas[elemento]+=1
else:
  repetidas[elemento]=1
  return repetidas

lista=(1,3,3,2,4,2,5,7,6,6,9,8)
resultado=contar_repetidas(lista)
print("las veces que aparece una ocurrencia:",resultado)

#tupla 4
print("indices")
def indice(tupla,elemento):
  indice={}
  for i in range(len(tupla)):
    if tupla{i}==elemento:
    indice.append(i)
    return indice
    lista = (1,2,3,4,3,5,5,6,2)
    mi_elemento=2
    resultado=indice(lista, mi_elemento)
    print(resultado)

#tupla 5
print("separa los elementos")
def cadena(tupla):
  vocales=("6","e","p")
  cadena_vocales=[]
  cadena_no_vocales=[]

for cadenas in tupla:
  if cadena[0].lower() in vocales:
    cadena_vocales.append(cadenas)
  else:
    cadena_no_vocales.append(cadenas)
return tupla(cadena_vocales),tupla(cadena_no_vocales)

lista= ("chat","python","java","html","objetivo","caballo")
cadena_vocales, cadena_no_vocales=cadenas(lista)

print("la cadena empieza con una vocal:",cadena_vocales)
print("cadenas que no empiezan por vocales",cadena_no_vocales)
