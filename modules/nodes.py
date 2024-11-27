# VARIABLES PARA INFORMACION INICIAL DE LOS NODOS
categories = ['J', 'S', 'M']
players = ['VICTOR', 'BRUNO', 'EMILIO', 'NICOLAS', 'EMMA']


class Node:
    def __init__(self, points, category, name):
        self.points = points
        self.category = category
        self.name = name
        self.next = None




