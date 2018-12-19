#! /usr/bin/env python
# -*- coding: utf-8 -*-

print "\nBienvenidos a MenuSoft.\n"

menu_del_dia = {}
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
carta = ["Primer Plato", "Segundo Plato", "Postre"]
menu_semanal = None
menu = False

seleccion = raw_input("¿Quiere introducir el menu del día de toda la semana? (S/N): ")[0]
seleccion = seleccion.upper()
if seleccion == "S":
    menu_semanal = True
else:
    menu_semanal = False
    print "Menú del día:"
    plato = raw_input(".-Introduzca el plato del día: ")
    precio_correcto = True
    while precio_correcto:
        try:
            precio = float(raw_input(".-Introduzca precio: "))
            precio_correcto = False
        except ValueError:
            print "El precio no es correcto. Introduzca un precio válido."

    menu_del_dia[plato] = precio

cont = 0
while menu_semanal:
    print "\nMenú del día {}".format(dias_de_la_semana[cont])
    plato = raw_input(".-Introduzca {}: ".format(carta[0]))

    precio_correcto = True
    while precio_correcto:
        try:
            precio = float(raw_input(".-Introduzca precio: "))
            precio_correcto = False
        except ValueError:
            print "El precio no es correcto. Por favor, introduzca un precio válido."

    menu_del_dia[plato] = precio

    if (cont + 1) == len(dias_de_la_semana):
        menu_semanal = False
        menu = True
    else:
        cont = cont + 1

print "\n"
print menu_del_dia
print "\nMuchas gracias por utilizar MenuSoft."

