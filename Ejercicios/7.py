#7
print("Bienvenido al Sistema de calculo".center(50, "-"))
URGENCIAS = 0.37
PEDIATRIA = 0.42
TRAUMATOLOGIA = 0.21
aumento_en_area = 0

salida = input("ingrese su presupuesto 1-si \ 2-no")
while salida != 2:
    presupuesto = int(input("ingresar la cantidad"))
    print("la cantidad de urgencias es:. {}".format(presupuesto * URGENCIAS))
    print("la cantidad de pediatria es:. {}".format(presupuesto * PEDIATRIA))
    print("la cantidad de traumatologia es:. {}".format(presupuesto * TRAUMATOLOGIA))

