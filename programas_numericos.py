def enumeracion(objetivo):
    respuesta = 0


    while respuesta**2 < objetivo: #Enumera todas las soluciones posibles
        print(respuesta)
        respuesta += 1


    if respuesta**2 == objetivo: #Evalúa las soluciones de acuerdo a las restricciones del problema
        return respuesta
    else:
        print(f'{objetivo} no tiene raíz cuadrada exacta') 


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0


    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso


    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raíz cuadrada de {objetivo}')
    else:
        return respuesta

    
def busq_binaria(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon: 
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    
    return respuesta


method = input('''Escoge el método para calcular la raíz cuadrada
            [E]numeración exhaustiva 
            [A]proximación de soluciones
            [B]úsqueda binaria
            ''')


objetivo = int(input('Escoge un número entero: '))


if method == 'e' or method == 'E':
    result = enumeracion(objetivo)
    # print(f'La raíz cuadrada de {objetivo} es {result}')

elif method == 'a' or method == 'A':
    result = aproximacion(objetivo)
    # print(f'La raíz cuadrada de {objetivo} es {result}')

elif method == 'b' or method == 'B':
    result = busq_binaria(objetivo)
    # print(f'La raíz cuadrada de {objetivo} es {result}')

else:
    print('No escogiste un método')    

if result != None:
    print(f'La raíz cuadrada de {objetivo} es {result}')




