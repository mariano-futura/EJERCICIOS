import random, time, sys, psutil, os
def INICIAR():
    articulos={}
    finalizar=False
    opcion=0
    while not finalizar:
        limpiar_consola()
        print('MENU APP')
        print('1. Dar de ALTA nuevos Articulos')
        print('2. Listar todos los Articulos')
        print('3. Borrar un articulo')
        try:
            opcion=int(input('Introduce la opcion deseada. INTRO para terminar'))
        except ValueError:
            pass

        if opcion==0:
            finalizar=True
        elif opcion==1:
            cargarArticulos(articulos)
        elif opcion==2:
            imprimir(articulos)
        elif opcion==3:
            eliminar(articulos)
        else:
            print('Opcion no valida...')

def eliminar(articulos):
    codigo_eliminar=int(input('Introduce el codigo de articulo a Eliminar: '))
    if codigo_eliminar in articulos:
        descripcion=articulos[codigo_eliminar][0]
        del articulos[codigo_eliminar]
        input(f'El articulo {descripcion} ha sido ELIMINADO con EXITO. Pulse una tecla.')
    else:
        input(f'!!! El codigo de Articulo {codigo_eliminar} no EXISTE. Pulse INTRO para continuar !!!')
def cargarArticulos(articulos):
    continuar = 's'

    while continuar.lower() == 's':
        #numero = float(input("Introduce un número: ")) if input("Introduce un número: ").isdigit() else 0.0

        idArticulo = articulos[articulos.__len__()]

        des_articulo = input('Introduce el nombre del artículo: ')
        pre_articulo = float(input('Introduce el precio: '))
        stk_articulo = float(input('Introduce el stock: '))

        articulos[idArticulo] = (des_articulo, pre_articulo, stk_articulo)

        print(f'Artículo {idArticulo} - {des_articulo} guardado con ÉXITO.')

        continuar = input('¿Desea continuar? [s/n]: ')

    return articulos
def cargaAutomatica(numero_de_elementos=1000):
    articulos = {}
    for codigo in range(1,numero_de_elementos):
        des_articulo = f'Articulo_{codigo}'
        pre_articulo = round(random.uniform(1, 200), 2)
        stk_articulo = random.randint(1, 1000)
        articulos[codigo]=(des_articulo,pre_articulo,stk_articulo)
        #print(f'Generando {numero_de_elementos} articulos aleatorios:')
        #print(codigo)
    tamano_diccionario = sys.getsizeof(articulos)
    input(f'Los articulos ocupan {round(tamano_diccionario/(1024*1024),3)} Megas. Pulsa una tecla para continuar...')
    return articulos
def imprimir(articulos, stockminimo=0):
    print('Listado completo de productos:')
    cuenta=0
    for codigo in articulos:
        if (stockminimo == 0) or (articulos[codigo][2] <= stockminimo):
            cuenta+=1
            print(codigo,articulos[codigo][0],articulos[codigo][1],articulos[codigo][2])
    input(f'Numero contados {cuenta}, pulsa una tecla para continuar...')
def consulta(articulos):
    continua = True
    while continua:
        codigo=int(input('Introduce el código del articulo a consultar o pulse -1 para terminar:'))
        if codigo == -1:
            continua = False
        if codigo in articulos:
            print(codigo,articulos[codigo][0],articulos[codigo][1])
        else:
            print(f'El código de articulo {codigo} NO EXISTE')
def dimeTiempoTranscurrido(inicio):
    tiempo_transcurrido=time.time() - inicio
    horas=int(tiempo_transcurrido // 3600)
    minutos=int((tiempo_transcurrido % 3600) // 60)
    segundos=int(tiempo_transcurrido % 60)
    centesimas = int((tiempo_transcurrido % 1) * 100)
    print(f'Han transcurrido {horas} horas {minutos} minutos {segundos} segundos y {centesimas} centesimas')
def infoMemoria():
    # Obtener la memoria máxima del sistema en bytes
    memoria_maxima = psutil.virtual_memory().total

    # Obtener la memoria utilizada del sistema en bytes
    memoria_utilizada = psutil.virtual_memory().used

    # Obtener la memoria disponible del sistema en bytes
    memoria_disponible = psutil.virtual_memory().available

    # Imprimir la información en megabytes
    print('INFORME DE MEMORIA UTILIZADA:')
    print(f"Memoria máxima: {memoria_maxima / (1024 ** 2)} MB")
    print(f"Memoria utilizada: {memoria_utilizada / (1024 ** 2)} MB")
    print(f"Memoria disponible: {memoria_disponible / (1024 ** 2)} MB")
    input('Pulsa una tecla para continuar..')
def limpiar_consola():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Otros sistemas (Linux, macOS)
        os.system('clear')

INICIAR()