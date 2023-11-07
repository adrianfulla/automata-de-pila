''''
Lab 07 - Teoria de la Computación

Automata de pila

Autor: Adrian Fulladolsa Palma
Fecha: 6/10/2023
'''

class automata_de_pila:
    def __init__(self, Q, E, P, S, Z, d, F):
        self.Q = Q # Conjunto de estados
        self.E = E # Simbolos de entrada
        self.P = P # Simbolos de pila
        self.S = S # Estado inicial
        self.Z = Z # Simbolo inicial de pila
        self.d = d # Subset finito
        self.F = F # Funcion
        