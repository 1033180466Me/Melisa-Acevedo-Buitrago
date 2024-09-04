# Definir las listas y contadores necesarios
caninos = []
felinos = []
graves = []
criticos = []
pacientes = []  # Asegúrate de que esta lista esté definida
cantidad_perros = 0
cantidad_gatos = 0
#Mensaje de bienvenida 
print("SISTEMA DE GESTION DE PACIENTES ANIMALES-CLINICA VETERINARIA")
print("\n menu principal")
print("1 Ingresar un paciente")
print("2 Cantidad de pacientes")
print("3 Mostrar de edades")
print("4 Mostrar pacientes graves y criticos")
print("5 Buscar paciente por por codigo")
print("6 Mostrar todos los pacientes")
print("7 salir")
while True:
    # Selección de opción
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        # Solicitar datos del paciente
        nombre = input("Ingrese el nombre del paciente: ")
        tipo_animal = input("Ingrese el tipo de animal (perro/gato): ").lower()
        edad = int(input("Ingrese la edad del paciente: "))
        estado = input("Ingrese el estado (grave/crítico): ").lower()
# Validación del tipo de animal
        if tipo_animal not in ['perro', 'gato']:
            print("Tipo de animal no válido. Por favor, ingrese 'perro' o 'gato'.")
            continue
if tipo_animal == 'perro':
    codigo = f"Caninos{cantidad_perros + 1:03}"
    cantidad_perros += 1
    caninos.append([nombre, codigo, tipo_animal, edad, estado])
elif tipo_animal == 'gato':
    codigo = f"Felinos{cantidad_gatos + 1:03}"
    cantidad_gatos += 1
        # Guardar paciente
felinos.append([nombre, codigo, tipo_animal, edad, estado])
        # Contar pacientes graves y críticos
if estado == "grave":
    graves.append([nombre, codigo, tipo_animal, edad, estado])
elif estado == "crítico":
    criticos.append([nombre, codigo, tipo_animal, edad, estado])

elif opcion == "2":
        print(f"Cantidad de pacientes ingresados: {cantidad_perros + cantidad_gatos}")
        print(f"Cantidad de perros: {cantidad_perros}")
        print(f"Cantidad de gatos: {cantidad_gatos}")

elif opcion == "3":
        if len(pacientes) > 0:
            promedio_edades = sum(p[3] for p in pacientes) / len(pacientes)
            print(f"El promedio de las edades de las mascotas ingresadas es: {promedio_edades:.2f} años")
        else:
            print("No hay pacientes ingresados.")

elif opcion == "4":
            print(f"Cantidad de pacientes en estado grave: {len(graves)}")
            print(f"Cantidad de pacientes en estado crítico: {len(criticos)}")
elif opcion == "5":
        codigo_busqueda = input("Ingrese el código del paciente a buscar: ")
        encontrado = False
        for paciente in pacientes:
            if paciente[1] == codigo_busqueda:
                print(f"Paciente encontrado: Nombre: {paciente[0]}, Tipo: {paciente[2]}, Edad: {paciente[3]}, Estado: {paciente[4]}")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró un paciente con el código {codigo_busqueda}.")
elif opcion == "6":
        if len(pacientes) > 0:
            print("\nLista de todos los pacientes ingresados:")
            for paciente in pacientes:
                print(f"Nombre: {paciente[0]}, Código: {paciente[1]}, Tipo: {paciente[2]}, Edad: {paciente[3]}, Estado: {paciente[4]}")
        else:
            print("No hay pacientes ingresados.")

elif opcion == "7":
        while True:
            sub_opcion = input("\n¿Está seguro que desea salir? (1. Confirmar salida / 2. Rechazar salida): ")
            if sub_opcion == "1":
                print("Saliendo del sistema. ¡Hasta luego!")
                exit()
            elif sub_opcion == "2":
                break
            else:
                print("Opción no válida. Por favor, ingrese 1 o 2.")
else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.")