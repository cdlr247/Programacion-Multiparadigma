#Tipos de datos

#Numericos
    #Enteros
x=0
y=1
z=-1

print(type(x))          #muestra el tipo de dato de la variable
print(type(x),x,id(x))  #muestra su localizacion en memoria (celda)
print(x,y,z)

    #Flotantes
x=0.0
y=0.5
z=3.5

print(type(x))          #muestra el tipo de dato de la variable
print(type(x),x,id(x))  #muestra su localizacion en memoria (celda)
print(x,y,z)

    #Complejos
x=-5j
y=2+4j

print(type(x))          #muestra el tipo de dato de la variable
print(type(x),x,id(x))  #muestra su localizacion en memoria (celda)
print(x,y)

#CONVERTIDORES DE DATOS
int()       #Entero  
float()     #Flotante
complex()   #Complejo

    #Booleanos
x=5
y=10

print(bool(x==y))
print(bool(x))
print(bool(y))
print(bool())

x={}            #es un diccionario vacio
x={hola:hola2}  #esto es un diccionario con datos
x={0}           #esto es un SET

    #Cadenas
saludo="Buenos dias"
saludo2='Buenos dias'
saludo3=""""Buenos dias
        holaaaaaaa"""
despedida = "Adios"

print(f"Saludo:  {saludo}") #cadena interpolada 

print(saludo)
print(saludo2)
print(f"""Despedida: 
{despedida}""")
