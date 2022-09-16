#Tupla es una ordenada e inmutable
from multiprocessing.sharedctypes import Value
from re import L
from statistics import median


tupla = (1, 2, 3)
print(tupla)
tupla = 1, 2, 3
print(type(tupla)) #class 'tupla'
print(tupla)
tupla = (1, 2, 3)
#tupla[0] = 5 #Error! TypeError
tupla = 1, 2, ('a', 'b'), 3
print (tupla)
print(tupla[2][0]) #a
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #class 'tuple'

for t in tupla:
        print(t) #1, 2, 3
tupla = (1, 2, 3)
x, y, z = tupla
print(x,y,z) #1 2 3

tupla = (2,)
print(type(tupla)) #class 'tuple'
tupla = (1, 1, 1, 3, 5)
print(tupla.count(1)) #3
tupla(7,7,7,3,5)
print(tupla.index(7,2)) #2

lista = [1, 2,3,4]
lista =list("1234")

lista = [1, "hola", 3.67, [1, 2, 3]]


#son ordenadas, mantienen el orden
#pueden ser formadas por tipos arbitrarios
#pueden ser indexadas con [i]
#se pueden anidar
#son mutables
#son dinamicas
#acceder y modificar lista

a=[90,"python", 3.87]
print(a[-1]) #3.87
print(a[-2])
a[2]=1
print(a)
l=[1,2,3,4,5]
del l[1]
print(l) #1,3,4,5
x=[1,2,3,['p','q',[5,6,7]]]

#modificar una lista
l=[1,2,3,4,5,6]
l[0:3] = [0,0,0]
print(l) # [0,0,0,4,5,6]

l=[1,2,3]
l +=[4,5]

l=[1,2,3]
x,y,z = L
print(x,z,y)


for l in list:
    print(l)

for index, l in enumerate(lista):
    print(index, l)

lista1 = [5,9,10]
lista2 = ["Jazz", "Rock", "Djent"]
for l1,l2 in zip(lista1, lista2):
    print(lista1[i])

lista1 = [5,9,10]
for  i in range(0,len(lista)):
    print(lista1[i])


#UNIDAD 1                           UNIDAD 2                UNIDAD 3
#Clases y Objetos                   SQL,API,DJANGU          Tensor flow
#Examen             60%             Examen      50%         Practicas           30%
#Practicas          40%             Practicas   50%         Proyecto final      70%

#Metodos
l = [2,3]
l.append(4)
print(l)

#Extend
l=[2,1]
l.extend(4,5)
print(l)

#insert
l=[2,3]
l.insert(1,2)
print(l)

#remove
l=[2,3]
l.remove(2)
print(l)

#pop
l=[2,3]
l.pop()
print(l)

#pop con indice
l=[2,3]
l.pop(0) #eliminara el elemento por su indice
print(l)

#reverse
l=[2,3,5,6]
l.reverse()
print(l)

#sort
l=[3,5,6,3,1,4]
l.sort()
print(l)

l=[3,5,6,3,1,4]
l.sort(reverse=True)
print(l)

indice = l.index(6)
print(indice)

l=["Hugo","paco","Aldo","Myriam","Claudio"]
print(l.index("paco",2))

#SET
#son mutables
#se definen entre llaves
#no se pueden repetir elementos
#no estan indexados

s = set(l)
print(s)
print(type(s))

for ss in s:
    print(ss)


print (2 in s)
lista = list(s)
lista[0]=3
print(lista)

#metodos SET
s={1,2,3}
s.add(4)
print(s)

s.remove(5)

s.discard(5)

s.pop()         #Elimina un elemento del set al azar
print(s)

s.clear() #elimina todos los elementos del set

s1 = {1,2,3}
s2 = {3,4,5}

print(s1.union(s2))
print(s1.intersection(s2))

#Diccionarios
d1 = {"Nombre": "Rocio",
      "Edad": 24, 
      "Documento": "0231309120"}
print(d1)

print(type(d1))

d2 = dict([("Nombre","Rocio"),("Edad",24),("Documento","02391093")])
print(d2)

