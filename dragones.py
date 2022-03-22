

import random
import time

def mostrarIntroduccion():
    print('Estas en una tierra lleno de dragones. Frente a ti')
    print('hay dos cuevas. En una de ellas, el dragon es generoso y')
    print('amigable y compartira su dinero contigo. El otro dragon')
    print('Es codicioso y esta hambriento, y te deborara inmediatamente.')
    print()

def elegirCueva():
    cueva= ''
    while cueva != '1' and cueva != '2':
        print('¿A qué cueva quires entrar? (1 ó 2)')
        cueva =input()

    return cueva

def explorarCueva(cuevaElegida):
    print('te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print()
    print('!Un gran dragon aparece subitamente frente a ti¡ Abre sus fauces y ...')
    print()
    time.sleep(4)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
        print('!Te regala su tesoro¡')
        time.sleep(2)
        print()
        print('PRO')

    else:
        print('!Te engulle de un bocado¡')
        time.sleep(2)
        print()
        print('LOOSER')

        
jugarDeNuevo = 'si'

while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

      mostrarIntroduccion()

      numeroDeCueva = elegirCueva()

      explorarCueva(numeroDeCueva)

      print('¿Quieres jugar de nuevo? (si o no)')
      
      jugarDeNuevo = input()
      

    




    
        
    

    
