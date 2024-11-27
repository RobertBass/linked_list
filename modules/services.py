from modules.linked_list import *


# MENU PRINCIPAL
def mainMenu():
    print('\n******  MENU PRINCIPAL  ******')
    print('1. MOSTRAR LISTA')
    print('2. AGREGAR NODO')
    print('3. MODIFICAR NODO')
    print('4. ELIMINAR NODO')
    print('5. SALIR\n')


# MENU AGREGAR NODO
def addMenu():
    print('\n******  SELECCIONA UNA OPCION  ******')
    print('1. AGREGAR NODO AL INICIO')
    print('2. AGREGAR NODO AL FINAL')
    print('3. AGREGAR NODO EN UNA POSICION ESPECIFICA')
    print('4. VOLVER AL MENU PRINCIPAL\n')


# MENU DE ELIMINAR NODO
def deleteMenu():
    print('\n******  SELECCIONA UNA OPCION  ******')
    print('1. ELIMINAR NODO POR VALOR')
    print('2. ELIMINAR NODO POR POSICION')
    print('3. VOLVER AL MENU PRINCIPAL\n')


# VALIDAR QUE NOMBRE NO ESTE VACIO Y QUE SOLO CONTENGA LETRAS
def validateName(name):
    if name != '' and name.isalpha() and len(name) >= 2:
        return False
    else:
        print('\n*** VERIFICA QUE NO ENVIES UN CAMPO VACIO, QUE SOLO CONTENGA LETRAS Y QUE TENGA AL MENOS 2 CARACTERES ***\n')
        return True


# VALIDAR QUE LA CATEGORIA SEA VALIDA
def validateCategory(category):
    if category in categories:
        return False
    else:
        print('\n*** DEBES ESCOGER UNA CATEGORIA ENTRE J, S o M ***\n')
        return True


# VALIDAR QUE EL PUNTAJE ESTE DENTRO DEL RANGO DE 0 A 100
def validatePoints(points):
    if points >= 0 and points <= 100:
        return False
    else:
        print(f'\n*** OPCION NO VALIDA, DEBES ESCOGER UNA OPCION ENTRE 0 Y 100 ***\n')
        return True


# VALIDAR SELECCION DEL MENU
def validateSelection(a, b, option):
    if option >= a and option <= b:
        return False
    else:
        print(f'\n*** OPCION NO VALIDA, DEBES ESCOGER UNA OPCION ENTRE {a} Y {b} ***\n')
        return True


# SOLICITAR NOMBRE DEL JUGADOR
def requireName():
    global name
    validate = True
    while validate == True:
        try:
            name = input('INGRESA EL NOMBRE DEL JUGADOR: ').upper()
            validate = validateName(name)
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR EL NOMBRE DEL JUGADOR\n')
    return name


# SOLICITAR PUNTAJE DEL JUGADOR
def requirePoints():
    global points
    validate = True
    while validate:
        try:
            points = int(input('INGRESA EL PUNTAJE DEL JUGADOR (0 - 100): '))
            validate = validatePoints(points)
        except ValueError as e:
            print(f'\nERROR: {e} => DEBE INGRESAR UN NUMERO\n')
    return points


# SOLICITAR CATEGORIA DEL JUGADOR
def requireCategory():
    global category
    validate = True
    while validate:
        try:
            category = input('INGRESA LA CATEGORIA DEL JUGADOR (J / S / M): ').upper()
            validate = validateCategory(category)
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR UNA OPCION\n')
    return category


# SOLICITAR CLAVE DE BUSQUEDA
def requireKey():
    global key
    validate = True
    print('DEBES SELECCIONAR UNA OPCION DE BUSQUEDA ENTRE LAS SIGUIENTES OPCIONES:')
    print('C = CATEGORIA')
    print('N = NOMBRE')
    while validate:
        try:
            valor = input('SELECCIONA UNA OPCION DE BUSQUEDA: ').upper()
            if valor == 'C' or valor == 'N':
                if valor == 'C':
                    key = 'category'
                elif valor == 'N':
                    key = 'name'
                validate = False
            else:
                print('\nOPCION DE BUSQUEDA NO VALIDA, VUELVE A INTENTARLO\n')
                validate = True
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR UNA OPCION\n')
    return key


# SOLICITAR VALOR
def requireValue(key):
    if key == 'category':
        value = requireCategory()
    else:
        value = requireName()
    return value


# SOLICITAR DATOS A MODIFICAR EN LA LISTA
def requireChanges():
    name = None
    category = None
    points = None
    validator = True
    while validator == True:
        try:
            option = input('DESEA MODIFICAR EL NOMBRE DEL JUGAROR? (S/N): ').upper()
            if option == 'S':
                name = requireName()
                validator = False
            elif option == 'N':
                validator = False
            else:
                print(f'\n{option} NO ES UNA OPCION VALIDA, VUELVE A INTENTARLO.\n')
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR UNA OPCION\n')
    while validator == False:
        try:
            option = input('DESEA MODIFICAR LA CATEGORIA DEL JUGADOR? (S/N):').upper()
            if option == 'S':
                category = requireCategory()
                validator = True
            elif option == 'N':
                validator = True
            else:
                print(f'\n{option} NO ES UNA OPCION VALIDA, VUELVE A INTENTARLO.\n')
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR UNA OPCION\n')
    while validator == True:
        try:
            option = input('DESEA MODIFICAR EL PUNTAJE DEL JUGADOR? (S/N):').upper()
            if option == 'S':
                points = requirePoints()
                validator = False
            elif option == 'N':
                validator = False
            else:
                print(f'\n{option} NO ES UNA OPCION VALIDA, VUELVE A INTENTARLO.\n')
        except ValueError as e:
            print(f'\nERROR: {e} => CAMPO VACIO, DEBES INGRESAR UNA OPCION\n')

    return name, category, points




''' PARA FUTURA IMPLEMENTACION
# MENU DE MODIFICAR NODO
def modifyMenu():
    print('\n******  SELECCIONA UNA OPCION  ******')
    print('1. MODIFICAR NODO POR VALOR')
    print('2. MODIFICAR NODO POR POSICION\n')

'''