from modules.nodes import *
import random

# CLASE DE LISTA ENLAZADA
class LinkedList:
    def __init__(self):
        self.head = None


# AGREGAR LOS NODOS SECUENCIALMENTE
    def addInfo(self, points, category, name):
        newInfo = Node(points, category, name)
# VERIFICAMOS SI LA LISTA YA CONTIENE ALGUN NODO, CASO CONTRARIO ESTE NODO TOMARA LA PRIMERA POSICION
        if not self.head:
            self.head = newInfo
        else:
            a = self.head
# RECORREMOS LA LISTA HASTA EL ULTIMO NODO PARA HALLAR LA POSICION QUE LE CORRESPONDA AL NUEVO NODO
            while a.next:
                a = a.next
            a.next = newInfo


# INICIALIZAR LISTA CON VALORES ALEATORIOS PARA PUNTAJE Y CATEGORIA
    def initList(self):
        for i in players:
            puntaje = random.randint(0, 100)
            categoria = random.choice(categories)
            nombre = i
            self.addInfo(puntaje, categoria, nombre)


# AGREGAR NUEVO NODO AL INICIO DE LA LISTA
    def addFirst(self, points, category, name):
        newInfo = Node(points, category, name)
        newInfo.next = self.head
        self.head = newInfo


# INSERTAR NODO EN UNA POSICION ESPECIFICA SELECCIONADA POR EL USUARIO
    def add_in_position(self, points, category, name, position):
        newInfo = Node(points, category, name)
        index = 0
# VERIFICAMOS SI SE SELECCIONO EL PRIMER LUGAR DE LA LISTA
        if position == 0:
            self.addFirst(newInfo)
        else:
            a = self.head
# RECORREMOS LA LISTA HASTA BUSCAR LA POSICION INDICADA POR EL USUARIO
            while a and index < position - 1:
                a = a.next
                index += 1
# SI RECORRIO T0DA LA LISTA Y NO ENCONTRO LA POSICION INDICADA, SE LA AGREGA AL FINAL DE LA LISTA.
# LA VALIDACION DE LA POSICION PERMITE QUE SE INCLUYA LA ULTIMA POSICION DE LA LISTA
            if a is None:
                self.addInfo(newInfo)
# SE INSERTA EL NODO EN LA POSICION INDICADA POR EL USUARIO
            else:
                newInfo.next = a.next
                a.next = newInfo


# EDITAR LOS VALORES DE UN NODO POR SU POSICION
    def modifyNodoByPosition(self, position, name, category, points):
        a = self.head
        validator = True
        index = 0
# VERIFICAMOS SI SE SELECCIONO EL PRIMER LUGAR
        if position == 0:
# VERIFICAMOS SI LOS CAMPOS SON NULOS, SI SON NULOS NO REALIZA LA MODIFICACION
            if name is not None:
                a.name = name
            if category is not None:
                a.category = category
            if points is not None:
                a.points = points
            if name is None and category is None and points is None:
                print('\nNO SE HA REALIZADO NINGUNA MODIFICACION\n')
            if name is not None or category is not None or points is not None:
                print('\nNODO MODIFICADO CORRECTAMENTE\n')
# RECORREMOS LA LISTA EN BUSCA DE LA POSICION INDICADA POR EL USUARIO
        if position > 0:
            index += 1
            while validator == True:
                a = a.next
                if position == index:
                    if name is not None:
                        a.name = name
                    if category is not None:
                        a.category = category
                    if points is not None:
                        a.points = points
                    if name is None and category is None and points is None:
                        print('\nNO SE HA REALIZADO NINGUNA MODIFICACION\n')
                    if name is not None or category is not None or points is not None:
                        print('\nNODO MODIFICADO CORRECTAMENTE\n')
                    validator = False
                else:
                    index += 1


# ELIMINAR UN NODO DE ACUERDO A UNA CLAVE Y SU VALOR
    def deleteNodeByValue(self, key, value):
        if self.head is None:
            print('NO EXISTEN NODOS EN LA LISTA')
            return
        else:
            a = self.head   # REPRESENTA AL NODO A VERIFICAR
            b = None    # REPRESENTA AL NODO EN LA POSICION ANTERIOR
            counter = 0
            while a:
# REALIZAMOS EL RECORRIDO EN LA LISTA PARA BUSCAR COINCIDENCIAS CON EL ATRIBUTO Y SU VALOR PARA COMPARARLOS
                if getattr(a, key) == value:
                    counter += 1
                    if b is None:
                        self.head = a.next
                        a = self.head
                    else:
                        b.next = a.next
                        a = b.next
                else:
                    b = a
                    a = a.next
            return counter

# ELIMINAR UN NODO DE ACUERDO A SU POSICION EN LA LISTA
    def deleteNodeByPosition(self, position):
        if self.head is None:
            print('NO EXISTEN NODOS EN LA LISTA')
            return
        else:
            a = self.head
            b = None
            index = 0
            while a:
                # VERIFICAMOS SI SE SELECCIONO EL PRIMER LUGAR
                if position == index:
                    if position == 0:
                        self.head = a.next
                        return
                    else:
                        b.next = a.next
                        return
                else:
                    index += 1
                    b = a
                    a = a.next


# MOSTRAR LISTA
    def showList(self):
        print(f'\n************ TABLA DE JUGADORES ************')
        if self.head is None:
            print('NO EXISTEN NODOS EN LA LISTA')
            return False
        else:
            position = 0
            item = self.head
            while item != None:
                position+= 1
                print(f'{position}. [PUNTAJE: {item.points}; CATEGORIA: {item.category}; NOMBRE: {item.name}]')
                item = item.next
            print(f'\n')
            return True


# VALIDAR POSICION
    def validatePosition(self, position):
        counter = 0
        if position >= 1:
            item = self.head
            while item != None:
                counter += 1
                item = item.next
            if position <= counter:
                return False
            if position == counter + 1:
                return False
            else:
                return True
        else:
            print('*** LA POSICION DEBE SER MAYOR O IGUAL A 1 ***')
            return True


# SOLICITAR POSICION EN LA LISTA QUE DESEA INGRESAR EL NODO
    def requirePosition(self):
        validate = True
        while validate:
            try:
                position = int(input('INGRESE LA POSICION DEL NODO QUE DESEA PROCESAR: '))
                validate = self.validatePosition(position)
                if validate == True:
                    print(f'LA POSICION {position} INGRESADA NO EXISTE, VUELVE A INTENTARLO.\n')
                else:
                    return position - 1
            except ValueError as e:
                print(f'ERROR: {e} => DEBE INGRESAR UN NUMERO')





''' FUNCION POR DESARROLLAR EN EL FUTURO
        # EDITAR LOS VALORES DE UN NODO MEDIANTE BUSQUEDA DEL CLAVE-VALOR
        def modifyNodeByValue(self, key, value, name, points, category):
            a = self.head
            counter = 0
            while a:
                if getattr(a, key) == value:
                    counter += 1
                    if a.name is not None:
                        a.name = name
                    if points is not None:
                        a.points = points
                    if category is not None:
                        a.category = category
                a = a.next
            return counter'''

