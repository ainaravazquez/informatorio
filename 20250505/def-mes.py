# Ejercicio: tenemos que ingresar por pantalla un string con la fecha en formato iso
# por ejemplo '20250505', identificar el mes en el que se encuentra, en este caso mayo.

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 
'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

fecha = input('Ingrese la fecha en formato iso (AAAAMMDD): ')

mes_ingresado= fecha[4:6] #aca tomo el orden del mes y lo coloco en una variable

if len(fecha) == 8 and fecha.isdigit():
    if int(mes_ingresado) >= 1 and int(mes_ingresado) <= 12:
        mes = meses[int(mes_ingresado)-1] #aca le resto 1 porque la lista empieza en 0
        print(f'El mes ingresado es: {mes}')
    else:
        print('El mes ingresado no es válido.')
