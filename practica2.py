# Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor ingresa la edad: "))   

#Paso 2: Verificar la edad ingresada en el sistema
if edad >= 18:
    EdadPermitida = True
else:
    EdadPermitida = False

#Paso 3: Si la variable permitido es verdadera:
if EdadPermitida:
    print("Puedes ingresar a la discoteca")
else:
    print("Lo sentimos, no puedes ingresar")