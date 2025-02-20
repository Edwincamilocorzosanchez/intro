#juego el ahorcad1
import random
import os
palabras = ['hola','perro','carro','arbol','helado','fresa','uva','color','rosado','vaca']
print('bienvenido usuario')
print('1: jugar')
print('2: no jugar')
jugar = int(input('desea jugar elige la opcion:'))
if jugar==1:
    num = int(input('escoge un numero para elegir la palabra'))
palabra_secreta = random.randint(1, len (palabras))
foundletters = True
intentos = 0

palabra= palabras[palabra_secreta]
letras = ['_'] * len (palabra)
while jugar:
    os.system('cls')
    print('adivina la palabra')
    for letra in letras:
        print(letra, end=' ')
    print('\n')
    print(f'intentos restantes: {3 - intentos}')
    foundletters = False
    letrass = input('ingresa una letra: ')
    for idx,ltr in enumerate(palabra):
        if ltr.upper() == letrass.upper():
            letras[idx] == letrass.upper()
            foundletters : True
            continue
else:
    foundletters == False
    intentos += 1
if intentos == 3:
    print('perdiste')
    jugar == False
elif ''. join(letras).upper == palabra.upper():
    print(f'felicitaciones has adivinado la palabra: {palabra}')
    jugar = False














    

    



