# Definir el alfabeto
alphabet = {'a', 'b'}

# Definir los estados
states = {'q0', 'q1', 'q2', 'q3'}

# Definir el estado inicial
start_state = 'q0'

# Definir los estados finales
final_states = {'q0', 'q2'}

# Definir las transiciones
transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q0', 'b': 'q3'},
    'q2': {'a': 'q3', 'b': 'q2'},
    'q3': {'a': 'q2', 'b': 'q1'}
}

# Función que verifica si una cadena es aceptada por el automáta
def accepts(string):
    current_state = start_state
    for c in string:
        if c not in alphabet:
            return False
        current_state = transitions[current_state].get(c)
        if current_state is None:
            return False
    return current_state in final_states

# Ejemplo de uso
input_string = 'abbaaabb'
if accepts(input_string):
    print(f'La cadena "{input_string}" es aceptada por el automáta')
else:
    print(f'La cadena "{input_string}" no es aceptada por el automáta')