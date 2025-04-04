from collections import deque
#coding=utf-8

"""
===============================================================================
 Programa: EjemploPilasColas
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostración inicial del funcionamiento y diferencias entre una pila y una cola

 ===============================================================================
"""
def visualiza_participantes(una_pila):
    print(f'\n la cantidad participantes es: {len(una_pila)}')
    print('los participantes son: ')
    
    for participantes in una_pila:
        print(f'° {participantes}')
   
    
def visualiza_pacientes(una_cola):
    print(f'\nLa cantidad de pacientes es: {len(una_cola)}')
    print('Los pacientes son: ')
    for paciente in una_cola:
        print(f' - {paciente}')


print('Programa para demostrar el  funcionamiento de pilas y colas')
print('\n Para una pila - Principio LIFO:') # Pila - Stack

pila_participantes = []
pila_participantes.append('Miguel')
pila_participantes.append('Felipe')
pila_participantes.append('Tatiana')
pila_participantes.append('otro Miguel')

visualiza_participantes(pila_participantes)

#quitamos el ultimo de la cola
ultimo_participante= pila_participantes.pop()
print(f'\nEl último participante es {ultimo_participante}')

visualiza_participantes(pila_participantes)

siguiente_en_salir = pila_participantes.pop()
print(f'\nEl siguiente participante es {siguiente_en_salir}')
visualiza_participantes(pila_participantes)


print('\n Para una Cola - Principio FIFO') #Cola - Queue
cola_pacientes = deque()

cola_pacientes.append('Otro Miguel')
cola_pacientes.append('Mariana')
cola_pacientes.append('Emmanuel')

visualiza_pacientes(cola_pacientes)
siguiente_paciente = cola_pacientes.popleft()
print(f'El siguiente paciente es {siguiente_paciente}')
visualiza_pacientes(cola_pacientes)

