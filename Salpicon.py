#2.Leer información de 10 frutas {nombre, color, precio} para preparar
# un salpicón; el programa debe permitir mostrar las 10 frutas ingresadas
# al mismo tiempo+(1)


x =10
Frutas=[]
cantidad = 3


for i in range(cantidad):
    fruta={}
    print("ingresando Fruta: ")
    fruta["nombre"]=input("Ingrese nombre de la fruta ")
    fruta["color"]=input("Ingrese color de la fruta ")
    fruta["precio"]=int(input("Ingrese el valor de la fruta $ "))
    Frutas.append(fruta)
print("Mostrando las Frutas.... ")
print(Frutas)