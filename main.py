import os
from colorama import init, Fore, Style
from modulos import *

init(autoreset=True)

def mostrar_menu():

    ancho = 40
    linea = "═" * ancho

    print()
    print(linea)
    print(Fore.YELLOW + "    SISTEMA DE GESTION DE PRODUCTOS     ")
    print(linea)
    print("  1. Registrar nuevo producto            ")
    print("  2. Visualizar todos los productos      ")
    print("  3. Actualizar producto por ID          ")
    print("  4. Eliminar producto por ID            ")
    print("  5. Buscar producto                     ")
    print("  6. Reporte de stock bajo               ")
    print("  0. Salir                               ")
    print(linea)
    
      
# ─── PROGRAMA PRINCIPAL ───
while True:
    os.system("cls")
    mostrar_menu()
 
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
         insertar_producto()
    elif opcion == "2":
         mostrar_productos()
    elif opcion == "3":
         actualizar_producto()
    elif opcion == "4":
         eliminar()
    elif opcion == "5": 
         buscar()
    elif opcion == "6":
         reporte() 
    elif opcion == "0":
        print("\n¡Hasta luego!\n")
        break
    else:
        print("✗ Opción inválida. Intente de nuevo.")
        input("\nPresione Enter para volver al menú...")

