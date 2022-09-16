#Una jugueteria tiene mucho exito en sus 2 productos, payyasos y muñecas, suele hacer su venta por correo y la empresa de logistica
# les cobra por peso del paquete, deben calcular el peso de los payasos y muñecas que saldran en cada paquete de demanda
# cada payaso pesa 112 gr, cada muñeca 75 gr. Escribir un programa que lea el numero de payasos y muñecas.
#calcule el peso total del paquete que sera enviado y el precio total del  envio, si por cada 100gr de payaso se cobran 2.5 
# y por cada 100 gr de muñeca 2 pesos

precioPayaso = 2.5
precioMuneca = 2
PesoPayasos = 0
PesoMunecas = 0
PrecioTotal = 0

cantidadPayasos = int(input("Ingrese la cantidad de payasos: "))
cantidadMunecas = int(input("Ingrese la cantidad de muñecas: "))



def CalcularPrecioYPesoTotal(Payasos, Munecas):
    PesoPayasos = Payasos * 112
    PesoMunecas = Munecas * 75
    PesoTotal =  PesoPayasos + PesoMunecas

    PrecioPayasos = (PesoPayasos/100) * 2.5
    PrecioMunecas = (PesoMunecas/100) * 2
    PrecioTotal = PrecioPayasos + PrecioMunecas
    print("El peso total del paquete es " + str(PesoTotal) + " y el precio total es " + str(PrecioTotal))

CalcularPrecioYPesoTotal(cantidadPayasos,cantidadMunecas)


