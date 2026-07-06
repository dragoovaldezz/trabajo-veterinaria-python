# Trabajo Final Integrador - Python
# Sistema de Gestión de Veterinaria
# Integrante 1: Menú principal y estructura del programa

mascotas = []
turnos = []
servicios = []
def registrar_mascota():
    print("\n[Opción 1] Registrar mascota")

    nombre = input("Ingrese el nombre de la mascota: ")
    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre de la mascota: ")

    especie = input("Ingrese la especie de la mascota: ")
    while especie == "":
        print("Error: la especie no puede estar vacía.")
        especie = input("Ingrese la especie de la mascota: ")

    edad = -1
    while edad < 0:
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            if edad < 0:
                print("Error: la edad no puede ser negativa.")
        except ValueError:
            print("Error: debe ingresar un número.")
            edad = -1

    duenio = input("Ingrese el nombre del dueño: ")
    while duenio == "":
        print("Error: el nombre del dueño no puede estar vacío.")
        duenio = input("Ingrese el nombre del dueño: ")

    mascota = [nombre, especie, edad, duenio]
    mascotas.append(mascota)

    print("\nMascota registrada correctamente.")


def ver_mascotas():
    print("\n[Opción 2] Ver mascotas registradas")

    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        print("\nMascotas registradas:")

        for i in range(len(mascotas)):
            mascota = mascotas[i]

            print("\nMascota", i + 1)
            print("Nombre:", mascota[0])
            print("Especie:", mascota[1])
            print("Edad:", mascota[2])
            print("Dueño:", mascota[3])


def solicitar_turno():
    print("\n[Opción 3] Solicitar turno")

    if len(mascotas) == 0:
        print("No hay mascotas registradas. Primero debe registrar una mascota.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ")

    encontrada = False

    for mascota in mascotas:
        if mascota[0].lower() == nombre_mascota.lower():
            encontrada = True

    if encontrada == False:
        print("Error: la mascota no está registrada.")
        return

    dia = input("Ingrese el día del turno: ")
    while dia == "":
        print("Error: el día no puede estar vacío.")
        dia = input("Ingrese el día del turno: ")

    horario = input("Ingrese el horario del turno: ")
    while horario == "":
        print("Error: el horario no puede estar vacío.")
        horario = input("Ingrese el horario del turno: ")

    motivo = input("Ingrese el motivo de la consulta: ")
    while motivo == "":
        print("Error: el motivo no puede estar vacío.")
        motivo = input("Ingrese el motivo de la consulta: ")

    turno = [nombre_mascota, dia, horario, motivo]
    turnos.append(turno)

    print("\nTurno registrado correctamente.")


def registrar_atencion():
    print("\n[Opción 4] Registrar atención médica")

    if len(mascotas) == 0:
        print("No hay mascotas registradas. Primero debe registrar una mascota.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota atendida: ")

    encontrada = False

    for mascota in mascotas:
        if mascota[0].lower() == nombre_mascota.lower():
            encontrada = True

    if encontrada == False:
        print("Error: la mascota no está registrada.")
        return

    print("\nTipos de servicio:")
    print("1. Consulta general")
    print("2. Vacunación")
    print("3. Desparasitación")
    print("4. Control médico")
    print("5. Urgencia")

    opcion_servicio = 0

    while opcion_servicio < 1 or opcion_servicio > 5:
        try:
            opcion_servicio = int(input("Ingrese el tipo de servicio: "))

            if opcion_servicio == 1:
                tipo_servicio = "Consulta general"
            elif opcion_servicio == 2:
                tipo_servicio = "Vacunación"
            elif opcion_servicio == 3:
                tipo_servicio = "Desparasitación"
            elif opcion_servicio == 4:
                tipo_servicio = "Control médico"
            elif opcion_servicio == 5:
                tipo_servicio = "Urgencia"
            else:
                print("Error: opción inválida.")

        except ValueError:
            print("Error: debe ingresar un número.")
            opcion_servicio = 0

    descripcion = input("Ingrese una descripción de la atención: ")
    while descripcion == "":
        print("Error: la descripción no puede estar vacía.")
        descripcion = input("Ingrese una descripción de la atención: ")

    costo = -1

    while costo < 0:
        try:
            costo = float(input("Ingrese el costo del servicio: "))

            if costo < 0:
                print("Error: el costo no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número.")
            costo = -1

    servicio = [nombre_mascota, tipo_servicio, descripcion, costo]
    servicios.append(servicio)

    print("\nAtención médica registrada correctamente.")


def ver_servicios():
    print("\n[Opción 5] Ver servicios realizados")

    if len(servicios) == 0:
        print("No hay servicios registrados.")
    else:
        print("\nServicios realizados:")

        for i in range(len(servicios)):
            servicio = servicios[i]

            print("\nServicio", i + 1)
            print("Mascota:", servicio[0])
            print("Tipo de servicio:", servicio[1])
            print("Descripción:", servicio[2])
            print("Costo: $", servicio[3])


def ver_estadisticas():
    print("\n[Opción 6] Ver estadísticas")

    total_recaudado = 0

    for servicio in servicios:
        total_recaudado = total_recaudado + servicio[3]

    print("Cantidad de mascotas registradas:", len(mascotas))
    print("Cantidad de turnos solicitados:", len(turnos))
    print("Cantidad de servicios realizados:", len(servicios))
    print("Total recaudado: $", total_recaudado)

    consultas = 0
    vacunaciones = 0
    desparasitaciones = 0
    controles = 0
    urgencias = 0

    for servicio in servicios:
        if servicio[1] == "Consulta general":
            consultas = consultas + 1
        elif servicio[1] == "Vacunación":
            vacunaciones = vacunaciones + 1
        elif servicio[1] == "Desparasitación":
            desparasitaciones = desparasitaciones + 1
        elif servicio[1] == "Control médico":
            controles = controles + 1
        elif servicio[1] == "Urgencia":
            urgencias = urgencias + 1

    print("\nCantidad por tipo de servicio:")
    print("Consulta general:", consultas)
    print("Vacunación:", vacunaciones)
    print("Desparasitación:", desparasitaciones)
    print("Control médico:", controles)
    print("Urgencia:", urgencias)


def mostrar_menu():
    print("\n===================================")
    print("      SISTEMA DE VETERINARIA")
    print("===================================")
    print("1. Registrar mascota")
    print("2. Ver mascotas registradas")
    print("3. Solicitar turno")
    print("4. Registrar atención médica")
    print("5. Ver servicios realizados")
    print("6. Ver estadísticas")
    print("7. Salir")
    print("===================================")


def pedir_opcion():
    try:
        opcion = int(input("Ingrese una opción: "))
        return opcion
    except ValueError:
        print("Error: debe ingresar un número.")
        return -1


def main():
    opcion = 0

    while opcion != 7:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            registrar_mascota()
        elif opcion == 2:
            ver_mascotas()
        elif opcion == 3:
            solicitar_turno()
        elif opcion == 4:
            registrar_atencion()
        elif opcion == 5:
            ver_servicios()
        elif opcion == 6:
            ver_estadisticas()
        elif opcion == 7:
            print("\nGracias por usar el sistema de veterinaria.")
        elif opcion == -1:
            pass
        else:
            print("Error: opción inválida.")

        if opcion != 7:
            input("\nPresione Enter para continuar...")


main()