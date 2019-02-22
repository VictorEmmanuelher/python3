print("Bienvenido al Sistema".center(50, "-"))
print("todos los productos tienen un descuento del 35%")
monto = 0
DESCUENTO = 0.35

monto = int(input("ingrese el valor de su producto"))
medicina = (monto * 0.35)
descuento = (monto - medicina)
print("su total a pagar es",descuento)
