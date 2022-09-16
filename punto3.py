## 3.Construir un programa para ir de compras en un supermercado
## que permita la construcción del siguiente MENU: 
'''Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)
2. Digitar 2 para mostrar todos los productos registrados (+0.8)
3. Digitar 0 para SALIR
'''

x =0
print("************Menu***********")
print("1. Agregar productos")
print("2. Mostrar productos")
print("3. Salir")
PRODUCTOS=[]

while (x!=3):
    detalle={}
    x=int(input("Ingrese una opcion del Menu"))
    if(x==1):
        print("ingresando Produto: ")
        detalle["codigo"]=input("Ingrese el codigo del Produto ")
        detalle["nombre"]=input("Ingrese nombre del Produto ")
        detalle["precio"]=int(input("Ingrese el valor del productos $ "))
        PRODUCTOS.append(detalle)
    elif(x==2):
        print("Mostrando los productos .... ")
        print(PRODUCTOS)
    elif(x==3):
        print("hasta Pronto...")
        break
    else:
        print("ingrese una opcion valida:")
