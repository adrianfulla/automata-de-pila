''''
Lab 07 - Teoria de la Computación

Automata de pila

Autor: Adrian Fulladolsa Palma
Fecha: 6/10/2023
'''

class automata_de_pila:
    def __init__(self, Q, E, P, S, Z, d, F):
        self.Q = Q # Conjunto de estados
        self.E = E # Alfabeto de entrada
        self.P = P # Simbolos de pila
        self.S = S # Estado inicial
        self.Z = Z # Simbolo inicial de pila
        self.d = d # Funcion de transición
        self.F = F # Estados finales
        
        
def run_automata():
    Q = ['q0', 'q1', 'q2']
    E = [0,1]
    P = ['X', 'Z0']
    F=['q2']
    d={'q0': {0: {'Z0':['q0', 'XXZ0'], 'X':['q0', 'XX']},
                    1: {'X': ['q1', 'e']}
            },
           'q1': {1: {'X': ['q1', 'e']}, 'e':['q2','Z0']
            }
        }
    S= 'q0'
    Z = 'Z0'

    auto = automata_de_pila(Q, E, P, S, Z, d, F)

    
    
run_automata()
    