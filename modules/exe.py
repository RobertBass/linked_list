from modules.services import *
import time

def exe():
    list = LinkedList()
    list.initList()

    print('=======================================================================')
    print('===================== SISTEMA DE LISTAS ENLAZADAS =====================')
    print('=======================================================================')
    time.sleep(1)
    while True:
        validate = True
        option = 0
        mainMenu()  # MOSTRAMOS EL MUNU PRINCIPAL AL USUARIO
        time.sleep(1)
        while validate:
            try:
                option = int(input('SELECCIONA UNA OPCION DEL MENU: '))
                validate = validateSelection(1,5, option)
                time.sleep(1)
            except ValueError as e:
                print(f'\nERROR: {e} => DEBE INGRESAR UN NUMERO\n')

# MOSTRAR LISTA
        if option == 1:
            list.showList()
            time.sleep(3)

# AGREGAR NODO A LA LISTA
        if option == 2:
            addMenu()   # MOSTRAMOS MENU SECUNDARIO PARA AGREGAR NODO
            validate2 = True
            option2 = 0
            time.sleep(1)
            while validate2:
                try:
                    option2 = int(input('SELECCIONA UNA OPCION: '))
                    validate2 = validateSelection(1, 4, option2)
                    time.sleep(1)
                except ValueError as e:
                    print(f'\nERROR: {e} => DEBE INGRESAR UN NUMERO\n')

# AGREGAR NODO AL INICIO DE LA LISTA
            if option2 == 1:
                name = requireName()
                points = requirePoints()
                category = requireCategory()
                list.addFirst(points, category, name)
                time.sleep(1)
                print('\nDATOS ALMACENADOS CORRECTAMENTE AL INICIO DE LA LISTA\n')

# AGREGAR NODO AL FINAL DE LA LISTA
            if option2 == 2:
                name = requireName()
                points = requirePoints()
                category = requireCategory()
                list.addInfo(points, category, name)
                time.sleep(1)
                print('\nDATOS ALMACENADOS CORRECTAMENTE EN LA ULTIMA POSICIÓN DE LA LISTA\n')

# AGREGAR NODO EN UNA POSICION ESPECIFICA
            if option2 == 3:
                name = requireName()
                points = requirePoints()
                category = requireCategory()
                list.showList()
                time.sleep(3)
                position = list.requirePosition()
                list.add_in_position(points, category, name, position)
                time.sleep(1)
                print(f'\nDATOS ALMACENADOS CORRECTAMENTE EN LA POSICION {position + 1}\n')

# SALIR DEL PROCESO
            if option2 == 4:
                print('\nREGRESANDO AL MENU PRINCIPAL\n')

# MODIFICAR NODO
        if option == 3:
            list.showList()
            time.sleep(2)
            position = list.requirePosition()
            name, category, points = requireChanges()
            list.modifyNodoByPosition(position, name, category, points)
            time.sleep(1)

# ELIMINAR NODO
        if option == 4:
            deleteMenu()
            validate3 = True
            option3 = 0
            time.sleep(1)
            while validate3:
                try:
                    option3 = int(input('SELECCIONA UNA OPCION: '))
                    validate3 = validateSelection(1, 3, option3)
                    time.sleep(1)
                except ValueError as e:
                    print(f'ERROR: {e} => DEBE INGRESAR UN NUMERO')

# ELIMINAR NODO POR SU CLAVE Y VALOR, ESTO ELIMINA TODOS LOS NODOS QUE CUMPLAN CON LA CONDICION
            if option3 == 1:
                validate3 = list.showList()
                time.sleep(2)
                if validate3 == True:
                    step = input('\nDEBE CONSIDERAR QUE AL ELIMINAR EN ESTA OPCION, ELIMINARAS NODOS QUE CUMPLAN CON LA '
                             'CONDICION INGRESADA. ESTAS SEGURO DE CONTINUAR? (S => CONTINUAR): ').upper()
                    if step == 'S':
                        key =  requireKey()
                        value = requireValue(key)
                        counter = list.deleteNodeByValue(key, value)
                        time.sleep(1)
                        if counter == 0:
                            print('\nNO SE ENCONTRARON NODOS CON EL CRITERIO DE BUSQUEDA\n')
                        else:
                            print(f'\n{counter} NODO(S) ELIMINADO(S) EN EL PROCESO\n')
                else:
                    print('REGRESANDO AL MENU PRINCIPAL')

# ELIMINAR NODO POR SU POSICION EN LA LISTA
            if option3 == 2:
                validate3 = list.showList()
                time.sleep(2)
                if validate3 == True:
                    position = list.requirePosition()
                    step = input(
                        f'\nESTAS SEGURO DE CONTINUAR CON LA ELIMINACION DEL NODO EN LA POSICION {position + 1}? (S => CONTINUAR): ').upper()
                    if step == 'S':
                        list.deleteNodeByPosition(position)
                        time.sleep(1)
                        print(f'\nNODO EN LA POSICION {position + 1} ELIMINADO CORRECTAMENTE\n')
                    else:
                        print('REGRESANDO AL MENU PRINCIPAL')
                else:
                    print('REGRESANDO AL MENU PRINCIPAL')

# SALIR DEL PROCESO
            if option3 == 3:
                print('\nREGRESANDO AL MENU PRINCIPAL\n')

# SALIR DEL PROGRAMA
        if option == 5:
            print('SALIENDO DEL PROGRAMA, VUELVA PRONTO...')
            time.sleep(2)
            exit(0)


