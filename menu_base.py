def datos_nacchi():
    print("Mi nombre es Ignacia Padilla y tengo 34 años.")
def datos_cami ():
    print("Mi nombre es Camila Cerda y tengo 26 años")

def datos_elba():
    print("Mi nombre es Elba Sanchez y tengo 20 años")
# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_nacchi()  # Llamada a la función de Ignacia
    elif op == "2":
        datos_cami()
        # Aquí se llamará a la función del integrante 2
    elif op == "3":
        datos_elba() # Aquí se llamará a la función del integrante 3
    else:
        print("Opción inválida.")
