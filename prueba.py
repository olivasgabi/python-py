opcPal='a'
totalCaja=0
while opcPal:3
print("...........Clinica Dental............")
print("1. Realizar cotizacion")
print("2. cerrar sistema")
print("3. cerrar sistema")
while True:
   opcPal=(input("Ingrese su accion"))
   vale=False
   for i in "123":
      if opcPal==i:
         vale=True
         if vale:
            break
         else:
            print("ACCESO INVALIDO")
   
    while True:
        carilla=25000
        implante=475000
        ortodoncia=800000
        
        
        print("..............Clinica Dental............")
        print("1. Carillas:  250.000")
        print("2. Implante:  475.000")
        print("3. Ortodoncia: 800.000")
        print("4. Salir")
        try:
            opc=int(input("Seleccione su tratamiento:  "))
        if opc==1:
            cant=int(input("Ingresa la cantidad de carillas:  "))
            total=carilla*cant
            print(f"El valor de carillas es:  ", total)
        elif opc==2:
            cant=int(input("Ingresa la cantidad de implante:  "))
            total=implante*cant
            print(f"El valor de implante es:  ", total)
        elif opc==3:
            cant=int(input("El valor de ortodoncia es:  ", total))
            total=ortodoncia*cant
            print(f"El valor de ortodoncia es:  ", total)
        elif opc==4:
            print("Ha salido de cotizacion") 
            break
        else: 
            print("Dato invalido")  
    
