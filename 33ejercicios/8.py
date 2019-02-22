print("Bienvenido al Sistema".center(50, "-"))
print("La hora extra son de Q10")
print("La hora de trabajo son de Q20")
hora = 0
Hora_extra = 0
SUELDO_HORA_EXTRA = 10
HORAS_DE_TRABAJO = 20
pago = 0
total = 0
hora = int(input("ingrese las horas de trabajo:"))
Hora_extra  = int(input("ingrese sus horas extras"))
pago = pago + int(hora * HORAS_DE_TRABAJO)
total = total + int(Hora_extra * SUELDO_HORA_EXTRA)
print("sus horas de trabajo son de:",pago)
print("su sueldo de horas extra es de:",total)
