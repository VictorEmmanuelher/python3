#solicitar al usuario que selecciones una opcion, opcion1 solicitar dos numero y elevar el primer nuemero elevando al segundo numero

#opcion2:solcitar 3numeros y elevar el primero al segundo y el resultado elevarlo al tercero

elevacion = 0
print("Bienvenido al programa".center(50,"-"))
opcion=input("1.elevar dos numeros el primero por el segundo 2.elevar 3numeros y elevar el primero por el segundo")

if opcion == "1":
    v1 = int(input("ingrese un valor:"))         
    v2 = int(input("ingrese un valor:"))
    elevacion = v1 ** v2
    print ("la elevacion es{}".format(elevacion))
elif opcion == "2":
      v1 = int(input("ingrese un valor:"))         
      v2 = int(input("ingrese un valor:"))
      v3 = int(input("ingrese un valor:"))
      elevacion =(v1 ** v2) ** v3
    print("la elevacion es {}".format(elevacion))
    else:
    ("opcion invalida")


