import os
from pathlib import Path
from sqlite3 import connect
from colorama import Back, init, Fore, Style
from conexion_db import db
from datetime import datetime

# Obtener el cursor (con manejo de errores)
try:
    cursor = db()
except Exception as e:
    print(f"Error al inicializar la base de datos: {e}")
    input("Presione Enter para salir...")
    exit(1)

init(autoreset=True)
os.system('cls')

#ruta_db = Path(__file__).parent / 'Bases_De_Datos' / 'inventario.db'   
#conn = sqlite3.connect(ruta_db)
#cursor = conn.cursor()
    

def mostrar_productos():
    os.system('cls')
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    if not productos:
        print('📭 No hay productos registrados.')
        return
    print('\n--- LISTA DE PRODUCTOS ---\n')

    largo_max_0 = max(len(str(p[0])) for p in productos)
    largo_max_1 = max(len(str(p[1])) for p in productos)
    largo_max_2 = max(len(str(p[2])) for p in productos)
    largo_max_3 = max(len(str(p[3])) for p in productos)
    largo_max_4 = max(len(str(p[4])) for p in productos)
    largo_max_5 = max(len(str(p[5])) for p in productos)   

    ##############################################################################################################
    # para armar encabezados
    h0, h1, h2, h3, h4, h5 = "ID", "NOMBRE", "DESCRIPCIÓN", "CANTIDAD", "PRECIO", "CATEGORÍA"

    if largo_max_0 < len(h0):
       largo_max_0 = largo_max_0 + len(h0)

    if largo_max_1 < len(h1):
       largo_max_1 = largo_max_1 + len(h1)

    if largo_max_2 < len(h2):
       largo_max_2 = largo_max_2 + len(h2)

    if largo_max_3 < len(h3):
       largo_max_3 = largo_max_3 + len(h3)
       
    if largo_max_4 < len(h4):
       largo_max_4 = largo_max_4 + len(h4) 

    if largo_max_5 < len(h5):
       largo_max_5 = largo_max_5 + len(h5)           

    print(f'{h0:<{largo_max_0}} ║ {h1:<{largo_max_1}} ║ {h2:<{largo_max_2}} ║ {h3:<{largo_max_3}} ║ {h4:<{largo_max_4}} ║ {h5:<{largo_max_5}} ║')

    ################################################################################################################# 

    print()
    
    for p in productos:
       print(f'{p[0]!s:<{largo_max_0}} ║ {p[1]!s:<{largo_max_1}} ║ {p[2]!s:<{largo_max_2}} ║ {p[3]!s:<{largo_max_3}} ║ {p[4]!s:<{largo_max_4}} ║ {p[5]!s:<{largo_max_5}} ║')

    input("\nENTER PARA CONTINUAR\n")

    #################################################################################################################