d3 = dict(Nombre="Rocio",Edad=24,Documento="23423422")
print(d3)

print(d3.get("Nombre"))


d3["Nombre"]="Pedro"
print(d3)

d3["Comida"] = "tacos"
print(d3)

d3["Comida"] = "burritos"
print(d3)

for x in d3:
    print(x)

for x in d3:
    print(d3[x])

for x,y in d3.items():
    print(x,y)

d1 = {"a":1, "B":2}
d2 = {"a":1, "b":{"c":3}}

d3={
    "d1":d1,
    "d2": d2
}

#metodos
d3.clear()

#items
print(d3.items())
print(list(d3.items()[0]))


#keys
print(d3.keys())
print(d3.values())


d3.popitem()

#update
d1 = {"a":1,"b":2}
d2 = {"a": 300, "b":400}
d1.update(d2)
print(d1)

#IF
a=0
b=2
if a!=1:
    print(b/a)
if b!=0:
    c=a/b
    d=c+1
    print(c,d)
print("fin")

if b!=1:
    pass
print("fin")

a=10
if a>5 and a<15:
    print(a)


if a>5:print("a es mayor que 15");print("Dentro del if")

print("fuera del if")

x=6
if x == 5:
    print("X es 5")
elif x==6:
    print("X es 6")
else:
    print("X no es 5")


print("Es 5" if x==5 else "No es 5")

a = 1
b = 5
c = a/b if b!=0 else -1
print(c)

#FOR

for i in "Phyton":
    print(i)
lista = [[1,2,3], [4,5,6],[7,8,9]]

for li in lista:
    for l in li:
        print(l)

#range
for i in range(5,20,2):
    print(i)

#break y continue
cadena = "Python"
for c in cadena:
    print(c)
    if c == "t":
        break

cadena = "Python"
for c in cadena:
    print(c)
    if c == "t":
        continue

while x>10:
    x-=1
    print(x)

while True:
    print("Bucle")

while x>0:x-=1;print(x)
else:
    print("fin del while")


#FUNCIONES
def f(x):
    print(2*x)

f(5)

def suma(x,y):
    print(x + y)

suma(1+2)

def resta(a,b,c=0):
    print(a-b-c)

resta(2,1)


listaNombres =["Rosa","Juan","Pedro"]

def nombres(nombres):
    for n in nombres:
        print(n)

nombres(listaNombres)

def nombres(*nombres):
    print(type(nombres))
    for n in nombres:
        print(n)

nombres("Pedro","Juan","Rosa")


def suma(**knumeros):
    suma = 0
    for key, value in knumeros.items():
        suma+=value
    print(suma)

suma(a=5,b=50,c=40)


def sumaMedia(a,b,c):
        suma = a + b + c
        media= suma/3
        return suma,media

sumaResultado, mediaResultado = sumaMedia(1,2,4)
print(sumaResultado,mediaResultado)


def miHola(a,b):
    """
    Alguna descripcion util
    """

help(miHola)
print(miHola)


def funcion(a,b,*args,**kargs):
    print(a)
    print(b)
    for i in args:
        print(i)
    for key,value in kargs.items():
        print(key,value)

funcion(10,20,48,92,42,213,4,2,3,5,7, x = "hola", y="adios")

#lambda arguments : exoression
(lambda *n: print(sum(n)))(*list(range(0,101,1)))

def multiplicador(n):
    return lambda a:print(a*n)
duplicador = multiplicador(2)
triplicador = multiplicador(3)
duplicador(11)
triplicador(11)


#input
x = input("Captura un numero: ")
print(type(x))



try:
    pass
except ZeroDivisionError:
    print("Zerro error")



#assert
def suma(a,b):
    assert(type(a)==int)
    assert(type(b)==int)
    print(a+b)
suma(1.2,5)


escribir un programa que reciba una cadena de caracteres 
y devuelva un diccionario  con cada palabra que contiene y su frecuencia

escribir una funcion que reciba un diccionario generado y que devuelva 
una tupla con la palabra mas repetida y su frecuencia



