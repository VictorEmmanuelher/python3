#6
print("Bienvenido al Sistema".center(50, "-"))

AUMENTO  = 0.08
DESCUENTO_POR_SERVICIO = 0.25

salario = 0

salario = int(input("ingrese su salario"))

salario = salario + int (salario * AUMENTO)
resta = (salario - DESCUENTO_POR_SERVICIO)
print("su salario es de:",salario)
print("su salario con descuento es de:",resta)