def insertar_producto():

    while True:  # Bucle principal que permite agregar múltiples productos
        os.system("cls")
        # Solicitar datos al inicio del ciclo
        print("\n" + "=" * 50)
        print("🆕 INGRESE LOS DATOS DEL PRODUCTO:")
        print("=" * 50)
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        categoria = input("Categoría: ")
        print("\n" + "=" * 50)

        # Validar nombre
        if not nombre or not nombre.strip():
            print("❌ Error: El nombre no puede estar vacío.")
            print("\n Cancelar 1 - Volver a intentar 2 \n")
            accion = input("Que desea hacer : ")
            if accion == "1":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                break
            elif accion == "2":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                continue
            else:
                input("Opción inválida regresar al menu")
                break

        # Validar descripción
        if not descripcion or not descripcion.strip():
            print("❌ Error: La descripcion no puede estar vacía.")
            print("\n Cancelar 1 - Volver a intentar 2 \n")
            accion = input("Que desea hacer : ")
            if accion == "1":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                break
            elif accion == "2":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                continue
            else:
                input("Opción inválida regresar al menu")
                break

        # Validar categoría
        if not categoria or not categoria.strip():
            print("❌ Error: La categoria no puede estar vacía.")
            print("\n Cancelar 1 - Volver a intentar 2 \n")
            accion = input("Que desea hacer : ")
            if accion == "1":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                break
            elif accion == "2":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                continue
            else:
                input("Opción inválida regresar al menu")
                break

        # Validar cantidad
        try:
            if int(cantidad) < 0:
                print("❌ Error: La cantidad no puede ser negativa")
                print("\n Cancelar 1 - Volver a intentar 2 \n")
                accion = input("Que desea hacer : ")
                if accion == "1":
                    input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                    break
                elif accion == "2":
                    input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                    continue
                else:
                    input("Opción inválida regresar al menu")
                    break
        except (ValueError, TypeError):
            print("❌ Error: La cantidad debe ser un número válido")
            print("\n Cancelar 1 - Volver a intentar 2 \n")
            accion = input("Que desea hacer : ")
            if accion == "1":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                break
            elif accion == "2":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                continue
            else:
                input("Opción inválida regresar al menu")
                break

        # Validar precio
        try:
            if float(precio) < 0:
                print("❌ Error: el precio no puede ser negativo")
                print("\n Cancelar 1 - Volver a intentar 2 \n")
                accion = input("Que desea hacer : ")
                if accion == "1":
                    input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                    break
                elif accion == "2":
                    input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                    continue
                else:
                    input("Opción inválida regresar al menu")
                    break
        except (ValueError, TypeError):
            print("❌ Error: El precio debe ser un número válido")
            print("\n Cancelar 1 - Volver a intentar 2 \n")
            accion = input("Que desea hacer : ")
            if accion == "1":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                break
            elif accion == "2":
                input("\nPRECIONE UNA TECLA PARA CONTINUAR")
                continue
            else:
                input("Opción inválida regresar al menu")
                break

        # Si todas las validaciones pasan, insertar en la tabla
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre.strip(), descripcion.strip(), cantidad, precio, categoria.strip()))
        #conn.commit()
        cursor.connection.commit # al fin pude guardar era asi


        print("\n ✅ Producto agregado correctamente \n")

        # Menú de opciones después de agregar el producto
        print("📋 ¿Qué deseas hacer?")
        print("1. ➕ Agregar otro producto")
        print("2. 🔙 Volver al menú principal")

        opcion = input("\nSelecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            os.system("cls")
            continue  # Continúa el bucle para agregar otro producto

        elif opcion == "2":
            print("\n🔙 Volviendo al menú principal...\n")
            input("PRECIONE UNA TECLA PARA CONTINUAR")
            break  # Sale de la función

        else:
            print("\n❌ Opción no válida. Volviendo al menú principal...\n")
            input("PRECIONE UNA TECLA PARA CONTINUAR")
            break  


###########################################################################################################

def actualizar_producto():
    
            os.system('cls')

            print(f"\n{Fore.CYAN}{'='*50}")
            print(f"{Fore.YELLOW}SISTEMA DE ACTUALIZACION DE INVENTARIO")
            print(f"{Fore.CYAN}{'='*50}")
            print(f"{Fore.GREEN}1. {Fore.WHITE}Actualizar TODOS los campos")
            print(f"{Fore.GREEN}2. {Fore.WHITE}Salir del sistema")
            print(f"{Fore.CYAN}{'='*50}")


            while True:
                os.system("cls")
                print(f"\n{Fore.GREEN}📝 ACTUALIZACION COMPLETA DE PRODUCTO")

                try:

                    pro_id = input("\nSELECCIONE EL ID DEL PRODUCTO A ACTUALIZAR : ").strip()
                    
                    cursor.execute('SELECT * FROM productos WHERE id = ?', (pro_id,))
                    productos = cursor.fetchall()
                    
                    if not productos:
                        print(f'{Fore.RED}❌ No hay productos con el ID: {pro_id}. Intente nuevamente.')
                        input("\nPRESIONE ENTER")
                        continue      
                    else:
                        # MOSTRAR EL REGISTRO COMPLETO
                        for p in productos:
                            print("\n" + "="*50)
                            print(f"{Fore.CYAN}REGISTRO DEL PRODUCTO ID : {Fore.YELLOW}{pro_id}")
                            print("="*50)
                            print(f"ID           : {p[0]}")
                            print(f"NOMBRE       : {p[1]}")
                            print(f"DESCRIPCION  : {p[2]}")
                            print(f"CANTIDAD     : {p[3]}")
                            print(f"PRECIO       : {p[4]}")
                            print(f"CATEGORIA    : {p[5]}")
                            print("="*50)

                
                    # Validar que no esté vacío
                    if pro_id == "":
                        print(f"{Fore.RED}❌ Error: El ID no puede estar vacio.")
                        input("\nPRESIONE ENTER")
                        continue
                    
                    # Validar que sea número
                    if not pro_id.isdigit():
                        print(f"{Fore.RED}❌ Error: El ID debe ser un numero entero.")
                        input("\nPRESIONE ENTER")
                        continue
                        
                    # Guardar valores actuales
                    id_actual = p[0]
                    nombre_actual = p[1]
                    descripcion_actual = p[2]
                    cantidad_actual = p[3]
                    precio_actual = p[4]
                    categoria_actual = p[5]
                
                    break
                
                except:
                    print(f"{Fore.RED}❌ Error en la consulta: ")
                    input("\nPRESIONE ENTER")
                    continue

            ##############################################################################################################
            # ACTUALIZACIÓN DE CAMPOS (ENTER mantiene el valor actual)

            print(f"\n{Fore.GREEN}📝 ACTUALIZANDO PRODUCTO \n")

            # Campo 1: NOMBRE
            nuevo_nombre = input("Nuevo nombre (ENTER para mantener): ").strip()
            if nuevo_nombre == "":
                nuevo_nombre = nombre_actual

            # Campo 2: DESCRIPCION
            #print(f"\n{Fore.CYAN}DESCRIPCION ACTUAL: {Fore.YELLOW}{descripcion_actual}")
            nueva_descripcion = input("Nueva descripcion (ENTER para mantener): ").strip()
            if nueva_descripcion == "":
                nueva_descripcion = descripcion_actual

            # Campo 3: CANTIDAD
            #print(f"\n{Fore.CYAN}CANTIDAD ACTUAL: {Fore.YELLOW}{cantidad_actual}")
            while True:
                nueva_cantidad = input("Nueva cantidad (ENTER para mantener): ").strip()
                if nueva_cantidad == "":
                    nueva_cantidad = cantidad_actual
                    break
                else:
                    if nueva_cantidad.isdigit():
                        nueva_cantidad = int(nueva_cantidad)
                        break
                    else:
                        print(f"{Fore.RED}❌ Error: La cantidad debe ser un número entero.")

            # Campo 4: PRECIO
            #print(f"\n{Fore.CYAN}PRECIO ACTUAL: {Fore.YELLOW}{precio_actual}")
            while True:
                nuevo_precio = input("Nuevo precio (ENTER para mantener): ").strip()
                if nuevo_precio == "":
                    nuevo_precio = precio_actual
                    break
                else:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        break
                    except ValueError:
                        print(f"{Fore.RED}❌ Error: El precio debe ser un número válido (ej: 10.99).")

            # Campo 5: CATEGORIA
            nueva_categoria = input("Nueva categoria (ENTER para mantener): ").strip()
            if nueva_categoria == "":
                nueva_categoria = categoria_actual

            ##############################################################################################################
            # ACTUALIZAR EN LA BASE DE DATOS
            try:
                cursor.execute('''
                    UPDATE productos 
                    SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                    WHERE id = ?
                ''', (nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, pro_id))
                
                cursor.connection.commit()

                os.system("cls")
                print("\n" + "="*50)
                print(f"{Fore.GREEN}✅ ¡ACTUALIZACIÓN EXITOSA!")
                print("="*50)
                print(f"{Fore.CYAN}ID           : {Fore.YELLOW}{pro_id}")
                print(f"{Fore.CYAN}NOMBRE       : {Fore.YELLOW}{nuevo_nombre}")
                print(f"{Fore.CYAN}DESCRIPCION  : {Fore.YELLOW}{nueva_descripcion}")
                print(f"{Fore.CYAN}CANTIDAD     : {Fore.YELLOW}{nueva_cantidad}")
                print(f"{Fore.CYAN}PRECIO       : {Fore.YELLOW}{nuevo_precio}")
                print(f"{Fore.CYAN}CATEGORIA    : {Fore.YELLOW}{nueva_categoria}")
                print("="*50)
                
            except:
                print(f"{Fore.RED}❌ Error al actualizar en la base de datos: ")

            print(f"\n{Fore.CYAN}🔄 Volviendo al menú principal...")
            input("\nPRESIONE ENTER PARA CONTINUAR")

#MENU
            print("\n1 ACTULIZAR OTRO PRODUCTO")
            print("2 VOLVER A MENU PRINCIPAL\n")
            opcion = input(f"\n{Fore.YELLOW}SELECCIONE : {Fore.WHITE}")

            if opcion == "1":
                os.system('cls')
                actualizar_producto()

            elif opcion == "2":
                os.system('cls')
                

                input("\nPRESIONE ENTER PARA SALIR")
                #break  # Sale del bucle principal y termina el programa
            else:
                print("SOLO 1 O 2")

###############################################################################################################
# ELIMINAR PRODUCTO POR ID


def eliminar():
   os.system("cls")
   print()
   dato = input(f"{Fore.CYAN}INGRESE EL ID DEL PRODUCTO A ELIMINAR : ")
   print()
   # Verificar si es solo numérico (y no vacío)
   
   if dato.isdigit():
      # Primero mostrar el registro que se va a eliminar
      cursor.execute('SELECT * FROM productos WHERE id = ?', (dato,))
      registro = cursor.fetchone()
      
      # Verificar si se encontró el registro
      if registro is None:
         print(f"{Fore.RED} NO EXISTE UN PRODUCTO CON EL ID: {dato}\n")
         input("\nPRECIONE ENTER PARA CONTINUAR")
         return
      # Crear un recuadro con el registro
      print(f"{Fore.YELLOW}{'='*60}")
      print(f"{Fore.RED}  REGISTRO A ELIMINAR ")
      print(f"{Fore.YELLOW}{'='*60}")
      print(f"{Fore.GREEN}ID: {registro[0]}")
      print(f"{Fore.GREEN}NOMBRE: {registro[1]}")
      print(f"{Fore.GREEN}PRECIO: {registro[2]}")
      print(f"{Fore.GREEN}CANTIDAD: {registro[3]}")
      print(f"{Fore.YELLOW}{'='*60}")
      
      # Preguntar confirmacion
      print()
      confirmar = input(f"{Fore.RED}¿Esta seguro que desea eliminar este registro? (S/N): ").upper()
      
      if confirmar == 'S':
         cursor.execute('DELETE FROM productos WHERE id = ?', (dato,))
         #conn.commit()
         cursor.connection.commit
         
         print(f"\n{Fore.GREEN} SE ELIMINO EL PRODUCTO CORRECTAMENTE.\n")
         input("\nPRECIONE ENTER PARA CONTINUAR")
      elif confirmar == 'N':
         print(f"\n{Fore.YELLOW} OPERACION CANCELADA. EL PRODUCTO NO FUE ELIMINADO.\n")
      else:
         print(f"\n{Fore.RED} OPCIÓN NO VÁLIDA. OPERACIÓN CANCELADA.\n")
      
   else:
      print(f"{Fore.RED}✗ SOLO NUMEROS\n")

##################################################################################################################


def buscar():
  
        def buscar_por_id():
            # BUSCAR PRODUCTO POR ID
            os.system("cls")
            print(Fore.CYAN + "\nBUSCAR PRODUCTO POR ID\n")
            
            id_buscar = input("Ingrese Id a buscar : ")
            print()

            cursor.execute('SELECT * FROM productos WHERE id = ?' , (id_buscar,))
            productos = cursor.fetchall()

            if not productos:
                    print('📭 No hay productos registrados.')
                    #return
            print()

            for p in productos:
                
                print(f'{Fore.WHITE}{Back.GREEN}SE ENCONTRO EL PRODUCTO\n')
                
                #print(f'{p[0]} - {p[1]} - {p[2]} - {p[3]} - {p[4]} - {p[5]}')
                
                print(Fore.GREEN + f"\nID          : {p[0]}")
                print(Fore.GREEN + f"Nombre      : {p[1]}")
                print(Fore.GREEN + f"Descripción : {p[2]}")
                print(Fore.GREEN + f"Cantidad    : {p[3]}")
                print(Fore.GREEN + f"Precio      : {p[4]}")
                print(Fore.GREEN + f"Categoría   : {p[5]}")


            input("\nPRESIONE ENTER PARA CONTINUAR\n")       


        def buscar_por_aproximacion():
                # BUSQUEDA POR PROXIMIDAD
            os.system("cls")
            print(Fore.YELLOW + "\nBUSCAR PRODUCTO POR PROXIMIDAD\n")
        
            termino_buscar = input("Ingrese término a buscar (ej: 'mou' para encontrar 'mouse'): ")
            print()

            # Agregar los % para la búsqueda por proximidad
            termino = f"%{termino_buscar}%"

            # Buscar en nombre, descripción o categoría
            cursor.execute('''
                SELECT * FROM productos 
                WHERE nombre LIKE ? 
                OR descripcion LIKE ? 
                OR categoria LIKE ?
            ''', (termino, termino, termino))

            productos = cursor.fetchall()

            # MOSTRAR RESULTADOS
            if not productos:
                print(Fore.RED + '📭 No hay productos registrados o no se encontraron coincidencias.')
            else:
                print(Fore.YELLOW + f"📝 Resultados para: '{termino_buscar}'")
                print(Fore.CYAN + "-" * 40)
                print(Fore.GREEN + f"\n✅ Se encontraron {len(productos)} producto(s):\n")
                
                
                for p in productos:
                    print(Fore.CYAN + "=" * 50)
                    print(f'{Fore.WHITE}{Back.GREEN} PRODUCTO {Back.RESET}\n')
                    
                    print(Fore.WHITE + f"ID          : {p[0]}")
                    print(Fore.WHITE + f"Nombre      : {p[1]}")
                    print(Fore.WHITE + f"Descripción : {p[2]}")
                    print(Fore.WHITE + f"Cantidad    : {p[3]}")
                    print(Fore.WHITE + f"Precio      : {p[4]}")
                    print(Fore.WHITE + f"Categoría   : {p[5]}")
                    print()

            input(Fore.CYAN + "\nPRESIONE ENTER PARA CONTINUAR\n")


        while True:
            os.system('cls')
            print(Fore.GREEN + "\nBUSCAR PRODUCTOS\n")
            print("1 Buscar por ID")
            print("2 Buscar por aproximación")  
            print("3 Salir")
            
            opcion = input("\nOpcion : ")
            
            if opcion == "1":
               buscar_por_id()
            elif opcion == "2":
               buscar_por_aproximacion()      
            elif opcion == "3":
                break
            else:
                print("\nOpcion invalida ")
                input()

#################################################################################################################
#Reporte de stock
def reporte():
    ahora = datetime.now()
    fecha = ahora.strftime("%d/%m/%Y")
    hora = ahora.strftime("%H:%M:%S")
 
    init(autoreset=True)
    os.system("cls")
        #limite = int(input("\nINGRESE LA CONSIDERACION DE STOCK BAJO: "))

    try:
        limite = int(input("\nINGRESE LA CONSIDERACION DE STOCK BAJO: "))

        cursor.execute("SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad", (limite,))
        resultados = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM productos WHERE cantidad = 0")
        sin_stock = cursor.fetchone()[0]

        #pass
    except:
        print(Fore.RED + "\n❌ Debe ingresar un número entero.")
        input("Presione ENTER para continuar...")
        return
        
    # Consultar productos con stock menor o igual al límite
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad", (limite,))
    resultados = cursor.fetchall()

    # Contar productos sin stock (cantidad = 0)
    cursor.execute("SELECT COUNT(*) FROM productos WHERE cantidad = 0")
    sin_stock = cursor.fetchone()[0]

    if not resultados:
        print(Fore.YELLOW + f"\n📭 No hay productos con cantidad ≤ {limite}.")
        print(f"Productos agotados (0 unidades): {sin_stock}")
        input("\nPresione ENTER para continuar...")
        return

    largo_max_0 = max(len(str(p[0])) for p in resultados)
    largo_max_1 = max(len(str(p[1])) for p in resultados)
    largo_max_2 = max(len(str(p[2])) for p in resultados)
    largo_max_3 = max(len(str(p[3])) for p in resultados)
    largo_max_4 = max(len(str(p[4])) for p in resultados)
    largo_max_5 = max(len(str(p[5])) for p in resultados)

    h0, h1, h2, h3, h4, h5 = "ID", "NOMBRE", "DESCRIPCION", "CANTIDAD", "PRECIO", "CATEGORIA"
    largo_max_0 = max(largo_max_0, len(h0)) + 2
    largo_max_1 = max(largo_max_1, len(h1)) + 2
    largo_max_2 = max(largo_max_2, len(h2)) + 2
    largo_max_3 = max(largo_max_3, len(h3)) + 2
    largo_max_4 = max(largo_max_4, len(h4)) + 2
    largo_max_5 = max(largo_max_5, len(h5)) + 2

    # Mostrar encabezado del reporte
    print(f"\nREPORTE DE INVENTARIO")
    print(f"{'▄' * 50}")
    print(f"STOCK BAJO (≤ {limite} unidades): {Fore.YELLOW}{len(resultados)} productos")
    print(f"AGOTADOS (Cantidad = 0): {Fore.RED}{sin_stock} productos")
    print(f"{'▄' * 50}\n")

    # Encabezados de tabla
    print(f"{Fore.CYAN}{h0:<{largo_max_0}} ║ {h1:<{largo_max_1}} ║ {h2:<{largo_max_2}} ║ {h3:<{largo_max_3}} ║ {h4:<{largo_max_4}} ║ {h5:<{largo_max_5}} ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * (largo_max_0 + largo_max_1 + largo_max_2 + largo_max_3 + largo_max_4 + largo_max_5 + 12)}{Style.RESET_ALL}")

    # Mostrar cada producto
    for p in resultados:
        color = Fore.RED if p[3] == 0 else Fore.WHITE
        simbolo = f"{Fore.WHITE}║{Fore.WHITE}"
        print(
            f"{color}{p[0]!s:<{largo_max_0}} {simbolo} "
            f"{color}{p[1]!s:<{largo_max_1}} {simbolo} "
            f"{color}{p[2]!s:<{largo_max_2}} {simbolo} "
            f"{color}{p[3]!s:<{largo_max_3}} {simbolo} "
            f"{color}${p[4]!s:<{largo_max_4 - 1}} {simbolo} "
            f"{color}{p[5]!s:<{largo_max_5}} {simbolo}"
        )

    ###############################################################################################################

    # Informe en txt
    print()

    informe = input("¿Desea exportar el stock bajo a un archivo? (S/N): ").strip().upper()

    if informe == "S":
        # Creo directorio si no existe
        directorio = Path(__file__).parent / 'Informes_Stock_Bajo'
        directorio.mkdir(parents=True, exist_ok=True)
        ruta_archivo = directorio / 'Info_Stock_Bajo.txt'
        
        try:
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                
                archivo.write(f"FECHA : {fecha} HORA : {hora}\n")
   
                archivo.write(f"REPORTE DE STOCK BAJO (≤ {limite} UNIDADES)\n")
                archivo.write(f"CANTIDAD DE PRODUCTOS SIN STOCK   : {sin_stock}\n")
                archivo.write(f"TOTAL DE PRODUCTOS CON STOCK BAJO : {len(resultados)}\n")
                archivo.write("\n")                        

                # Escribir encabezados
                archivo.write(f"{h0:<6} {h1:<32} {h2:<25} {h3:<8} {h4:<12} {h5:<15}\n")
                archivo.write("\n")                        

                # Escribir cada producto
                for p in resultados:
                    archivo.write(f"{p[0]:<6} {p[1]:<32} {p[2]:<25} {p[3]:<8} ${p[4]:<12} {p[5]:<15}\n")
            print(Fore.GREEN + f"\n✅ INFORME EXPORTADO CORRECTAMENTE en:\n{ruta_archivo}")
            archivo.close()

        except:
            print(Fore.RED + f"\n❌ Error al exportar el informe")
    else:
        print(Fore.CYAN + "\nExportación cancelada.")

    input("\nPresione ENTER para continuar...")

