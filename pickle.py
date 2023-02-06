import pickle

# Clase que representa el estado de ejecución
class ExecutionState:
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2

# Función para guardar el estado de ejecución en un archivo
def save_state(state, filename):
    with open(filename, 'wb') as f:
        pickle.dump(state, f)

# Función para cargar el estado de ejecución desde un archivo
def load_state(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Crear un objeto ExecutionState
execution_state = ExecutionState(1, 2)

# Guardar el estado de ejecución en un archivo
save_state(execution_state, 'execution_state.pkl')

# Cargar el estado de ejecución desde un archivo
restored_state = load_state('execution_state.pkl')

# Verificar que se haya restaurado el estado de ejecución correctamente
print(restored_state.variable1)
print(restored_state.variable2)

"""
En este ejemplo, creamos una clase "ExecutionState" que representa el estado de ejecución que queremos guardar. 
Luego, definimos dos funciones "save_state" y "load_state" que utilizan pickle para guardar y cargar el estado de ejecución, 
respectivamente. Finalmente, creamos un objeto "ExecutionState", lo guardamos en un archivo y lo cargamos de nuevo para verificar 
que se haya restaurado correctamente.
"""