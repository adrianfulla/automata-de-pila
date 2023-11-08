''''
Lab 07 - Teoria de la Computación

Automata de pila

Autor: Adrian Fulladolsa Palma
Fecha: 6/10/2023
'''

import random
from datetime import datetime

class automata_de_pila:
    def __init__(self, Q, E, P, S, Z, d, F):
        self.Q = Q # Conjunto de estados
        self.E = E # Alfabeto de entrada
        self.P = P # Simbolos de pila
        self.S = S # Estado inicial
        self.Z = Z # Simbolo inicial de pila
        self.d = d # Funcion de transición
        self.F = F # Estados finales
        
    def run(self, input_string):
        # Inicializa la pila con el símbolo inicial de pila
        stack = [self.Z]
        current_state = self.S
        
        for symbol in input_string:
            if symbol not in self.E:
                print(f"Error: El símbolo '{symbol}' no está en el alfabeto de entrada.")
                return False

            if current_state not in self.Q:
                print(f"Error: El estado actual '{current_state}' no es válido.")
                return False

            if stack[-1] not in self.P:
                print(f"Error: El símbolo en la cima de la pila '{stack[-1]}' no es válido.")
                return False
            
            if current_state not in self.d:
                print(f"Error: El estado actual '{current_state}' no tiene transiciones validas.")
                if current_state == "q2":
                    print(f"Cadena: {input_string},simbolo: {symbol}")
                return False
            
            if symbol in self.d[current_state]:
                if stack[-1] in self.d[current_state][symbol]:
                    transition = self.d[current_state][symbol][stack[-1]]
                    new_state, stack_symbols = transition
                    current_state = new_state
                    
                    if stack_symbols == 'e':
                        stack.pop()  # Desapila el símbolo superior
                    else:
                        # Apila los símbolos de stack_symbols (en orden inverso)
                        for s in reversed(stack_symbols):
                            stack.append(s)
                else:
                    print(f"Error: No se encontró una transición para el símbolo '{symbol}' en el estado '{current_state}' con '{stack[-1]}' en la cima de la pila.")
                    return False

            elif 'e' in self.d[current_state]:
                symbol = 'e'
                if stack[-1] in self.d[current_state][symbol]:
                    transition = self.d[current_state][symbol][stack[-1]]
                    new_state, stack_symbols = transition
                    current_state = new_state
                    
                    if stack_symbols == 'e':
                        stack.pop()  # Desapila el símbolo superior
                    else:
                        # Apila los símbolos de stack_symbols (en orden inverso)
                        for s in reversed(stack_symbols):
                            stack.append(s)
                else:
                    print(f"Error: No se encontró una transición para el símbolo '{symbol}' en el estado '{current_state}' con '{stack[-1]}' en la cima de la pila.")
                    return False
            else:
                print(f"Error: No se encontró una transición para el símbolo '{symbol}' en el estado '{current_state}' con '{stack[-1]}' en la cima de la pila.")
                return False

        if current_state in self.F:
            print(f"La cadena {input_string} fue aceptada por el autómata.")
            return True
        else:
            print(f"La cadena {input_string} no fue aceptada por el autómata.")
            return False

def generate_expressions(E):
    n = len(E)
    random.seed(datetime.now().timestamp())
    expressions = []
    
    for _ in range(random.randint(1, 100)):
        expression = ""
        for _ in range(random.randint(1, 15)):
            expression += E[random.randint(0, n-1)]
        expressions.append(expression)
    
    return expressions

# Ejemplo de uso
if __name__ == "__main__":
    Q = ['q0', 'q1', 'q2']
    E = ['0', '1']
    P = ['X', 'Z0']
    F = ['q2']
    d = {'q0': {'0': {'Z0': ['q0', ['X', 'X', 'Z0']], 'X': ['q0', ['X', 'X']]},
                '1': {'X': ['q1', 'e']}
                },
         'q1': {'1': {'X': ['q1', 'e']}, 
                'e': {'Z0': ['q2', ['Z0']]}
                }
         }
    S = 'q0'
    Z = 'Z0'

    auto = automata_de_pila(Q, E, P, S, Z, d, F)
    input_string = '0110'  # Reemplaza esto con la cadena que quieras probar
    auto.run(input_string)
    
    #print("Expresiones aleatoria")
    
    expressions = generate_expressions(E)
    aceptados = []
    rechazados = []
    for expression in expressions:
        if auto.run(expression):
            aceptados.append(expression)
        else:
            print(f"La cadena {expression} no fue aceptada por el autómata")
            rechazados.append(expression)
     
    print("---------------------------------------------------------------")       
    print("Expresiones aceptadas")
    for e in aceptados:
        print(e)
        