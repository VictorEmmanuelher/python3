print("Bienvenidos al sistema".center(50, "-"))
print ("El prestramo es de 10.000 Quetzales")
PRESTAMO = 10.000
Años_a_pagar = 0
tasa_de_interes = 0.27

Años_a_pagar = int(input("ingrese los años a pagar"))
if PRESTAMO == 10.000:
    interes = (10.000 * Años_a_pagar)
    aumento = interes / tasa_de_interes
    print("el interes a pagar es de:",aumento)
