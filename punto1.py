cantidad = 20
print(f"Voy a solicitarte {cantidad} números:")
numeros = []
neg=0
for i in range(cantidad):
    
    numero = input(f"Ingresa el número {i + 1}: ")
    numero = int(numero)
    if (numero < 0):
            neg=neg+1
    numeros.append(numero)
        
print('los numeros ingresados son: ',numeros)
print('los numeros negativos son: ',neg)
