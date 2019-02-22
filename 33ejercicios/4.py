Euros_Dolar = 1.45
Dolar_Euros = 7.65
cantidad = 0
total = 0
print ("Bienvenido al conversor".center(50,"-"))
opcion=input(" 1- Euros a dolares 2- dolares a Euros:")

if opcion == "1":
    Euros = input ("cantidad de Euros")
    saldo = float (Euros)/ Euros_Dolar
    print ("La convercion es {}".format(saldo))
elif opcion == "2":
    dolares = input ("cantidad de dolares")
    saldo = float (dolares) * Dolar_Euros
    print ("La convercion es {}".format(saldo))
else:
    print ("opcion no valida")
